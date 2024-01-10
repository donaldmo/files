import streamlit as st
import random
import time

from dotenv import load_dotenv
from langchain.llms import HuggingFaceHub
from langchain.chains import LLMChain 
from langchain.prompts import PromptTemplate


load_dotenv()


def get_response(ques):
    llm = HuggingFaceHub(
        repo_id='mrm8488/t5-base-finetuned-wikiSQL', 
        # model_kwargs={"temperature": 0.5, "max_length": 64}
    )

    template = 'Translate English to SQL: {question}'

    temp2 = 'In {lang}: {question}'

    prompt = PromptTemplate(
        template=template,
        input_variables=["question"]
    )

    llm_chain = LLMChain(prompt=prompt, llm=llm, verbose=True)

    return llm_chain.run(ques)    


if __name__ == '__main__':

    st.title('Simple Chat')

    lang = st.selectbox(
        "Select the Language of  the Solution:", ("Python", "C++", "Java", "SQL")
    )

    # question = "What is the average of the respondents using a mobile device?"

    if 'messages' not in st.session_state:
        st.session_state.messages = []

    # Display chat messages from history on app rerun
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    if prompt := st.chat_input("What is up?"):
        # answer = get_response(prompt)

        with st.chat_message("user"):
            st.markdown(prompt)

        with st.chat_message('assistant'):
            message_placeholder = st.empty()
            full_response = ''

            assistant_response = random.choice([
                'Hello there! How can I assist you today?',
                'Hi, Is there anything I can help you with?',
                'Do you need help?',
            ])

            for chunk in assistant_response.split():
                full_response += chunk + ' '
                time .sleep(0.05)

                message_placeholder.markdown(full_response + "▌")

            message_placeholder.markdown(full_response)
            
        st.session_state.messages.append({
            "role": "user", "content": prompt
        })
