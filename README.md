# Task 8 – Rule-Based Chatbot 

A simple **rule-based chatbot** built with Python using `if-elif-else` control flow and input/output loops.

##  Objective
Build a chatbot that responds to user input using pattern matching — no machine learning required.

## Features
- Greetings & farewells
- Identity questions ("Who are you?")
- Real-time **date & time** retrieval
- **Random jokes** and motivational quotes
- Basic **arithmetic** (e.g., `5 + 3`, `10 * 4`)
- Graceful exit on `bye` / `exit` / `quit`
- Fallback response for unknown inputs

## 🛠 Tools
- **Language**: Python 3
- **Libraries**: Built-in only (`datetime`, `random`, `re`)

##  How to Run

```bash
python chatbot.py
```

### Example Conversation
```
You: hello
ChatBot: Hello! 👋 How can I help you today?

You: tell me a joke
ChatBot: Why do programmers prefer dark mode? Because light attracts bugs! 🐛

You: what time is it
ChatBot: The current time is: 14:32:10 ⏰

You: 15 * 6
ChatBot: The answer is: 90 🧮

You: bye
ChatBot: Goodbye! It was nice chatting with you. 👋
```

##  Key Concepts
- **Control Flow** – if-elif-else chains for intent matching
- **Loops** – `while True` loop with exit condition
- **Input Handling** – `input()` with `.lower().strip()` normalization
- **String Matching** – `in` operator and exact comparisons

##  Limitations of Rule-Based Bots
- Can't understand **context** or multi-turn conversations
- Fails on **typos** or unexpected phrasing
- Requires manually writing every rule
- Doesn't **learn** from interactions

##  How This Could Evolve into an ML Bot
- Use **NLP libraries** (NLTK, spaCy) for tokenization
- Train an **intent classifier** (e.g., with scikit-learn or TensorFlow)
- Add **entity extraction** for dynamic responses
- Use **transformer models** (e.g., BERT, GPT) for open-domain conversation
