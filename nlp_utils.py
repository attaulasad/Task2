# faq_chatbot/nlp_utils.py

import spacy

# Load the SpaCy model (use a small model for performance)
nlp = spacy.load("en_core_web_sm")

def preprocess_text(text):
    """Preprocess the text by converting to lowercase and removing stopwords."""
    doc = nlp(text.lower())
    return " ".join([token.lemma_ for token in doc if not token.is_stop and not token.is_punct])

def calculate_similarity(text1, text2):
    """Calculate similarity between two texts using SpaCy's similarity method."""
    doc1 = nlp(text1)
    doc2 = nlp(text2)
    return doc1.similarity(doc2)
