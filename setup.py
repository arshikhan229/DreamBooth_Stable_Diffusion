import os

def setup_environment():
    os.system('pip install -qq git+https://github.com/ShivamShrirao/diffusers')
    os.system('pip install -q -U --pre triton')
    os.system('pip install -q accelerate transformers ftfy bitsandbytes==0.35.0 gradio natsort safetensors xformers')
    os.system('wget -q https://github.com/ShivamShrirao/diffusers/raw/main/examples/dreambooth/train_dreambooth.py')
    os.system('wget -q https://github.com/ShivamShrirao/diffusers/raw/main/scripts/convert_diffusers_to_original_stable_diffusion.py')
