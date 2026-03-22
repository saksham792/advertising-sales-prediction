print("🤖 AI Chatbot Started")
print("Type 'bye' to exit")

name = input("What is your name? ")
print("Hello", name, "! Nice to meet you.")

while True:
    user = input("You: ").lower()

    if user == "hello":
        print("Bot: Hello! How are you?")
    elif user == "how are you":
        print("Bot: I am fine and ready to help you.")
    elif user == "your name":
        print("Bot: My name is Python Bot.")
    elif user == "time":
        print("Bot: I cannot tell exact time yet, but I can learn that soon.")
    elif user == "bye":
        print("Bot: Goodbye", name, "!")
        break
    else:
        print("Bot: Sorry, I don't understand that yet.")
         