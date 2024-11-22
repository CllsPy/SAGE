import streamlit as st
import PyPDF2
from main import summarize
import google.generativeai as genai
import streamlit as st
import PyPDF2
from main import summarize
import time
import streamlit as st
from PIL import Image


icon = Image.open('documents.png')

st.set_page_config(
       page_title =  'Paper Summarizer',
        page_icon=icon,
        layout='centered',
        initial_sidebar_state='auto',
)

st.title(":blue[Bem-Vindo, ]")

# sidebar
with st.sidebar:
       st.header("Objective")
       st.write(""" Este projeto utiliza a Inteligência Artificial Generativa   do Google e engenharia de prompts para gerar resumos estruturados  
       de artigos científicos carregados, simplificando os principais insights para um entendimento rápido.""")
       st.markdown("---")

       st.header("Utilização")
       st.write("""
       1. Faça UPLOAD de um artigo em formato PDF.
       2. CLIQUE em sumarizar.
       3. AGUARDE a sua resposta.
       
       """)
       

       st.markdown("---")
       st.markdown(f' made by [CLL](https://github.com/CllsPy)')
    
col1, col2 = st.columns(2)

with st.form('Gemini Paper Summarizer'):
    uploaded_file = st.file_uploader('', type='pdf')
    sub_button = st.form_submit_button('Sumarizar')
    
    if not uploaded_file:
        st.write(f'Por favor **ANEXE** um PDF')
        st.stop()

    
    if  uploaded_file: 
        with col1:
            if uploaded_file is not None:
                with st.spinner('PROCESSANDO...'): 
                       time.sleep(15)
                       pdf_reader = PyPDF2.PdfReader(uploaded_file)
                       text_content = ""
                       
                       for page in pdf_reader.pages:
                                text_content += page.extract_text()
                       
                       if text_content.strip():
                              response = summarize(text_content)
                              summarized_text = (response.text)     
                           
if sub_button:
    with st.expander('Mostrar Resposta'):
           full_response = st.markdown(summarized_text)
           full_response
           st.button("📋", on_click=on_copy_click, args=(full_response,))
