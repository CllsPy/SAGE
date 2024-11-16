import google.generativeai as genai

import os
from dotenv import load_dotenv

# Carregando as variáveis de ambiente do arquivo .env
load_dotenv()
# Acessando a variável de ambiente API_KEY
api_key = os.getenv("API_KEY")
# Verificando se a API_KEY foi carregada com sucesso
if api_key:
    print("Chave de API carregada com sucesso:", api_key)
else:
    print("Chave de API não encontrada no arquivo .env.")

genai.configure(api_key=api_key)
model = genai.GenerativeModel("gemini-1.5-flash")
sample_pdf = genai.upload_file('2402.07927v1.pdf')

def summarize(sample_pdf):
  response = model.generate_content(["Sumarize este pdf, responda em português-brasil", sample_pdf])
    
  return response

def main():
    summrize(sample_pdf)
    
if __name__ == "__main__":
    main()
