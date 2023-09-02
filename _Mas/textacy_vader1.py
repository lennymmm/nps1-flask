import spacy
from textacy.vader import SentimentIntensityAnalyzer
#from textacy.vader import SentimentIntensityAnalyzer

# Carga el modelo en español
nlp = spacy.load("es_core_news_sm")

# Ejemplo de texto
text = "Me encanta este producto. Es fantástico."

# Procesa el texto con Spacy
doc = nlp(text)

# Analiza el sentimiento con VADER (a través de textacy)
sia = SentimentIntensityAnalyzer()
sentiment = sia.get_doc_sentiment(doc)

print(sentiment)
