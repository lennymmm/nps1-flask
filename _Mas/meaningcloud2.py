from meaningcloud import SentimentResponse
from meaningcloud import SentimentRequest

def analyze_sentiment(text):
    key = "832d3dcf3e93f5064d6a836877ab129f"  # Reemplaza con tu clave de API de MeaningCloud
    lang = "es"  # Indica que el texto está en español

    sentiment_request = SentimentRequest(
        key=key,
        lang=lang,
        txt=text
    )

    sentiment_response = sentiment_request.sendReq()

    return sentiment_response

# Ejemplo de uso
text = "Me encanta este lugar, la comida es deliciosa y el servicio es excelente."
result = analyze_sentiment(text)

print(result.getResults())
