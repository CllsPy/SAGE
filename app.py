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
        
        if text_content.strip():
            # Get the response from the summarization function
            response = summarize(text_content)
            
            # Extract and display the text from the response
            try:
                text_summary = response.result["candidates"][0]["content"]["parts"][0]["text"]
                st.write(text_summary)
            except (KeyError, IndexError, AttributeError) as e:
                st.error("Unable to parse the summary response. Check the response format.")
        else:
            st.warning("The PDF does not contain readable text.")
    except Exception as e:
        st.error(f"An error occurred: {e}")

