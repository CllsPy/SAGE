import streamlit as st
from main import summarize

uploaded_file = st.file_uploader("Choose a file")
st.markdown((summarize(uploaded_file)))
