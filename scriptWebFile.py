from textblob.classifiers import NaiveBayesClassifier
import pickle
import os
from training_data import training_data

# combine genre classification and sentiment analysis
def classify_text(f):
    sentences = f

    # Set the path to the classifier file
    classifier_file = 'classifier.pkl'

    # Check if the classifier file exists
    if os.path.isfile(classifier_file):
        # Load the classifier from the file
        with open(classifier_file, 'rb') as f:
            classifier = pickle.load(f)
    else:
        classifier = NaiveBayesClassifier(training_data)
        with open(classifier_file, 'wb') as f:
            pickle.dump(classifier, f)
    
    # Get the predicted label for each sentence and calculate the average
    total_scores = [0, 0, 0]
    for sentence in sentences:
        probs = classifier.prob_classify(sentence)
        total_scores[0] += probs.prob('fantasy')
        total_scores[1] += probs.prob('horror')
        total_scores[2] += probs.prob('science fiction')

    avg_scores = [score / len(sentences) for score in total_scores]
    
    # Get the top two genres with the highest scores, sorted by score
    top_genres = sorted(range(len(avg_scores)), key=lambda i: avg_scores[i], reverse=True)[:2]

    # Create a nested array with the top two genres and scores, sorted by score
    top_scores = [[None] * 2 for _ in range(2)]
    for i, genre_index in enumerate(top_genres):
        if genre_index == 0:
            top_scores[i][0] = 'Fantasy'
        elif genre_index == 1:
            top_scores[i][0] = 'Horror'
        elif genre_index == 2:
            top_scores[i][0] = 'Science fiction'
        top_scores[i][1] = avg_scores[genre_index]
    top_scores.sort(key=lambda x: x[1], reverse=True)

    return top_scores



