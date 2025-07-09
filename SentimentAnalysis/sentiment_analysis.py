from transformers import pipeline
import nltk
from nltk.corpus import words

# Initialize pipeline
try:
    sentiment_pipeline = pipeline("sentiment-analysis")
except Exception as e:
    sentiment_pipeline = None
    pipeline_error = str(e)

# Load English vocabulary from NLTK
english_vocab = set(words.words())

def is_valid_text(text):
    """Basic check to see if text contains recognizable English words"""
    if not text or not isinstance(text, str):
        return False
    tokens = text.lower().split()
    valid_words = [word for word in tokens if word in english_vocab]
    return len(valid_words) >= max(1, len(tokens) // 2)  # At least 50% real words

def sentiment_analyzer(text_to_analyse):
    if not is_valid_text(text_to_analyse):
        return {
            'status': 400,
            'error': 'Invalid text: does not contain recognizable English words.'
        }

    if sentiment_pipeline is None:
        return {
            'status': 503,
            'error': 'Service Unavailable: Sentiment model failed to load.',
            'details': pipeline_error
        }

    try:
        result = sentiment_pipeline(text_to_analyse)[0]
        label = result.get('label', 'unknown')
        score = result.get('score', None)

        return {
            'status': 200,
            'label': label,
            'score': score
        }
    except Exception as e:
        return {
            'status': 500,
            'error': 'Internal Server Error: Sentiment analysis failed.',
            'details': str(e)
        }