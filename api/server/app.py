from flask import Flask, request, jsonify
import hashlib, tempfile, time, os, shutil, glob, collections

app = Flask(__name__)
# Set the maximum content length to 4MB
app.config['MAX_CONTENT_LENGTH'] = 4 * 1024 * 1024
# Set the disk space miniumum to 256MB
app.config['MIN_DISK_SPACE'] = 256 * 1024 * 1024

# Specify the directory where uploaded files will be saved
app.config['UPLOAD_FOLDER'] = os.path.join(os.getcwd(), 'uploads')

# Throttling rate limit
app.config['UPLOAD_LIMIT'] = 64 * 1024 * 1024   # MB per day


# Implements OpenAPI 3.0.3 /upload/ipynb endpoint
@app.route('/upload/ipynb', methods=['POST'])
def upload_ipynb():
    content_length = request.content_length
    if content_length is None or content_length > app.config['MAX_CONTENT_LENGTH']:
        return jsonify({'status': 'error', 'message': 'File size exceeds maximum allowed'}), 413
    
    # Get client IP address from X-Forwarded-For header
    if request.headers.getlist("X-Forwarded-For"):
        client_ip = request.headers.getlist("X-Forwarded-For")[0]
    else:
        client_ip = request.remote_addr
    
    # Create a temporary file to save the uploaded chunks
    temp_file = tempfile.NamedTemporaryFile(delete=True)

    # Check if the temporary file was created successfully and return an error if not
    if temp_file is None:
        return jsonify({'status': 'error', 'message': 'Failed to process the request'}), 500
    
    # Check if there is enough disk space to save the file
    if shutil.disk_usage(app.config['UPLOAD_FOLDER']).free < app.config['MIN_DISK_SPACE']:
        return jsonify({'status': 'error', 'message': 'Failed to process the request'}), 500

    if shutil.disk_usage(temp_file.name).free < app.config['MIN_DISK_SPACE']:
        return jsonify({'status': 'error', 'message': 'Failed to process the request'}), 500

    # Define a path UPLOAD_FOLDER/IP/today's date, if doesn't exists, create it
    # If exists, check disk usage for that folder if it is larger than UPLOAD_LIMIT, return error
    new_folder_path = os.path.join(app.config['UPLOAD_FOLDER'], f'{client_ip}', f'{time.strftime("%Y-%m-%d")}')
    if not os.path.exists(new_folder_path):
        os.makedirs(new_folder_path, exist_ok=True)
    else:
        if shutil.disk_usage(new_folder_path).used > app.config['UPLOAD_LIMIT']:
            return jsonify({'status': 'error', 'message': 'Too many requests, please try again later'}), 429            

    # Process file upload in chunks
    chunk_size = 4096
    file_hash = hashlib.md5()
    while True:
        chunk = request.stream.read(chunk_size)
        if not chunk:
            break

        # Check of temporary file size exceeds maximum allowed
        if temp_file.tell() + len(chunk) > app.config['MAX_CONTENT_LENGTH']:
            return jsonify({'status': 'error', 'message': 'File size exceeds maximum allowed'}), 413

        # Calculate file hash in chunks and write to temporary file
        file_hash.update(chunk)
        temp_file.write(chunk)

    # Check if there is enough disk space to save the file
    if shutil.disk_usage(app.config['UPLOAD_FOLDER']).free < app.config['MIN_DISK_SPACE']:
        return jsonify({'status': 'error', 'message': 'Failed to process the request'}), 500

    # Flush temporary file to disk
    temp_file.flush()

    # Resolve file path and name
    file_hash = file_hash.hexdigest()
    new_file_path = os.path.join(new_folder_path, f'{file_hash}')

    # check if the duplicate data that starts with the same same hash already exists
    if glob.glob(f'{new_file_path}*'):
        return jsonify({'status': 'error', 'message': 'Failed to process the request'}), 500

    # Copy temporary file into permanent storage, include file hash and timestamp
    new_file_name = f'{new_file_path}.{client_ip}.{int(time.time())}.ipynb'
    shutil.copy(temp_file.name, new_file_name)

    # Close temporary file which will delete it
    temp_file.close()

    # File upload complete, return success response
    response = {'status': 'success', 'message': 'File uploaded successfully'}
    return jsonify(response)


# Test code to upload a file
if __name__ == '__main__':
    app.run(host = '127.0.0.1')