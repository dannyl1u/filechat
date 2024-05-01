import subprocess
import ollama
from ollama import AsyncClient
import asyncio
import threading
import time

# Find more animations frames here
# https://github.com/sindresorhus/cli-spinners/blob/main/spinners.json
loading_animation_frames = [
    "-",
    "\\",
    "|",
    "/"
]

def loading(stop_loading_thread):
    i = 0

    while not stop_loading_thread.is_set():
        for char in '|/-\\':
            print('thinking ' + loading_animation_frames[i % len(loading_animation_frames)], end="\r")
            time.sleep(.125)
            i += 1
    
    # Clear the loading animation
    print('\033[K', end="\r")

async def send_prompt(prompt):
    response = await AsyncClient().chat(model='llama3', messages=[{'role': 'user', 'content': prompt}])
    return response['message']['content']

def main():
    print("Welcome to the Command Assistant! I'm here to help you with your MacOS tasks. Let's get started.")
    print("Please type your task, and I'll suggest a MacOS command for it.")
    
    user_input = input("What would you like to do today (e.g. 'list all files in a directory')?\n> ")
    prompt = ("You are a command outputter, your output will only contain valid MacOS commands and nothing more, "
              "so that they can be copy-pasted as is. Do not give any additional notes or text. Give me the command to " + user_input)
    
    # Create an event to signal the loading animation thread to stop
    stop_loading_thread = threading.Event()
    # Start loading animation
    loading_thread = threading.Thread(target=loading, args=(stop_loading_thread,))
    loading_thread.start()

    response = asyncio.run(send_prompt(prompt))

    # Stop loading animation
    stop_loading_thread.set()
    loading_thread.join()

    cmd = response
    
    print("\nSuggested command: " + cmd)
    confirmation = input("Do you want to run this command? (y/n): \n")
    
    if confirmation.lower() == 'y':
        try:
            subprocess.run(cmd, shell=True, check=True)
            print("Command executed successfully.")
        except subprocess.CalledProcessError:
            print("Command failed to execute.")
        except Exception as e:
            print(f"An error occurred: {e}")
    else:
        print("Command execution cancelled.")

if __name__ == "__main__":
    ollama.pull('llama3')
    main()