# Necesita bajar mas de 700 MB de recursos
# Ahora en (base) Conda ... parece y no en pyenv
from codeswitch.codeswitch import SentimentAnalysis
sa = SentimentAnalysis('spa-eng')
result = sa.analyze("El servicio es pésimo")
print(result)
sentence = "El perro le ladraba a La Gatita .. .. lol #teamlagatita en las playas de Key Biscayne este Memorial day"
result = sa.analyze(sentence)
print(result)
