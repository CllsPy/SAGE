import streamlit as st
import PyPDF2
from main import summarize
import google.generativeai as genai
import streamlit as st
import PyPDF2
from main import summarize
import time
import streamlit as st

with st.form('Gemini Paper Summarizer'):
    st.header("Gemini Summarizer")
    uploaded_file = st.file_uploader('', type='pdf')
    if uploaded_file is not None:
        try:
            pdf_reader = PyPDF2.PdfReader(uploaded_file)
            text_content = ""
            
            for page in pdf_reader.pages:
                text_content += page.extract_text()
            
            if text_content.strip():
                # Get the response from the summarization function
    
                with st.spinner("Wait..."):
                    time.sleep(5)
                    response = summarize(text_content)
                    st.write("DONE!")
                
                try:
                        summarized_text = (response.text)
                        st.write(summarized_text)
                        
                except (KeyError, IndexError, AttributeError) as e:
                    st.error(f"Unable to parse the summary response. Check the response format. Error: {e}")
            else:
                st.warning("The PDF does not contain readable text.")
        except Exception as e:
            st.error(f"An error occurred: {e}")

