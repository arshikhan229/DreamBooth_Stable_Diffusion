import os

def login_to_huggingface(token):
    os.makedirs(os.path.expanduser("~/.huggingface"), exist_ok=True)
    with open(os.path.expanduser("~/.huggingface/token"), 'w') as f:
        f.write(token)
