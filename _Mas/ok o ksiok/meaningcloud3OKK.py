import requests

def analyze_sentiment(text):
    url = "https://api.meaningcloud.com/sentiment-2.1"
    key = "832d3dcf3e93f5064d6a836877ab129f"  # Reemplaza con tu clave de API de MeaningCloud
    lang = "es"  # Indica que el texto está en español

    payload = {
        "key": key,
        "lang": lang,
        "txt": text
    }

    response = requests.post(url, data=payload)
    sentiment_data = response.json()
    polarity = sentiment_data["score_tag"]

    return polarity # sentiment_data

# Ejemplo de uso
#text = "Me encanta este lugar, la comida es deliciosa y el servicio es excelente."
text = "El servicio es muy malo. No lo recomiendo."

rr = analyze_sentiment(text)

print(rr)

text2 = "El lugar esta aceptable"
rrr = analyze_sentiment(text2)
print(rrr)
text = "Buen servicio y atención al cliente"
rr = analyze_sentiment(text)
print(rr)

text = "Excelente experiencia, altamente recomendado"
rr = analyze_sentiment(text)
print(rr)

