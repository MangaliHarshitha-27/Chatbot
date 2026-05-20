
def chatbot_response(user_input):
    user_input = user_input.lower()

    if user_input == "hello":
        return "Hi! How can I assist you today?"
    
    elif user_input == "how are you":
        return "I'm just a chatbot, but I'm doing great!"
    
    elif user_input == "what is your name":
        return "I am CodeAlpha Chatbot."
    
    elif user_input == "help":
        return "You can ask me basic questions like hello, how are you, or type 'bye' to exit."
    
    elif user_input == "bye":
        return "Goodbye! Have a great day!"
    
    else:
        return "Sorry, I don't understand that. Try typing 'help'."

print("🤖 Welcome to Basic Chatbot!")
print("Type 'bye' to exit.\n")

while True:
    user_input = input("You: ")
    response = chatbot_response(user_input)
    print("Bot:", response)

    if user_input.lower() == "bye":
        break