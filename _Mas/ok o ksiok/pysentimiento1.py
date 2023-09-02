from pysentimiento import create_analyzer
analyzer = create_analyzer(task="sentiment", lang="es")

analyzer.predict("Qué gran jugador es Messi")
# returns AnalyzerOutput(output=POS, probas={POS: 0.998, NEG: 0.002, NEU: 0.000})
analyzer.predict("Esto es pésimo")
# returns AnalyzerOutput(output=NEG, probas={NEG: 0.999, POS: 0.001, NEU: 0.000})
analyzer.predict("Qué es esto?")
# returns AnalyzerOutput(output=NEU, probas={NEU: 0.993, NEG: 0.005, POS: 0.002})

analyzer.predict("jejeje no te creo mucho")
# AnalyzerOutput(output=NEG, probas={NEG: 0.587, NEU: 0.408, POS: 0.005})
"""
Emotion Analysis in English
"""

emotion_analyzer = create_analyzer(task="emotion", lang="en")

emotion_analyzer.predict("yayyy")
# returns AnalyzerOutput(output=joy, probas={joy: 0.723, others: 0.198, surprise: 0.038, disgust: 0.011, sadness: 0.011, fear: 0.010, anger: 0.009})
emotion_analyzer.predict("fuck off")
# returns AnalyzerOutput(output=anger, probas={anger: 0.798, surprise: 0.055, fear: 0.040, disgust: 0.036, joy: 0.028, others: 0.023, sadness: 0.019})

"""
Hate Speech (misogyny & racism)
"""
hate_speech_analyzer = create_analyzer(task="hate_speech", lang="es")

hate_speech_analyzer.predict("Esto es una mierda pero no es odio")
# returns AnalyzerOutput(output=[], probas={hateful: 0.022, targeted: 0.009, aggressive: 0.018})
hate_speech_analyzer.predict("Esto es odio porque los inmigrantes deben ser aniquilados")
# returns AnalyzerOutput(output=['hateful'], probas={hateful: 0.835, targeted: 0.008, aggressive: 0.476})

hate_speech_analyzer.predict("Vaya guarra barata y de poca monta es XXXX!")
# returns AnalyzerOutput(output=['hateful', 'targeted', 'aggressive'], probas={hateful: 0.987, targeted: 0.978, aggressive: 0.969})
