import streamlit as st
import PyPDF2
from main import summarize
import google.generativeai as genai

import streamlit as st
import PyPDF2
from main import summarize

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

            with st.spinner("Analyzing paper... this takes about a minute"):
                response = summarize(text_content)
            
            # Extract the summarized text
            try:
                summarized_text = (response.text)

                with st.expander:
                    st.write(summarized_text)
                    
            except (KeyError, IndexError, AttributeError) as e:
                st.error(f"Unable to parse the summary response. Check the response format. Error: {e}")
        else:
            st.warning("The PDF does not contain readable text.")
    except Exception as e:
        st.error(f"An error occurred: {e}")

