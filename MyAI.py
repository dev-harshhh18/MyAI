import openai
import os
from dotenv import load_dotenv
from cryptography.fernet import Fernet
import time

# Load the environment variables and OpenAI API key
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

# Function to generate a valid Fernet encryption key
def generate_fernet_key():
    key = Fernet.generate_key()
    print(f"New Fernet Key: {key.decode()}")  # Print the new key for your .env file
    return key

# Use the key from .env or generate a new one if it doesn't exist
encryption_key = os.getenv("ENCRYPTION_KEY")
if not encryption_key:
    encryption_key = generate_fernet_key().decode()  # Generate a new key if not found in .env

cipher_suite = Fernet(encryption_key.encode())  # Initialize cipher suite with the key

# Prompt function
def generate_response(user_input):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # Use appropriate model
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": user_input}
            ]
        )
        return response['choices'][0]['message']['content']

    except openai.error.RateLimitError as e:
        return "Error: Rate limit exceeded. Please try again later."
    except Exception as e:
        return f"An error occurred: {str(e)}"


# Save conversation securely
def save_conversation(text):
    encrypted_text = cipher_suite.encrypt(text.encode())
    with open("conversations.log", "ab") as file:
        file.write(encrypted_text + b"\n")

# Retrieve conversation (with keyword access)
def retrieve_conversations(secret_keyword):
    if secret_keyword != "Dream":  # Replace with your chosen keyword
        return "Invalid keyword. Access denied."
    try:
        with open("conversations.log", "rb") as file:
            lines = file.readlines()
            decrypted_conversations = [cipher_suite.decrypt(line).decode() for line in lines]
        return "\n".join(decrypted_conversations)
    except Exception as e:
        return f"An error occurred: {e}"

# Main loop to talk to AI
if __name__ == "__main__":
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            break
        elif user_input.lower().startswith("retrieve"):
            keyword = user_input.split(" ")[1]
            print("Conversations:", retrieve_conversations(keyword))
        else:
            response = generate_response(user_input)
            print("AI:", response)
            save_conversation(user_input + " -> " + response)
