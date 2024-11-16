import streamlit as st
from main import summarize

uploaded_file = st.file_uploader("Upload your research paper (PDF)", type="pdf")
if uploaded_file is not None:
  pdfFile = genai.upload_file(path=uploaded_file, name=name, resumable=True)
  st.markdown((summarize(pdfFile)))
