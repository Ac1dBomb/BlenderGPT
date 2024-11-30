Blender Scripting Assistant with Local GPT Model Integration
Overview
This project is a powerful Blender extension that integrates a local GPT-based language model (e.g., LLaMA, GPT-Neo) for automating Python script generation within Blender. The tool allows users to interact with Blender through a natural language interface, enabling users to easily generate Blender Python scripts for various tasks, including object manipulation, animation, and more.

The extension uses a local server to interact with the model, providing efficient, customizable, and cost-effective AI assistance for Blender scripting tasks.
*This was mainly developed for Intel Arc GPUs using LLM-IPex/llama.cpp*

Features
Key Features:
Local Model Integration:

Use of a local server (LLaMA, GPT-Neo, etc.) for model generation, ensuring data privacy and reduced cost compared to cloud-based models.
Seamless interaction with Blender to generate Python code directly for Blender tasks.
Blender UI Integration:

Gradio UI embedded within Blender, making it easy to communicate with the model and receive results instantly.
Real-time feedback and a simple interface for script generation.
Script Generation:

Automatically generate Blender Python code based on user input.
Ability to customize input prompts to generate specific code for tasks like object manipulation, animations, or procedural generation.
Advanced Error Handling and Logging:

Built-in error logging for both model communication and Blender scripting, providing clear feedback in case of issues.
Blender Integration:

Simple integration with Blender's Python API, allowing seamless interaction with the generated code directly inside the Blender environment.
Requirements
Blender: Blender 2.8 or newer is required.
Python: Python 3.7 or newer.
Local Model Server: A local server running a language model (e.g., LLaMA or GPT-Neo). The server should be capable of responding to POST requests for model generation.
Gradio: Python library for creating interactive UIs.
Requests: Python library to interact with the local model API.
Dependencies:
You can install the necessary dependencies using pip:

bash
Copy code
pip install gradio requests
Setup Instructions
1. Install Blender and Python Dependencies
Ensure you have Blender 2.8 or newer installed on your system. You will also need Python 3.7 or newer for running the extension.

Next, install the required Python dependencies. Open a terminal or command prompt and run:

bash
Copy code
pip install gradio requests
2. Set Up the Local Model API
To use the extension, you must have a local model server running. This could be any supported model, such as LLaMA or GPT-Neo. The local model server must expose an API that accepts POST requests for generating Python code.

Example server setup:

Set up the model (e.g., using Hugging Face Transformers or another framework).
Expose an API endpoint (e.g., /generate) that accepts input and returns Python code based on a prompt.
3. Clone the Repository
Clone this repository to your local machine:

bash
Copy code
git clone https://github.com/your-username/blender-scripting-assistant.git
cd blender-scripting-assistant
4. Install Blender Add-on
To install the Blender extension, follow these steps:

Open Blender.
Go to Edit > Preferences > Add-ons > Install....
Navigate to the cloned repository directory and select the __init__.py file.
Activate the add-on by checking the box next to the add-on's name in the preferences.
Usage
Gradio Interface
After installing and activating the add-on, you'll see a panel inside Blender with a Gradio interface that allows you to interact with the local GPT model. Follow these steps:

Enter a Prompt: Type in a natural language description of the Blender task you want to automate (e.g., "Create a rotating cube").
Generate Script: Press the "Generate" button. The model will process your prompt and return a Python script that you can use directly in Blender.
Apply the Script: The script will be executed inside Blender, performing the requested task.
Blender Scripting Flow
The prompt is sent to the local model server via an API call.
The model generates a Python script in response to the prompt.
The script is returned and executed inside Blender.
Available Configuration Options
Model Type: You can select which model to use (GPT-4 or GPT-3.5 Turbo).
Prompt Customization: Customize the prompt format, such as whether to include code comments, instructions, or just raw Python code.
Advanced Features
1. Caching Responses
To improve performance, responses from the model can be cached locally. This avoids making repeated requests for the same prompt, saving both time and resources.

2. Custom Model Parameters
The extension allows you to customize parameters for the GPT model (e.g., temperature, max_tokens, top_p). This allows for fine-tuning the model's creativity and response length.

3. Error Handling and Logging
Comprehensive logging has been integrated to track issues with both Blender's API and the model API. Any errors are logged for easy troubleshooting.

Troubleshooting
Common Issues
Local Model Server Not Responding: Ensure that the local model server is running and reachable at the correct endpoint (http://localhost:5000/generate).
Model Response Timeout: The model may take some time to generate a response. Adjust the timeout or ensure the model is properly optimized for speed.
Debugging
You can access detailed logs for debugging issues related to either the local model or Blender's Python API. Logs are printed to the terminal or console window.

Future Improvements
Multilingual Support: The ability to generate scripts in different languages for users from various regions.
Export to File: Option to export the generated scripts directly to files (e.g., .py, .txt, or .json).
Enhanced UI: Future iterations could include more complex interfaces for editing the generated scripts directly within Blender.
License
This project is licensed under the MIT License. See the LICENSE file for more information.

Credits
Blender: For providing the Python API and integration capabilities.
Gradio: For building the interactive UI.
Open-source Models: For providing the GPT-based models that power the script generation.
Contact
For further inquiries or feedback, please reach out to the project maintainer via email or GitHub issues.

