
"""Text preprocessing pipeline for hate speech classification."""

import re
import nltk
import spacy

nltk.download('stopwords', quiet=True)
from nltk.corpus import stopwords

nlp = spacy.load('en_core_web_sm')
STOP = set(stopwords.words('english'))


def clean_text(text: str) -> str:
    """Remove noise from raw text."""
    text = str(text)
    text = re.sub(r'https?://\S+|www\.\S+', ' ', text)
    text = re.sub(r'@\w+', ' ', text)
    text = re.sub(r'<[^>]+>', ' ', text)
    text = re.sub(r'(.)\1{2,}', r'\1\1', text)
    text = re.sub(r'[^a-zA-Z\s]', ' ', text)
    text = re.sub(r'\s+', ' ', text)
    text = text.lower().strip()
    return text


def lemmatize_text(text: str) -> str:
    """Lemmatize text using SpaCy and remove stopwords with NLTK."""
    doc = nlp(text)
    tokens = [
        token.lemma_
        for token in doc
        if token.lemma_ not in STOP
        and not token.is_space
        and len(token.lemma_) > 2
    ]
    return ' '.join(tokens)


def preprocess(text: str) -> str:
    """Full preprocessing pipeline: clean + lemmatize."""
    return lemmatize_text(clean_text(text))
