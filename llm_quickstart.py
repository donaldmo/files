from langchain.llms import HuggingFaceHub, OpenAI
import streamlit as st

st.title('🦜🔗 Quickstart App')

openai_api_key = ''

def generate_response(input_text,language_model=None):
    models = ['openai', 'hugginface']
    model = language_model if language_model else 'huggingface'
        
    llm = None
    
    if model == 'huggingface':
        llm = HuggingFaceHub(
            repo_id=''
        )

    if model == 'openai':
        llm = OpenAI(
            temperature=0.7, 
            openai_api_key=openai_api_key
        )

    st.info(llm(input_text))

with st.form('my_form'):
    text = st.text_area(
        'Enter text:',
        'What are the three pieces of advise for learning how to code?'
    )

    submitted = st.form_submit_button('Submit')

    if not openai_api_key.startswith('sk-'):
        st.warning('Please enter your OpenAI API key!', icon='⚠')

    if submitted and openai_api_key.startswith('sk-'):
        generate_response(text)        