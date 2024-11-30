import bpy
import requests
import logging
import re
import gradio as gr

# Set up logging
logging.basicConfig(level=logging.INFO)

def get_model_response(prompt, model_type, chat_history, system_prompt, model_params=None):
    try:
        model_params = model_params or {"temperature": 0.7, "top_p": 0.9, "max_tokens": 1500}
        
        if model_type == "local":
            # Replace with the URL of your local model API
            url = "http://localhost:5000/generate"
            payload = {
                "model": "llama",  # Example model name, replace with your specific model
                "prompt": prompt,
                "chat_history": chat_history,
                "system_prompt": system_prompt,
                **model_params
            }
            response = requests.post(url, json=payload)
            response.raise_for_status()
            return response.json().get("text", "No response from model")
        
        elif model_type == "openai":
            # OpenAI API call logic (if required in the future)
            response = openai.ChatCompletion.create(
                model="gpt-4",
                messages=generate_message_history(chat_history, system_prompt, prompt),
                max_tokens=model_params.get("max_tokens", 1500)
            )
            return response.choices[0].message['content']
    
    except requests.exceptions.RequestException as e:
        logging.error(f"Request failed: {e}")
        return "Error: Request to model failed"
    except Exception as e:
        logging.error(f"Unexpected error: {e}")
        return "Error: Unexpected issue occurred"

def generate_message_history(chat_history, system_prompt, prompt):
    messages = [{"role": "system", "content": system_prompt}]
    for message in chat_history[-10:]:
        if message["type"] == "assistant":
            messages.append({"role": "assistant", "content": "```\n" + message["content"] + "\n```"})
        else:
            messages.append({"role": message["type"].lower(), "content": message["content"]})

    messages.append({"role": "user", "content": "Can you please write Blender code for me that accomplishes the following task: " + prompt + "? \n. Do not respond with anything that is not Python code. Do not provide explanations"})
    return messages

def gradio_interface(prompt, state):
    chat_history = state or []
    response = get_model_response(prompt, "local", chat_history, system_prompt="You are a helpful Blender scripting assistant.")
    chat_history.append({"role": "user", "content": prompt})
    chat_history.append({"role": "assistant", "content": response})
    return response, chat_history

# Gradio interface setup
gr.Interface(fn=gradio_interface, inputs=["text", "state"], outputs=["text", "state"]).launch()

def init_props():
    bpy.types.Scene.gpt4_chat_history = bpy.props.CollectionProperty(type=bpy.types.PropertyGroup)
    bpy.types.Scene.gpt4_model = bpy.props.EnumProperty(
        name="GPT Model",
        description="Select the GPT model to use",
        items=[
            ("gpt-4", "GPT-4 (powerful, expensive)", "Use GPT-4"),
            ("gpt-3.5-turbo", "GPT-3.5 Turbo (less powerful, cheaper)", "Use GPT-3.5 Turbo"),
        ],
        default="gpt-4",
    )
    bpy.types.Scene.gpt4_chat_input = bpy.props.StringProperty(
        name="Message",
        description="Enter your message",
        default="",
    )
    bpy.types.Scene.gpt4_button_pressed = bpy.props.BoolProperty(default=False)
    bpy.types.PropertyGroup.type = bpy.props.StringProperty()
    bpy.types.PropertyGroup.content = bpy.props.StringProperty()

def clear_props():
    del bpy.types.Scene.gpt4_chat_history
    del bpy.types.Scene.gpt4_chat_input
    del bpy.types.Scene.gpt4_button_pressed

def split_area_to_text_editor(context):
    area = context.area
    for region in area.regions:
        if region.type == 'WINDOW':
            override = {'area': area, 'region': region}
            bpy.ops.screen.area_split(override, direction='VERTICAL', factor=0.5)
            break

    new_area = context.screen.areas[-1]
    new_area.type = 'TEXT_EDITOR'
    return new_area
