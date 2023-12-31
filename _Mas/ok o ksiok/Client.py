#! /usr/bin/env python

# Created by MeaningCloud Support Team
# Date: 26/02/18

import sys
import meaningcloud

# @param model str - Name of the model to use. Example: "IAB_en" by default = "IPTC_en"
model = 'IAB_en'

# @param license_key - Your license key (found in the subscription section in https://www.meaningcloud.com/developer/)
license_key = '832d3dcf3e93f5064d6a836877ab129f'

# @param text - Text to use for different API calls
text = 'London is a very nice city but I also love Madrid.'


try:
    # We are going to make a request to the Topics Extraction API
    topics_response = meaningcloud.TopicsResponse(meaningcloud.TopicsRequest(license_key, txt=text, lang='en',
                                                                             topicType='e').sendReq())

    # If there are no errors in the request, we print the output
    if topics_response.isSuccessful():
        print("\nThe request to 'Topics Extraction' finished successfully!\n")

        entities = topics_response.getEntities()
        if entities:
            print("\tEntities detected (" + str(len(entities)) + "):\n")
            for entity in entities:
                print("\t\t" + topics_response.getTopicForm(entity) + ' --> ' +
                      topics_response.getTypeLastNode(topics_response.getOntoType(entity)) + "\n")

        else:
            print("\tNo entities detected!\n")
    else:
        if topics_response.getResponse() is None:
            print("\nOh no! The request sent did not return a Json\n")
        else:
            print("\nOh no! There was the following error: " + topics_response.getStatusMsg() + "\n")

    # CLASS API CALL
    # class_response = meaningcloud.ClassResponse(
    #   meaningcloud.ClassRequest(license_key, txt=text, model=model).sendReq())

    # SENTIMENT API CALL
    sentiment_response = meaningcloud.SentimentResponse(
       meaningcloud.SentimentRequest(license_key, lang='en', txt=text, txtf='plain').sendReq())

    # GENERIC API CALL
    # generic = meaningcloud.Request(url="url_of_specific_API",key=key)
    # generic.addParam('parameter','value')
    # generic_result = generic.sendRequest()
    # generic_response = meaningcloud.Response(generic_result)

    # We are going to make a request to the Language Identification API
    lang_response = meaningcloud.LanguageResponse(meaningcloud.LanguageRequest(license_key, txt=text).sendReq())

    # If there are no errors in the request, we will use the language detected to make a request to Sentiment and Topics
    if lang_response.isSuccessful():
        print("\nThe request to 'Language Identification' finished successfully!\n")
        first_lang = lang_response.getFirstLanguage()
        if first_lang:
            language = lang_response.getLanguageCode(first_lang)
            print("\tLanguage detected: " + lang_response.getLanguageName(first_lang) + ' (' + language + ")\n")
        else:
            print("\tNo language detected!\n")

    # We are going to make a request to the Lemmatization, PoS and Parsing API
    parser_response = meaningcloud.ParserResponse(
        meaningcloud.ParserRequest(license_key, txt=text, lang='en').sendReq())

    # If there are no errors in the request, print tokenization and lemmatization
    if parser_response.isSuccessful():
        print("\nThe request to 'Lemmatization, PoS and Parsing' finished successfully!\n")
        lemmatization = parser_response.getLemmatization(True)
        print("\tLemmatization and PoS Tagging:\n")
        for token, analyses in lemmatization.items():
            print("\t\tToken -->", token)
            for analysis in analyses:
                print("\t\t\tLemma -->", analysis['lemma'])
                print("\t\t\tPoS Tag -->", analysis['pos'], "\n")
    print("sentim:", sentiment_response.getGlobalScoreTag )

except ValueError:
    e = sys.exc_info()[0]
    print("\nException: " + str(e))