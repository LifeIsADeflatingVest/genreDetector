from textblob import TextBlob
import random
from training_data import training_data

# combine genre classification and sentiment analysis
def classify_text(f):
    text = f
    texts = [s.strip() for s in text.split('.') if s.strip()]
    genre_probabilities = {"science fiction": 0, "fantasy": 0, "crime fiction": 0, "romance": 0, "supernatural horror": 0, "literary": 0}
    sentiments = []
    for text in texts:
        blob = TextBlob(text)
        sentiment = blob.sentiment.polarity
        sentiments.append(sentiment)
        for words, genre_label in training_data:
            if any(word in blob.words for word in words):
                genre_probabilities[genre_label] += 1
    if sum(genre_probabilities.values()) > 0:
        genre = max(genre_probabilities, key=genre_probabilities.get)
    else:
        genre = None
    sentiment = sum(sentiments) / len(sentiments)
    if sentiment > 0.2:
        sentiment = "positive"
    elif sentiment < -0.2:
        sentiment = "negative"
    else:
        sentiment = "neutral"
    return genre, sentiment



