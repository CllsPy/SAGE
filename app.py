import streamlit as st
from main import summarize

uploaded_file = st.file_uploader("Upload your research paper (PDF)", type="pdf")

if uploaded_file is not None:
    # Convert the uploaded file to a binary stream (BytesIO)
    pdf_bytes = uploaded_file.read()

    # Pass the binary PDF data to the summarize function
    summary = summarize(pdf_bytes)
    
    # Display the summary
    st.markdown(summary)
