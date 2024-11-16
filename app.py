import streamlit as st
from main import summarize
import google.generativeai as genai

# Upload the PDF
#uploaded_file = st.file_uploader("Upload your research paper (PDF)", type="pdf")
uploaded_file = st.file_uploader(genai.upload_file())
if uploaded_file is not None:

    file = genai.get_file(uploaded_file)
    summary = summarize(file) 
    summary
    

