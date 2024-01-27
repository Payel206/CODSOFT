import nltk
import random

# Download the punkt tokenizer for nltk
nltk.download('punkt')

# List of responses for the chatbot
responses = {
    "hello": ["Hi there!", "Hello!", "Hey!"],
    "how are you": ["I'm doing well, thank you!", "Not too bad!", "I'm fine, thanks for asking."],
    "bye": ["Goodbye!", "See you later!", "Bye!"],
    "What is Age" : ["My age is 30"],
    "What's the weather like today?" "Tell me about the weather" : ["I'm sorry, I don't have real-time weather information."]
}



# Function to generate a response
def generate_response(user_input):
    # Tokenize the user input
    words = nltk.word_tokenize(user_input.lower())

    # Check if any key phrase is present in the user input
    for key in responses:
        if any(word in words for word in key.split()):
            return random.choice(responses[key])

    # If no key phrase is found, generate a generic response
    return "I'm not sure what you're asking. Can you try again?"


# Main loop for the chatbot
while True:
    user_input = input("You: ")
    if user_input.lower() == 'exit':
        print("Chatbot: Goodbye!")
        break
    response = generate_response(user_input)
    print("Chatbot:", response)
