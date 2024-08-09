# faq_chatbot/faq_data.py

import json
from .config import Config
from .logger import setup_logger

logger = setup_logger()

def load_faq_data():
    try:
        with open(Config.FAQ_DATA_PATH, "r") as file:
            data = json.load(file)
        logger.info("FAQ data loaded successfully.")
        return data
    except FileNotFoundError:
        logger.error("FAQ data file not found.")
        return {}
