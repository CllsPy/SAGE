import streamlit as st
from main import summarize
import fitz  # PyMuPDF

# Upload the PDF
uploaded_file = st.file_uploader("Upload your research paper (PDF)", type="pdf")

def extract_text_from_pdf(pdf_file):
    """Extracts text from the given PDF."""
    with fitz.open(stream=pdf_file, filetype="pdf") as doc:
        text = ""
        for page in doc:
            text += page.get_text()  # Extract text from each page
    return text

if uploaded_file is not None:
    # Extract text from the PDF
    pdf_text = extract_text_from_pdf(uploaded_file.read())

    # Pass the extracted text to the summarize function
    summary = summarize(pdf_text)  # Assuming summarize now expects text

    # Display the summary
    st.markdown(summary)
