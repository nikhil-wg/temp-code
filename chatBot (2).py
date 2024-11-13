# simple_chatbot.py

# Define responses based on keywords
responses = {
    "hello": "Hello! How can I assist you today?",
    "hi": "Hi there! How can I help?",
    "how are you": "I'm just a bot, but I'm here to help!",
    "bye": "Goodbye! Have a nice day!",
    "help": "Sure, I'm here to help! What do you need assistance with?"
}

# Default response for unknown inputs
default_response = "I'm sorry, I don't understand that. Could you please rephrase?"

# Function to get a response
def get_response(user_input):
    # Normalize the user input to lowercase
    user_input = user_input.lower()
    
    # Check if the user input matches any known keywords
    for keyword, response in responses.items():
        if keyword in user_input:
            return response
    
    # If no keyword is matched, return the default response
    return default_response

# Main function to run the chatbot
def chat():
    print("Chatbot: Hello! I am a simple chatbot. Type 'bye' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "bye":
            print("Chatbot:", responses["bye"])
            break
        response = get_response(user_input)
        print("Chatbot:", response)

# Run the chatbot
if __name__ == "__main__":
    chat()
