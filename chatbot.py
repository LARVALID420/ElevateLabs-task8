"""
Rule-Based Chatbot
Task 8: Python Developer Internship
A simple chatbot using if-elif-else and input/output loops.
"""

def get_response(user_input):
    """Return a response based on user input using rule-based matching."""
    user_input = user_input.lower().strip()

    # Greetings
    if user_input in ["hi", "hello", "hey", "howdy", "hiya"]:
        return "Hello! 👋 How can I help you today?"

    elif user_input in ["how are you", "how are you?", "how r u", "how's it going"]:
        return "I'm doing great, thanks for asking! 😊 What can I do for you?"

    # Name / Identity
    elif "your name" in user_input or "who are you" in user_input:
        return "I'm ChatBot 🤖 — your friendly rule-based assistant!"

    elif "what are you" in user_input or "are you a bot" in user_input or "are you human" in user_input:
        return "I'm a rule-based chatbot built with Python! No ML magic here — just good ol' if-elif-else. 😄"

    # Time / Date
    elif "time" in user_input:
        from datetime import datetime
        return f"The current time is: {datetime.now().strftime('%H:%M:%S')} ⏰"

    elif "date" in user_input or "today" in user_input:
        from datetime import datetime
        return f"Today's date is: {datetime.now().strftime('%B %d, %Y')} 📅"

    # Weather (static response — rule-based can't fetch real data)
    elif "weather" in user_input:
        return "I can't check live weather, but I hope it's sunny where you are! ☀️"

    # Help
    elif "help" in user_input or "what can you do" in user_input:
        return (
            "I can respond to:\n"
            "  • Greetings (hi, hello, hey)\n"
            "  • Questions about myself\n"
            "  • Time & Date queries\n"
            "  • Jokes 😂\n"
            "  • Basic math (e.g. '2 + 2')\n"
            "  • Motivational quotes\n"
            "  • Farewells\n"
            "Just type and I'll do my best!"
        )

    # Jokes
    elif "joke" in user_input or "funny" in user_input or "make me laugh" in user_input:
        import random
        jokes = [
            "Why do programmers prefer dark mode? Because light attracts bugs! 🐛",
            "Why did the developer go broke? Because he used up all his cache! 💸",
            "How many programmers does it take to change a lightbulb? None — that's a hardware problem. 💡",
            "I told my computer I needed a break. Now it won't stop sending me Kit-Kat ads. 🍫",
        ]
        return random.choice(jokes)

    # Motivation
    elif "motivat" in user_input or "quote" in user_input or "inspire" in user_input:
        import random
        quotes = [
            "\"Code is like humor. When you have to explain it, it's bad.\" – Cory House",
            "\"First, solve the problem. Then, write the code.\" – John Johnson",
            "\"The best error message is the one that never shows up.\" – Thomas Fuchs",
            "\"Simplicity is the soul of efficiency.\" – Austin Freeman",
        ]
        return random.choice(quotes)

    # Basic Math
    elif any(op in user_input for op in ["+", "-", "*", "/", "plus", "minus", "times", "divided"]):
        # Replace word operators
        expr = (user_input
                .replace("plus", "+")
                .replace("minus", "-")
                .replace("times", "*")
                .replace("divided by", "/"))
        # Extract and evaluate math expression safely
        import re
        match = re.search(r"[\d\s\+\-\*\/\.]+", expr)
        if match:
            try:
                result = eval(match.group().strip())  # safe for simple arithmetic
                return f"The answer is: {result} 🧮"
            except Exception:
                return "Hmm, I couldn't calculate that. Try something like '5 + 3'."
        return "I didn't catch that math problem. Try: '10 * 4'"

    # Farewell
    elif user_input in ["bye", "goodbye", "quit", "exit", "see you", "cya", "later"]:
        return "FAREWELL"  # signal to exit

    # Thanks
    elif "thank" in user_input or "thanks" in user_input or "thx" in user_input:
        return "You're welcome! Happy to help. 😊"

    # Default / Unknown
    else:
        return (
            "Hmm, I'm not sure how to respond to that. 🤔\n"
            "Type 'help' to see what I can do!"
        )


def main():
    print("=" * 50)
    print("       Welcome to ChatBot 🤖")
    print("  Type 'bye' or 'exit' to quit.")
    print("=" * 50)
    print()

    while True:
        try:
            user_input = input("You: ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nChatBot: Goodbye! Take care 👋")
            break

        if not user_input:
            print("ChatBot: Please say something! 😊\n")
            continue

        response = get_response(user_input)

        if response == "FAREWELL":
            print("ChatBot: Goodbye! It was nice chatting with you. 👋")
            break

        print(f"ChatBot: {response}\n")


if __name__ == "__main__":
    main()
