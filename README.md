# NeuroNest: AI-Powered Learning for Everyone

**Welcome to NeuroNest!** This project uses AI to make learning easier, especially for students with special needs. This README will guide you through setting up and running the NeuroNest project.

**Project Repository:** [https://github.com/mdzaidcodes/neuronest](https://github.com/mdzaidcodes/neuronest)

## What You'll Need:

Before we start, here's a list of things you'll need to have:

1.  **A Computer:** You'll need a computer (Windows, macOS, or Linux) to run this project.
2.  **Internet Connection:** You'll need an internet connection to download necessary software and the AI model.
3.  **Basic Computer Skills:** You should be comfortable with using a computer, opening files, and typing.

## Step-by-Step Setup Guide:

### 1. Install Essential Software:

   *   **Visual Studio Code (VS Code):**
      *   This is where you'll view and edit the code.
      *   Go to: [https://code.visualstudio.com/](https://code.visualstudio.com/) and download the correct version for your computer.
      *   Follow the instructions to install VS Code.
   *   **Python:**
      *   NeuroNest uses Python, a popular programming language.
      *   Go to: [https://www.python.org/downloads/](https://www.python.org/downloads/) and download the latest version of Python 3.
      *   Follow the instructions to install Python. During installation, make sure to check the box that says "Add Python to PATH".
   *  **Ollama:**
      * Ollama is what runs our AI model.
      *  Go to: [https://ollama.com/](https://ollama.com/) and download the correct version for your computer.
      * Follow the instructions to install Ollama.

### 2. Clone the Project (Get the Code):

   *   **Open VS Code:** Start Visual Studio Code.
   *   **Open Terminal:** Click on "Terminal" -> "New Terminal" at the top of VS Code.
   *   **Type this command and press Enter:**
      ```bash
      git clone https://github.com/mdzaidcodes/neuronest.git
      ```
      This will copy the NeuroNest project to your computer into a folder called "neuronest".
   *   **Navigate to the project folder:**
      ```bash
      cd neuronest
      ```

### 3. Install Python Libraries (Requirements):

   *   **In the terminal inside VS Code (while you are inside the neuronest folder), type this and press Enter:**
      ```bash
      pip install -r requirements.txt
      ```
      This command installs all the necessary Python libraries required for the project.

### 4. Download the Llama 3.2 AI Model:

   *   **Open Terminal (if it's not already open) and type this command then press Enter:**
      ```bash
      ollama run llama3
      ```
     Ollama will download the llama 3.2 model to your computer. This might take some time, depending on your internet speed.
     When prompted, you can type something like "Hi" just to test it out. After that, you can close ollama and keep running it from your terminal and just keep it open in background

### 5. Running the NeuroNest Application

   *   **Make sure Ollama is running in the background**
   * **In the terminal inside VS Code, type this and press Enter:**

      ```bash
      python app.py
      ```
    This starts the NeuroNest server.
   *  You will see in your terminal output some thing that indicates that the server started running on something called a host and port. It will most likely look like "Running on http://127.0.0.1:5000".
    * Open either **Google Chrome or Safari**
    * Type this address into the address bar of your web browser: `http://127.0.0.1:5000`
   *  That will open the NeuroNest application page.
   *   You can start using the application now.
   *   **Keep the Terminal window with python app.py running**. If you close it, the application will stop working.

### Done!

You've successfully set up and run NeuroNest! If you encounter any problems, please check the troubleshooting section.

## Troubleshooting

*   **`pip` command not found:** If you get a message that `pip` is not found, make sure you selected the option "Add Python to PATH" when installing Python. You can uninstall and re-install Python, and make sure this option is selected. Also make sure that Python is installed correctly
*   **Ollama not working:** If Ollama does not start or has any problem running, make sure Ollama is installed correctly.
*   **Application not running:** Make sure that you keep the terminal with python app.py running in the background. If you close it, the application will stop working

*   If you are having problem after following all the instructions you can contact the project owner mdzaidcodes in github.

