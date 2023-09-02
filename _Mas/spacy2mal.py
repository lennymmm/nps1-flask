import spacy

nlp = spacy.load("en_core_web_lg")

def sentiment_analysis(text: str) -> float:
    doc = nlp(text)
    sentiment = 0
    count = 0
    for token in doc:
        print(token.text, token.has_vector, token.vector_norm, token.sentiment)
        if token.has_vector and token.vector_norm > 0:
            sentiment += token.sentiment
            count += 1
    if count > 0:
        sentiment /= count
    print ("sent:", sentiment," count:",count)
    return sentiment

text = "I love chocolate ice cream!"
sentiment = sentiment_analysis(text)
print(sentiment)