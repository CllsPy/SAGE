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
        initial_sidebar_state='expanded',
)


# sidebar
with st.sidebar:
        st.title("Objective")
        st.info(
                """This project uses Google Generative AI and prompt engineering to generate 
                        structured summaries of uploaded 
                        scientific articles, simplifying key insights for quick understanding.
                """)
                
        st.markdown("---")
        st.markdown(f' made by [CLL](https://github.com/CllsPy)')
    
col1, col2 = st.columns(2)

with st.form('Gemini Paper Summarizer'):
    st.header("Gemini Summarizer")
    uploaded_file = st.file_uploader('', type='pdf')
    sub_button = st.form_submit_button('Submit')
    
    if not uploaded_file:
        st.info(f'Please **Upload** a PDF file')
        st.stop()

    if  uploaded_file: 
        with col1:
            if uploaded_file is not None:
                    pdf_reader = PyPDF2.PdfReader(uploaded_file)
                    text_content = ""
                
                    for page in pdf_reader.pages:
                            text_content += page.extract_text()
                    
                    if text_content.strip():
                                response = summarize(text_content)
                                summarized_text = (response.text)     
                               
if sub_button:
       with st.expander('Show Anser"):
              st.info(summarized_text)
