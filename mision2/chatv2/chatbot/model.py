import os # trabaja con el sistema operativo
import pickle # guarda y carga objetos de python en archivos
from sklearn.feature_extraction.tex import countVectorizar
# counVectorizar convierte texto en un vector
from sklearn.naive_bayes import MultinomialNB
MODEL_DIR = "models"
MODEL_PATH = os.path.join(MODEL_DIR, "chatbot_model.pkl")
VECTORIZER_PATH = os.path.join(MODEL_DIR, "vectorizer.pkl")
ANSWERS_PATH = os.path.join(MODEL_DIR, "answers.pkl")