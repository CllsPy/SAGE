import google.generativeai as genai
from prompt import sum
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

def summarize(file):
  response = model.generate_content([sum, file])
  return response

def main():
    summrize(file)
    
if __name__ == "__main__":
    main()
