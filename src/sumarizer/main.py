# main.py
import google.generativeai as genai
from utils.prompt import sum
import os

def initialize_model(api_key):
    """Inicializa o modelo Gemini com a chave de API fornecida"""
    genai.configure(api_key=api_key)
    return genai.GenerativeModel("gemini-1.5-flash")

def summarize(file, model):
    """Gera o resumo do texto usando o modelo fornecido"""
    response = model.generate_content([sum, file])
    return response

def main(api_key):
    model = initialize_model(api_key)
    return model