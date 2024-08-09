# faq_chatbot/config.py

import os

class Config:
    FAQ_DATA_PATH = os.getenv("FAQ_DATA_PATH", "faq_data.json")
