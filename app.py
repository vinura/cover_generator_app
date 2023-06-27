import streamlit as st
from langchain.llms import OpenAI
from main import *
st.title('Cover Letter Generator')

# openai_api_key = st.sidebar.text_input('OpenAI API Key')

def generate_response(url, cv):
  output = get_cover_letter(url, cv)
  st.write(output)

with st.form('my_form'):
    text = st.text_area('Enter LinkedIn Job URL:', 'Full URL with https:// ...')
    files = st.file_uploader("Upload files", type=["pdf"], accept_multiple_files=False)

    submitted = st.form_submit_button('Submit')

    # if not openai_api_key.startswith('sk-'):
    #     st.warning('Please enter your OpenAI API key!', icon='⚠')

    # if submitted and openai_api_key.startswith('sk-'):
    if submitted:
        generate_response(text, files)