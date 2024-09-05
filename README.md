# Concurrent Image Generation with Multiple GPUs

ConGen is capible of concurrently running multiple image generation models in parallel by leveraging multiple GPUs. 

# Summary



ConGen scales image generation by running an instance of a specified model on each GPU, continuously monitoring their status. As soon as an image is generated, ConGen efficiently scales the workload by assigning a new prompt to the next available GPU for processing.
ConGen takes advantage of programmatically setting the "CUDA_VISIBLE_DEVICES" environment variable to control which GPU is used for each task. The "ConcurrentGeneration.py" script acts as the queuing system, managing image generation prompts and monitoring GPU availability. The moment a GPU finishes generating an image, "ConcurrentGeneration.py" triggers a new instance of the "ImageGenerationOOP.py" script, limiting it to the specific GPU that is free.

# Dependencies:
- NVIDIA GPU with CUDA installed and configured.
- Compatible CUDA version (12.1 or newer).

# Installation
It is highly recommended that you use a virtual environment:

   `git clone https://github.com/KevinZWong/ConGen.git`
   
   `cd ConGen`
   
   `pip install -r requirements.txt`

# Running the Sample
Replace the list image_descriptions in main.py with a list of image prompts:
`python3 main.py`
Results of concurrently generated images will appear in the outputs folder.

# Short Comings
ConGen will only work if the selected model fits on each and every one of your GPUs. If only a portion of your GPUs has enough VRAM to support your specified image model, please specify which GPUs to use by exporting the CUDA_VISIBLE_DEVICES environment variable.
