from setup import setup_environment
from login import login_to_huggingface
from config import MODEL_NAME, OUTPUT_DIR, IMAGE_PATH, INSTANCE_PROMPT, CLASS_PROMPT, NUM_CLASS_IMAGES, MAX_TRAIN_STEPS, SAVE_INTERVAL
from data_loader import load_images
from train import train_model
from inference import launch_interface
from transformers import StableDiffusionPipeline

def main():
    setup_environment()
    login_to_huggingface("YOUR_HUGGINGFACE_TOKEN")
    load_images(IMAGE_PATH, OUTPUT_DIR)
    train_model(MODEL_NAME, OUTPUT_DIR, INSTANCE_PROMPT, CLASS_PROMPT, NUM_CLASS_IMAGES, MAX_TRAIN_STEPS, SAVE_INTERVAL)

    pipe = StableDiffusionPipeline.from_pretrained(OUTPUT_DIR).to("cuda")
    launch_interface(pipe)

if __name__ == '__main__':
    main()
