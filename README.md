BlenderGPT - Local LLM with Intel GPUs


BlenderGPT is an extension for Blender that allows you to control the software using natural language commands. It integrates large language models (LLMs) like GPT-4 directly into Blender’s interface, converting simple English commands into Python scripts that can be executed within Blender. This updated version uses a local model running on Intel GPUs through oneAPI and LLM-IPEX, coupled with llama.cpp, FastAPI, and Gradio UI for a high-performance and efficient Blender control solution.

Overview
This project is a custom port of the original BlenderGPT to work with locally hosted language models powered by Intel hardware and optimizations. Instead of relying on OpenAI’s cloud-based GPT models, this setup allows you to run the model on your local machine using Intel OneAPI for GPU acceleration, LLM-IPEX (Intel Extension for PyTorch), and llama.cpp for model inference. The FastAPI server handles communication between Blender and the LLM, while Gradio provides a user-friendly UI.

Features
Local Model Deployment: Run large language models locally on Intel GPUs using oneAPI and LLM-IPEX optimizations for improved performance.
Blender Control via Natural Language: Generate Python scripts for Blender using simple English commands.
FastAPI & Gradio UI: A lightweight and fast API server built with FastAPI to manage interactions with the LLM, and Gradio for the user interface.
Intel Optimizations: Leverage Intel’s oneAPI and LLM-IPEX for better performance, especially on Intel CPUs and GPUs.
Installation
System Requirements
Blender 3.4 or later
Intel GPU (for optimal performance using oneAPI and LLM-IPEX)
Python 3.8+ (for running the server)
FastAPI (for serving the local model API)
Gradio (for the interactive UI)
Steps to Install
Clone the repository:

Run the following command to clone this repository:

bash
Copy code
git clone https://github.com/Ac1dBomb/BlenderGPT.git
Set up your Python environment:

Create and activate a Python virtual environment (optional but recommended):

bash
Copy code
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
Install dependencies:

Install the required Python packages from the requirements.txt file:

bash
Copy code
pip install -r requirements.txt
Configure Intel GPU:

Ensure your system has the Intel OneAPI toolkit installed and configured for Intel GPU acceleration.
You can install the Intel Extension for PyTorch (LLM-IPEX) by following this guide.
Install Blender Add-on:

Open Blender and navigate to Edit > Preferences > Add-ons > Install.
Select the downloaded ZIP file or folder of the cloned repository and install it.
Enable the BlenderGPT add-on by checking the checkbox next to it in the Add-ons tab.
Configure the server:

The local model server needs to be running. Navigate to the directory where server.py is located and start the FastAPI server:

bash
Copy code
uvicorn server:app --reload
This will start the FastAPI server on http://127.0.0.1:8000, and it will be accessible to Blender.

Usage
Running the Add-on
In Blender:

Once the add-on is installed and enabled, open the 3D View and press N to open the sidebar.
Locate the BlenderGPT tab on the sidebar.
Type a natural language command (e.g., "create a cube at the origin") in the input field.
Click the Execute button to generate and execute the corresponding Blender Python code.
Interactive User Interface:

The Gradio UI allows you to interact with the model through the browser. Once the FastAPI server is running, you can also open http://127.0.0.1:7860 in your web browser to interact with the model directly.
How It Works
Blender Command:
The user provides a natural language command through the Blender interface (in the sidebar or Gradio UI).
Server Request:
The BlenderGPT add-on sends a request to the FastAPI server running locally, which is connected to the language model hosted by llama.cpp.
Model Inference:
The FastAPI server sends the request to the local LLM model (using llama.cpp and LLM-IPEX for Intel optimizations) to generate the corresponding Python script for Blender.
Execute Code:
The generated Python code is returned to Blender and executed, performing the desired action.
Requirements
Blender 3.4 or later
Intel GPU with oneAPI and LLM-IPEX optimizations
Python 3.8+
PyTorch and Intel Extension for PyTorch (LLM-IPEX)
llama.cpp Python bindings for LLM inference
FastAPI and Gradio for the local model server and UI
Dependencies
blender (bpy)
requests (for HTTP requests)
gradio (for building the user interface)
fastapi (for running the local server)
uvicorn (ASGI server for FastAPI)
numpy (for numerical operations)
intel-extension-for-pytorch (for Intel GPU acceleration)
llama-cpp-python (for llama.cpp model integration)
loguru (for logging)
h5py (for model manipulation, if necessary)
For a complete list of dependencies, see the requirements.txt file.

Troubleshooting
BlenderGPT not executing commands: Ensure that the FastAPI server is running and accessible at http://127.0.0.1:8000. Check the console for any server-related errors.
Intel GPU not detected: Make sure that Intel OneAPI and LLM-IPEX are correctly installed and configured. You can test this by running any basic PyTorch code on your GPU to verify it is being utilized.
Slow performance: If performance is suboptimal, ensure that your Intel GPU drivers and oneAPI tools are up-to-date. Consider reducing the model size for faster inference if necessary.
Demonstration
You can see a demo of how this works by viewing the video below:



License
This project is licensed under the MIT License - see the LICENSE file for details.