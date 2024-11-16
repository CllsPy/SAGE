import streamlit as st
from main import summarize

uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
  st.markdown((summarize(uploaded_file)))
