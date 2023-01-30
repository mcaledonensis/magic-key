import gradio as gr

def interact(state, text):
    state = state + [(text, text + "?")]
    return state, state

class Window(gr.Chatbot):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


with gr.Blocks(css="#window .overflow-y-auto{height:300px}") as demo:
    gr.Markdown("""<h1><center>Build Yo'own ChatGPT with OpenAI API & Gradio</center></h1>""")
    window = Window(elem_id="window")
    state = gr.State([])
    
    with gr.Row():
        txt = gr.Textbox(show_label=False, placeholder="Enter text or markdown and press enter").style(container=False)
            
    txt.submit(interact, [state, txt], [state, window])
    txt.submit(lambda :"", None, txt)
            
demo.launch()