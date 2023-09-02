from meaningcloud import SentimentAnalysis

# Configura tu clave de API de MeaningCloud
API_KEY = '832d3dcf3e93f5064d6a836877ab129f'

def analyze_sentiment(text):
    sentiment_analyzer = SentimentAnalysis(API_KEY)
    response = sentiment_analyzer.sentiment(text)
    
    if response['status']['code'] == '0':
        sentiment = response['score_tag']
        agreement = response['agreement']
        subjectivity = response['subjectivity']
        
        print("Sentimiento: ", sentiment)
        print("Acuerdo: ", agreement)
        print("Subjetividad: ", subjectivity)
    else:
        print("Error en la solicitud:", response['status']['msg'])

# Ejemplo de texto para analizar
texto = "Me encanta este producto, es increíblemente útil y fácil de usar."

# Llama a la función analyze_sentiment con el texto
analyze_sentiment(texto)