# tests/test_chatbot.py

import unittest
from faq_chatbot.chatbot import FAQChatbot
from faq_chatbot.exceptions import NoMatchFound

class TestFAQChatbot(unittest.TestCase):
    
    def setUp(self):
        self.chatbot = FAQChatbot()

    def test_faq_found(self):
        response = self.chatbot.get_response("What is your return policy?")
        self.assertIn("return", response.lower())

    def test_no_faq_found(self):
        with self.assertRaises(NoMatchFound):
            self.chatbot.get_response("This is a very random question.")
            
if __name__ == "__main__":
    unittest.main()
