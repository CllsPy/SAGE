import streamlit as st
from main import summarize
import fitz  # PyMuPDF

# Upload the PDF
uploaded_file = st.file_uploader("Upload your research paper (PDF)", type="pdf")

# def extract_text_from_pdf(pdf_file):
#     """Extracts text from the given PDF."""
#     with fitz.open(stream=pdf_file, filetype="pdf") as doc:
#         text = ""
#         for page in doc:
#             text += page.get_text()  # Extract text from each page
#     return text

if uploaded_file is not None:
    file = genai.get_file(uploaded_file)
    summary = summarize(file) 
    file
    

