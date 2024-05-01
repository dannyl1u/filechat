# filechat

> "The hottest new programming language is English" - Andrej Karpathy

no more memorizing unix command cheatsheets... filechat is all you need  
filechat lets you talk to your computing with plain english 🗣️  

e.g. telling the computer in english `update permissions so that owners can have read/write access to photos` is a lot easier to remember than `find / -name "*.jpg" -type f -exec chmod 644 {} \;`

https://github.com/dannyl1u/filechat/assets/45186464/8883bbd7-db71-4805-a2fb-5597e71f9880

video is played back at 1x speed, running locally on a m1 pro macbook with **no external connections (no gpt key needed!)**

uses [llama3 w/ ollama](https://ollama.com/library/llama3) 🦙

## Getting Started

### Download and Install

1. **Download the latest release**:
   - Navigate to the [Releases](https://github.com/dannyl1u/filechat/releases) page and download the latest `filechat.zip` file.

2. **Unzip the File**:
   - Unzip the downloaded file to extract the `filechat` executable.

### Adding `filechat` to Your PATH

To run `filechat` from anywhere on your terminal, you need to add it to your PATH. Follow these instructions based on your operating system:

#### For macOS and Linux:

1. **Move the Executable**:
   - Move the `filechat` executable to a directory that's in your PATH, such as `/usr/local/bin` or `~/bin`. If you choose `~/bin`, make sure it exists, or create it using:
     ```bash
     mkdir -p ~/bin
     ```

   - Move the executable:
     ```bash
     mv filechat ~/bin/
     ```

2. **Add `~/bin` to Your PATH** (if not already included):
   - Open your terminal and add the following line to your shell configuration file (`~/.bashrc`, `~/.zshrc`, etc.):
     ```bash
     export PATH="$HOME/bin:$PATH"
     ```
   - Reload your shell configuration:
     ```bash
     source ~/.bashrc  # Or replace .bashrc with your specific config file
     ```

### Running

Open a new terminal and type:

```bash
filechat
``
🎉

## how to setup locally (the old way) 😴

`git clone https://github.com/dannyl1u/filechat.git`

`cd filechat`

`pip install -r requirements.txt`

`python app.py`

### but if you have filechat... 😎

https://github.com/dannyl1u/filechat/assets/45186464/002796f2-082a-4831-bbc8-3b8b61918900
