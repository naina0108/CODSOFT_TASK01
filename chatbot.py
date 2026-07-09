print("Hello!")
print("I'm your Rule-Based Chatbot.")

name = input("What's your name? ")
print("Nice to meet you, " + name + "!")
print("How can I help you? (type 'bye' to exit)\n")

while True:
    user_input = input("You: ").lower().strip()


# Greetings
    if any(word in user_input for word in ["hi", "hello", "hey"]):
        print("Bot: Hey there! How can I assist you?")

    elif "how are you" in user_input:
        print("Bot: I'm great, thanks for asking! How about you?")

    elif "what's up" in user_input or "whats up" in user_input or "wassup" in user_input:
        print("Bot: Not much, just waiting to chat with you!")

    elif "good morning" in user_input:
        print("Bot: Good morning! Hope you have a great day ahead.")

    elif "good night" in user_input:
        print("Bot: Good night! Sleep well.")


# About the bot
    elif "who are you" in user_input:
        print("Bot: I'm ChatBot — a simple chatbot that follows predefined rules to chat with you.")

    elif "who made you" in user_input or "who created you" in user_input or "who built you" in user_input:
        print("Bot: I was created using Python by my developer.")

    elif "your name" in user_input:
        print("Bot: I'm ChatBot, your friendly rule-based assistant!")

    elif "what can you do" in user_input or "help" in user_input:
        print("Bot: I can chat casually and answer a few predefined questions —you can ask me about Python, AI,or other questions!")

    elif "are you real" in user_input or "are you human" in user_input or "are you a robot" in user_input:
        print("Bot: I'm a chatbot — no feelings, just code and rules!")

    elif "how old are you" in user_input or "your age" in user_input:
        print("Bot: I don't have an age — I was just written into existence!")

    elif "do you sleep" in user_input:
        print("Bot: Nope, I'm always awake and ready to chat.")

    elif "favorite color" in user_input or "favourite colour" in user_input:
        print("Bot: I'd say... binary black and white. Classic.")


# Tech / AI knowledge
    elif "what is python" in user_input:
        print("Bot: Python is a popular programming language used for Web Development, AI, Data Science, and Automation.")

    elif "what is ai" in user_input or "what is artificial intelligence" in user_input:
        print("Bot: AI stands for Artificial Intelligence — it enables computers to perform tasks that usually require human intelligence.")

    elif "what is machine learning" in user_input or "what is ml" in user_input:
        print("Bot: Machine Learning is a branch of AI where systems learn patterns from data instead of being explicitly programmed.")

    elif "what is nlp" in user_input:
        print("Bot: NLP stands for Natural Language Processing — it helps computers understand and generate human language.")

    elif "what is a chatbot" in user_input:
        print("Bot: A chatbot is a program designed to simulate conversation with users, either through rules or AI models.")

    elif "codsoft" in user_input:
        print("Bot: CodSoft is the organization offering this Artificial Intelligence internship!")


# Fun / casual
    elif "joke" in user_input:
        print("Bot: Why do programmers prefer dark mode? Because light attracts bugs!")

    elif "sing" in user_input:
        print("Bot: I'd sing, but my voice is just text. Imagine a great melody here!")

    elif "love you" in user_input:
        print("Bot: Aww, that's sweet! I appreciate you too.")

    elif "weather" in user_input:
        print("Bot: I can't check live weather yet, but I hope it's nice where you are!")

    elif "time" in user_input:
        print("Bot: I can't check the time yet. ")


# Gratitude / farewell
    elif "thank" in user_input:
        print("Bot: You're welcome! Feel free to ask another question anytime.")

    elif user_input in ["bye", "exit", "quit", "goodbye"]:
        print(f"Bot: Goodbye, {name}! Have a nice day.")
        break

    else:
        print("Bot: Sorry, I don't understand that. Could you try rephrasing?")
