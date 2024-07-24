# DreamBooth Stable Diffusion Fine-Tuning

This project aims to fine-tune the Stable Diffusion model using the DreamBooth method. It includes environment setup, HuggingFace login, configuration, training, and inference using Gradio.

## Project Structure

The project is divided into several modules for better organization and maintainability:

- `setup.py`: Handles environment setup and installation of dependencies.
- `login.py`: Manages HuggingFace login.
- `config.py`: Defines configuration settings.
- `data_loader.py`: Loads images and masks for training.
- `train.py`: Fine-tunes the Stable Diffusion model.
- `inference.py`: Generates images using the fine-tuned model.
- `main.py`: Orchestrates the workflow of the entire project.

## Installation

1. Clone the repository:
    ```sh
    git clone <repository-url>
    cd dreambooth_stable_diffusion
    ```

2. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

3. Set up HuggingFace API credentials:
    ```sh
    mkdir ~/.huggingface
    echo -n "YOUR_HUGGINGFACE_TOKEN" > ~/.huggingface/token
    ```

## Usage

1. Run the `main.py` script to execute the entire workflow:
    ```sh
    python main.py
    ```

## License

This project is licensed under the MIT License.
