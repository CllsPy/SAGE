# main.py
import google.generativeai as genai
from prompt import get_summary_prompt
import os

def initialize_model(api_key):
    """Inicializa o modelo Gemini com a chave de API fornecida"""
    genai.configure(api_key=api_key)
    return genai.GenerativeModel("gemini-2.5-flash")

def summarize(file, model):
    """Gera o resumo do texto usando o modelo fornecido"""
    response = model.generate_content([get_summary_prompt(), file])
    return response

def main(api_key):
    model = initialize_model(api_key)
    return model