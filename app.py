import subprocess
import ollama

def main():
    print("Welcome to the Command Assistant! I'm here to help you with your MacOS tasks. Let's get started.")
    print("Please type your task, and I'll suggest a MacOS command for it.")
    
    user_input = input("What would you like to do today (e.g. 'list all files in a directory')?")
    prompt = ("You are a command outputter, your output will only contain valid MacOS commands and nothing more, "
              "so that they can be copy-pasted as is. Give me the command to " + user_input)
    
    response = ollama.chat(model='llama3', messages=[{'role': 'user', 'content': prompt}])
    cmd = response['message']['content']
    
    print("\nSuggested command: " + cmd)
    confirmation = input("Do you want to run this command? (y/n): ")
    
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