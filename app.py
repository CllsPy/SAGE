import streamlit as st
import PyPDF2
from main import summarize
import google.generativeai as genai

# Upload the PDF
uploaded_file = st.file_uploader('', type='pdf')

if uploaded_file is not None:
    try:
        # Read PDF content
        pdf_reader = PyPDF2.PdfReader(uploaded_file)
        text_content = ""
        for page in pdf_reader.pages:
            text_content += page.extract_text()
        
        # Ensure text is not empty
        if text_content.strip():
            # Summarize the extracted text
            summary = summarize(text_content) 
            st.write(summary)
        else:
            st.warning("The PDF does not contain readable text.")
    except Exception as e:
        st.error(f"An error occurred: {e}")
