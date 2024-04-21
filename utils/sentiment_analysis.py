import torch
from transformers import BertTokenizer, BertForSequenceClassification

def analyze_sentiment(reviews):

    # Join all reviews into a single string
    all_reviews = ' '.join(reviews)

    # Initialize BERT model and tokenizer
    model = BertForSequenceClassification.from_pretrained('bert-base-cased', num_labels=2)
    tokenizer = BertTokenizer.from_pretrained('bert-base-cased')
    labels = ['Negative', 'Positive']

    # Encode all reviews
    encoded_reviews = tokenizer.encode_plus(
        all_reviews,
        max_length=512,
        truncation=True,
        padding='max_length',
        return_tensors='pt'
    )

    # Pass the encoded reviews to the BERT model
    output = model(**encoded_reviews)

    # Get the predicted sentiment probabilities
    sentiment_probs = output[0].softmax(dim=-1).tolist()[0]

    # Get the predicted sentiment label
    sentiment_label = labels[sentiment_probs.index(max(sentiment_probs))]

    return sentiment_label, sentiment_probs
