import gradio as gr
import torch
from transformers import StableDiffusionPipeline

def inference(pipe, prompt, negative_prompt, num_samples, height, width, num_inference_steps, guidance_scale):
    with torch.autocast("cuda"), torch.inference_mode():
        return pipe(prompt, height=int(height), width=int(width), negative_prompt=negative_prompt, num_images_per_prompt=int(num_samples), num_inference_steps=int(num_inference_steps), guidance_scale=guidance_scale).images

def launch_interface(pipe):
    with gr.Blocks() as demo:
        with gr.Row():
            with gr.Column():
                prompt = gr.Textbox(label="Prompt", value="photo of zwx dog in a bucket")
                negative_prompt = gr.Textbox(label="Negative Prompt", value="")
                run = gr.Button(value="Generate")
                with gr.Row():
                    num_samples = gr.Number(label="Number of Samples", value=4)
                    guidance_scale = gr.Number(label="Guidance Scale", value=7.5)
                with gr.Row():
                    height = gr.Number(label="Height", value=512)
                    width = gr.Number(label="Width", value=512)
                num_inference_steps = gr.Slider(label="Steps", value=24)
            with gr.Column():
                gallery = gr.Gallery()
    
        run.click(inference, inputs=[prompt, negative_prompt, num_samples, height, width, num_inference_steps, guidance_scale], outputs=gallery)
    
    demo.launch(debug=True)
