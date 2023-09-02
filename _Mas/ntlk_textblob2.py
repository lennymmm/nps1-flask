from textblob import TextBlob

texto = "Este es un texto en español."

blob = TextBlob(texto)
sentimiento = blob.sentiment

print(sentimiento.polarity)  # Polaridad del sentimiento (-1 a 1)
print(sentimiento.subjectivity)  # Subjetividad del sentimiento (0 a 1)
print(sentimiento)