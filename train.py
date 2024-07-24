import os

def train_model(model_name, output_dir, instance_prompt, class_prompt, num_class_images, max_train_steps, save_interval):
    os.system(f'accelerate launch train_dreambooth.py --pretrained_model_name_or_path={model_name} --instance_data_dir={output_dir}/instance_images --class_data_dir={output_dir}/class_images --output_dir={output_dir} --instance_prompt="{instance_prompt}" --class_prompt="{class_prompt}" --num_class_images={num_class_images} --max_train_steps={max_train_steps} --save_interval={save_interval}')
