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
            
            # Debug: Print the full response structure
            st.write("Debug Response:", response)

            # Attempt to extract the text
            try:
                # Update this path based on the response structure
                text_summary = response.result["candidates"][0]["content"]["parts"][0]["text"]
                st.write(text_summary)
            except Exception as e:
                st.error(f"Unable to parse the summary response. Error: {e}")
        else:
            st.warning("The PDF does not contain readable text.")
    except Exception as e:
        st.error(f"An error occurred: {e}")

