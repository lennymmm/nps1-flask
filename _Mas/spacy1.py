import spacy
from spacy.tokens import Doc

nlp = spacy.load("en_core_web_sm")
#nlp = spacy.load("es_core_news_sm")

def sentiment_analysis(text: str) -> int:
    doc = nlp(text)
    sentiment = 0
    for token in doc:
        if token.has_vector and token.vector_norm > 0:
            sentiment += token.sentiment
    return sentiment

text = "I love chocolate ice cream!"
#text = "El malgusto es lo peor que tiene este servicio y no me gusta nada" 
# "Yo amo el helado de chocolate y amo la vida y el cielo azul!"
sentiment = sentiment_analysis(text)
print(sentiment)  # Output: 0.4