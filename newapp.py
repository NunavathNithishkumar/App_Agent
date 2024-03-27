import os
import platform
from transformers import pipeline

# Define the NLP pipeline for text generation
nlp = pipeline("text-generation", model="EleutherAI/gpt-neo-2.7B")

# Database of chunks and their corresponding actions
chunk_database = {
    "open_notepad": "Open Notepad",
    "open_chrome": "Open Chrome",
    "open_file_explorer": "Open File Explorer",
    "open_visual_studio_code": "Open Visual Studio Code",
    "open_cmd": "Open Command Prompt",
    "open_powershell": "Open PowerShell",
    "open_taskmgr": "Open Task Manager",
    "open_calc": "Open Calculator",
    "open_paint": "Open Paint",
    "open_wordpad": "Open WordPad",
    "open_excel": "Open Excel",
    "open_powerpoint": "Open PowerPoint",
    "open_outlook": "Open Outlook",
    "close_notepad": "Close Notepad",
    "close_chrome": "Close Chrome",
    "close_file_explorer": "Close File Explorer",
    "close_visual_studio_code": "Close Visual Studio Code",
    "close_cmd": "Close Command Prompt",
    "close_powershell": "Close PowerShell",
    "close_taskmgr": "Close Task Manager",
    "close_calc": "Close Calculator",
    "close_paint": "Close Paint",
    "close_wordpad": "Close WordPad",
    "close_excel": "Close Excel",
    "close_powerpoint": "Close PowerPoint",
    "close_outlook": "Close Outlook"
}

# Function to process the user input using NLP and execute the corresponding action
def process_and_execute_command(user_input):
    # Generate text using NLP pipeline
    generated_text = nlp(user_input, max_length=50, do_sample=True)[0]['generated_text'].strip()
    
    # Check if the generated text matches any chunk in the database
    for chunk_key, chunk_action in chunk_database.items():
        if chunk_key in generated_text:
            execute_action(chunk_action)
            return
    
    print("Sorry, I couldn't understand your command.")

# Function to execute the action corresponding to the chunk
def execute_action(action):
    if "Open" in action:
        app_name = action.split("Open ")[1]
        result = open_app(app_name)
        print(result)
    elif "Close" in action:
        app_name = action.split("Close ")[1]
        result = close_app(app_name)
        print(result)

# Platform-specific function to open an app
def open_app(app_name):
    try:
        os.system(f"start {app_name}.exe")
        return f"{app_name} opened successfully."
    except Exception as e:
        return f"Error opening {app_name}: {e}"

# Platform-specific function to close an app
def close_app(app_name):
    try:
        os.system(f"taskkill /F /IM {app_name}.exe")
        return f"{app_name} closed successfully."
    except Exception as e:
        return f"Error closing {app_name}: {e}"

# Function to list available apps
def list_available_apps():
    apps = [key.split("_")[1].capitalize() for key in chunk_database.keys()]
    return ", ".join(apps)

# Example usage
while True:
    user_input = input("Enter a command: ")
    if user_input.lower() == "exit":
        print("Exiting...")
        break
    elif user_input.lower() == "list apps":
        print("Available apps:", list_available_apps())
    else:
        process_and_execute_command(user_input)
