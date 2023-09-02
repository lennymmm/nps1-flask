import meaningcloud

license_key = '832d3dcf3e93f5064d6a836877ab129f'
language = 'en'
txt = 'This is a positive sentence.'

sentiment_response = meaningcloud.SentimentResponse(meaningcloud.SentimentRequest(license_key, lang=language, txt=txt).sendReq())
sentiment = sentiment_response.getScoreTag()
print(sentiment)
