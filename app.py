import streamlit as st
from main import summarize

uploaded_file = st.file_uploader("Upload your research paper (PDF)", type="pdf")
if uploaded_file is not None:
  st.markdown((summarize(uploaded_file)))
