import streamlit as st
import PyPDF2
from main import summarize
import google.generativeai as genai
import streamlit as st
import PyPDF2
from main import summarize
import time
import streamlit as st

col1, col2 = st.columns(2)

with st.form('Gemini Paper Summarizer'):
    st.header("Gemini Summarizer")
    uploaded_file = st.file_uploader('', type='pdf')
    sub_button = st.form_submit_button('Submit')
    
    if not uploaded_file:
        st.info('Please Upload a PDF first')
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
     st.write(summarized_text)


