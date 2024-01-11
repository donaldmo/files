template = f'''
    Give a {lang} solution for the Leetcode question
    Leetcode Question: {question}
    {lang} Solution: 
'''



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