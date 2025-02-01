from flask import Flask, render_template, request, jsonify
import ollama
import os
import re # Import 're' module for regular expressions
from flask_cors import CORS


app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "http://localhost:3000"}})

# Global variable to track if the model is loaded
model_name = "llama3.2"  # Using Llama 3 model


# Function to check if the model is pulled
def is_model_pulled(model_name):
    try:
        models = ollama.list()
        return any(model["name"] == model_name for model in models["models"])
    except Exception as e:
        print(f"Error checking for model {model_name}: {e}")
        return False

# Pull the model on startup if it's not already pulled
if not is_model_pulled(model_name):
    print(f"Pulling {model_name}...")
    try:
        ollama.pull(model_name)
        print(f"{model_name} pulled successfully!")
    except Exception as e:
        print(f"Error pulling {model_name}: {e}")
        exit(1) # Exit if model pulling fails.
else:
    print(f"{model_name} is already pulled.")


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/chat', methods=['POST'])
def chat():
    try:
        user_message = request.json['message']
        response = ollama.chat(model=model_name, messages=[
            {
                'role': 'system',
                'content': """You are an educational chatbot designed to help users learn about a variety of topics. Your responses should be clear, concise, and informative. When answering questions:

                    *   Provide brief and factual explanations.
                    *   Use simple language suitable for a general audience.
                    *   Avoid unnecessary jargon or overly technical terms.
                    *   If possible, relate information to real-world examples.
                    *   Keep responses to 1-3 sentences.
                    *   Do not provide opinions.
                    *   Be neutral in your tone.
                    *   If you don't know the answer, say "I'm sorry, I don't have information on that."

                Your goal is to make learning accessible and engaging."""
            },
            {
                'role': 'user',
                'content': user_message,
            }
        ])
        bot_response = response['message']['content'].strip()
          # Remove any newlines or carriage return and replace with spaces
        bot_response = re.sub(r'[\r\n]+', ' ', bot_response).strip()
        return jsonify({'response': bot_response})

    except Exception as e:
        print(e)
        return jsonify({'error': 'Error processing request'}), 500


if __name__ == '__main__':
    app.run(debug=True, port=5000)