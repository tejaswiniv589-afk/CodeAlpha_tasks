"""
Basic Chatbot
CodeAlpha Python Programming Internship - Task 4

A simple rule-based chatbot that responds to a fixed set of user inputs
like greetings, small talk, and farewells using if-elif matching.
"""

import random


def get_response(user_input):
    """
    Given the user's message (already lowercased), return an
    appropriate rule-based reply. Returns None if the input
    should end the conversation.
    """
    text = user_input.lower().strip()

    # Farewell - ends the chat loop
    if text in ("bye", "goodbye", "exit", "quit"):
        return None

    # Greetings
    if text in ("hello", "hi", "hey", "hii", "hlo"):
        return random.choice(["Hi!", "Hello there!", "Hey! How can I help you?"])

    # Wellbeing check
    elif "how are you" in text:
        return "I'm fine, thanks! How about you?"

    elif text in ("i am fine", "i'm fine", "good", "i am good", "im good"):
        return "Glad to hear that!"

    # Identity questions
    elif "your name" in text:
        return "I'm a simple chatbot built for the CodeAlpha internship!"

    elif "who made you" in text or "who created you" in text:
        return "I was built as part of a CodeAlpha Python internship project."

    # Small talk
    elif "what can you do" in text or "help" in text:
        return "I can chat about basic things like greetings and how you're doing. Try saying 'hello' or 'bye'!"

    elif "thank" in text:
        return "You're welcome!"

    elif "time" in text:
        return "Sorry, I can't check the time yet - I'm just a simple rule-based bot!"

    elif "weather" in text:
        return "I don't have access to live weather data, but I hope it's nice outside!"

    # Fallback for anything unrecognized
    else:
        return "Sorry, I didn't understand that. Could you rephrase?"


def chat():
    print("=" * 45)
    print("Simple Chatbot (type 'bye' to exit)")
    print("=" * 45)
    print("Bot: Hi! I'm your simple chatbot. Say hello to get started.")

    while True:
        user_input = input("You: ")

        response = get_response(user_input)

        if response is None:
            print("Bot: Goodbye!")
            break

        print(f"Bot: {response}")


if __name__ == "__main__":
    chat()