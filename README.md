Welcome to NeuroNest, a tool designed to make learning easier for students with special needs. This guide will walk you through setting up the tool on your computer. For the best experience, we recommend using Google Chrome or Safari browsers.
Prerequisites

Before you begin, ensure you have the following installed:

    Python (3.8 or later)
    Visual Studio Code (or any other code editor)

Step 1: Install Python

Download and install Python from Python's official website. Follow the instructions based on your operating system.
Step 2: Install Visual Studio Code

Download and install Visual Studio Code from here. This is the editor where you will write and run your code.
Setup Instructions
Step 1: Clone the GitHub Repository

    Open Visual Studio Code.
    Open the terminal in Visual Studio Code (View > Terminal).
    Type the following command and press Enter:

    git clone https://github.com/mdzaidcodes/neuronest.git

Step 2: Install Required Libraries

    In the Visual Studio Code terminal, navigate to the project directory:

cd neuronest

Install all required Python libraries by running:

    pip install -r requirements.txt

Step 3: Download and Set Up the AI Model

    Download the Ollama Lamma 3.2 model from the provided link (add your specific download link here).
    Place the downloaded model in a directory inside your project (e.g., /models).

Step 4: Run the Flask Application

    In the terminal, ensure you are in the project directory.
    Start the Flask server by running:

    python app.py

    Make sure your file is named app.py; if not, replace app.py with your Flask application's filename.

Step 5: Access the Application in Your Browser

    Open Google Chrome or Safari.
    In the address bar, type localhost:5000 and press Enter.

You should now see the NeuroNest running locally on your browser!
Troubleshooting

If you encounter any issues, make sure all commands were typed correctly and that you are in the correct directory. Check your internet connection if downloads are failing.
Conclusion

Congratulations! You have successfully set up and run your NeuroNest tool. If you have any questions or need further assistance, please feel free to ask for help.
