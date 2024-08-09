# main.py

import argparse
from faq_chatbot.chatbot import FAQChatbot
from faq_chatbot.exceptions import NoMatchFound

def main():
    parser = argparse.ArgumentParser(description="FAQ Chatbot")
    parser.add_argument("query", type=str, help="Your question")
    args = parser.parse_args()

    chatbot = FAQChatbot()

    try:
        response = chatbot.get_response(args.query)
        print(f"Chatbot: {response}")
    except NoMatchFound as e:
        print(f"Chatbot: {e}")

if __name__ == "__main__":
    main()
