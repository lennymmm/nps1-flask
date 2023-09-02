from transformers import BertTokenizer, BertForSequenceClassification
from torch.nn.functional import softmax
import torch

def daSent(text):
    # Carga el modelo y el tokenizador
    MODEL_NAME = 'nlptown/bert-base-multilingual-uncased-sentiment'
    model = BertForSequenceClassification.from_pretrained(MODEL_NAME)
    tokenizer = BertTokenizer.from_pretrained(MODEL_NAME)

    inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True, max_length=512)
    with torch.no_grad():
        outputs = model(**inputs)
        
    # Aplica softmax a las salidas para obtener probabilidades
    probs = softmax(outputs.logits, dim=1)  # BERT regresa logits

    # Decodifica la predicción
    rating0 = torch.argmax(probs) + 1  # El modelo específico que estamos usando predice un valor entre 1 y 5
    return f"{rating0}"

print(daSent( "Me encanta este producto. Es fantástico."))
print(daSent( "Tiene el leopardo su abrigo en un monte seco y pardo"))
print(daSent( "Esta muy fea y sucia la oficina. Es desagradable"))
