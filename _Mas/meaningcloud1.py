from meaningcloud import SentimentAnalysisClient

client = SentimentAnalysisClient('832d3dcf3e93f5064d6a836877ab129f')
response = client.sentiment(text='This is a positive sentence.')
sentiment = response['score_tag']
print(sentiment)
