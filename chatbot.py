def chatbot():
    print("Hi there! I am a simple shopping chatbot. Type 'bye' to exit.")
    
    # Define a dictionary for responses
    responses = {
        ("hi", "hello", "hey"): "Hello there! How can I assist you today?",
        ("bye",): "Goodbye! Have a great day!",
        ("i need",): "What kind of item do you need?",
        ("what products do you have?",): "We have laptops, smartphones, and headphones. What are you interested in?",
        ("can you recommend",): "Sure! What kind of recommendation are you looking for?",
        ("i am",): "Hello! How are you feeling today?",
        ("feeling",): "Good to hear that!",
        
    }
    
    # Process user input
    while True:
        user_input = input("> ").strip().lower()
        
        # Find a response
        response = next(
            (reply for keywords, reply in responses.items() if any(keyword in user_input for keyword in keywords)),
            "I'm sorry, I didn't understand that. Can you rephrase?"
        )
        
        print(response)
        if user_input == "bye":
            break

if __name__ == "__main__":
    chatbot()
