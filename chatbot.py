# faq_chatbot/chatbot.py

from .faq_data.py import load_faq_data
from .nlp_utils import preprocess_text, calculate_similarity
from .exceptions import NoMatchFound
from .logger import setup_logger

logger = setup_logger()

class FAQChatbot:
    def __init__(self):
        self.faq_data = load_faq_data()

    def get_response(self, user_query):
        if not self.faq_data:
            logger.error("No FAQ data available.")
            raise NoMatchFound("Sorry, I couldn't find any relevant answers.")

        user_query_processed = preprocess_text(user_query)
        best_match = None
        best_similarity = 0.0

        for faq in self.faq_data.get("faqs", []):
            question_processed = preprocess_text(faq["question"])
            similarity = calculate_similarity(user_query_processed, question_processed)
            if similarity > best_similarity:
                best_similarity = similarity
                best_match = faq

        if best_match and best_similarity > 0.75:  # A threshold for similarity
            logger.info(f"Found a match with similarity: {best_similarity}")
            return best_match["answer"]
        else:
            logger.warning("No good match found.")
            raise NoMatchFound("Sorry, I couldn't find any relevant answers.")
