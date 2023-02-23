
import requests

# Set the URL of the Flask server
url = 'http://api.pattern.foundation/upload/ipynb'

# Set the path of the file to upload
file_path = 'test.py'

# Open the file and set up the request headers
with open(file_path, 'rb') as f:
    headers = {'Content-Type': 'application/octet-stream'}

    # Send the file in chunks using a POST request
    r = requests.post(url, data=f, headers=headers)

# Print the response from the server
print(r.text)
