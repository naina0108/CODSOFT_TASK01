# 🤖 TASK 01: ChatBot With Rule-Based       Responses


---

## 📌 Project Overview

This project presents an AI-powered Chatbot designed to simulate intelligent and natural conversations through an interactive user interface. By leveraging Natural Language Processing (NLP) techniques and rule-based conversational logic, the chatbot is capable of understanding user queries and delivering relevant, context-aware responses. The system is built to provide a seamless conversational experience while demonstrating the practical application of Artificial Intelligence in human-computer interaction.

Beyond answering user queries, the chatbot emphasizes efficiency, accessibility, and user engagement, making it adaptable to various domains such as customer support, virtual assistance, education, and information retrieval. This project showcases how AI can enhance digital communication by automating interactions and improving the overall user experience.

---

## ✨ Features

- 💬 Real-time, interactive text-based conversation with a continuous chat loop
- 🧠 Rule-based intent recognition using keyword/substring matching
- 🔁 Handles greetings, small talk, and casual queries
- 🤖 Answers questions about the bot itself (name, creator, capabilities)
- 📚 Responds to basic tech/AI knowledge queries (Python, AI, ML, NLP)
- 😄 Includes fun/casual responses (jokes, compliments, etc.)
- 🚪 Graceful exit on bye/exit/quit/goodbye commands
- ⚡ Lightweight — no external APIs or heavy libraries required
- 🧩 Easy to extend with new rules and responses
- 📈 **24 unique query-response rules** across 5 categories

---

## 🧠 Rule-Based Logic

Unlike AI chatbots powered by machine learning, this bot relies on **explicitly defined rules**:

1. User input is captured and normalized (lowercased, cleaned).
2. The input is checked against a set of predefined **keywords/patterns**.
3. If a match is found, the bot returns a corresponding **predefined response**.
4. If no rule matches, a **default fallback response** is triggered, keeping the conversation going instead of breaking.

This mirrors the logic of early conversational systems like ELIZA — simple, transparent, and fully predictable.

```
User Input → Normalize Text → Match Against Rules → Return Mapped Response
                                     ↓ (no match)
                              Fallback Response
```

---

## 📂 Project Structure

```
📦 RuleBot
 ┣ 📜 chatbot.py        # Core chatbot logic (rules + conversation loop)
 ┗ 📜 README.md         # Project documentation
```

*Built and tested in **Google Colab** for quick prototyping and easy sharing.*

---

## ⚙️ How It Works

1. Run `chatbot.py` in Google Colab (or any Python environment).
2. The chatbot greets the user and waits for input.
3. Every message you type is compared against the bot's rule set.
4. The bot replies based on the matched rule — or a fallback if nothing matches.
5. Type an exit keyword (like `bye` or `exit`) to end the conversation.

**Example interaction:**
```
Hello!
I'm your Rule-Based Chatbot.
What's your name? Bhavan
Nice to meet you, Bhavan!
How can I help you? (type 'bye' to exit)

You: hi
Bot: Hey there! How can I assist you?

You: what is ai
Bot: AI stands for Artificial Intelligence — it enables computers to perform 
tasks that usually require human intelligence.

You: tell me a joke
Bot: Why do programmers prefer dark mode? Because light attracts bugs!

You: thanks
Bot: You're welcome! Feel free to ask another question anytime.

You: bye
Bot: Goodbye, Bhavan! Have a nice day.
```

---

## 📋 Rule Categories

The chatbot currently handles **24 query-response rules**, organized into 5 categories:

| Category | Example Queries |
|----------|------------------|
| 👋 Greetings | "hi", "what's up", "good morning", "good night" |
| 🤖 About the Bot | "who made you", "your name", "what can you do", "are you human" |
| 📚 Tech/AI Knowledge | "what is python", "what is ai", "what is machine learning", "what is nlp" |
| 😄 Fun/Casual | "joke", "sing", "love you", "weather" |
| 👋 Gratitude/Farewell | "thanks", "who are you", "bye" / "exit" / "quit" |

---

## 🛠️ Technologies Used

| Tool | Purpose |
|------|---------|
| ![Python](https://img.shields.io/badge/-Python-3776AB?logo=python&logoColor=white) | Core programming language |
| ![Colab](https://img.shields.io/badge/-Google%20Colab-F9AB00?logo=googlecolab&logoColor=white) | Development & execution environment |
| `re` / string methods | Pattern matching for rule detection |

---

## 🚀 Future Improvements

- [ ] Refactor rule storage into a dictionary for easier scalability
- [ ] Add NLP-based intent detection (e.g., NLTK / spaCy) for smarter matching
- [ ] Build a web interface using **Flask** or **Streamlit**
- [ ] Expand the rule set with more topics and conversational depth
- [ ] Add memory/context so the bot remembers earlier parts of the conversation
- [ ] Deploy as a live demo for easy public access

---

