import streamlit as st
from main import summarize
import google.generativeai as genai

# Upload the PDF
uploaded_file = st.file_uploader(type='pdf')
if uploaded_file is not None:
    summary = summarize(uploaded_file) 
    summary
    

