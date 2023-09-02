from textblob import TextBlob

def sentiment_analysis(text: str) -> float:
    blob = TextBlob(text)
    sentiment = blob.sentiment.polarity
    return sentiment

text = "Me gusta el chocolate"
#text = "I love chocolate ice cream!"
sentiment = sentiment_analysis(text)
print(sentiment)
print (sentiment_analysis("I love chocolate ice cream!"))


