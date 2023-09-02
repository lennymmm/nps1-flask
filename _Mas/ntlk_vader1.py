import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

# Descarga el léxico de VADER
nltk.download('vader_lexicon')

sia = SentimentIntensityAnalyzer()

# Ejemplo de texto
# text = "Me encanta este producto. Es fantástico."
text = "Es muy malo este servicio. No me subscribiré."

# Analiza el sentimiento con VADER
sentiment = sia.polarity_scores(text)

print(sentiment)