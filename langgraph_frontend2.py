import streamlit as st

#calling the graph
from langgraph_backend_2 import chatbot
from langchain_core.messages import HumanMessage
CONFIG ={'configurable' : {'thread_id' : 'thread-1'}}

if 'message_history' not in st.session_state:
    st.session_state['message_history'] = []

#loading the conversation history
for message in st.session_state['message_history']:
    with st.chat_message(message['role']):
        st.text(message['content'])

user_input = st.chat_input('Type here')

if user_input:

    #first add the message to message history
    #we are adding role and content so that we can differentiate which is ai message and which is user message when extracted or read
    st.session_state['message_history'].append({'role' : 'user','content':user_input})

    with st.chat_message('user'):
        st.text(user_input)

    # response = chatbot.invoke({'messages' : [HumanMessage(content = user_input)]}, config=CONFIG)

    with st.chat_message('assistant'):
        ai_message = st.write_stream(
            message_chunk.content for message_chunk , metadata in chatbot.stream(
                {'messages' : [HumanMessage(content=user_input)]},
                config={'configurable' : {'thread_id' :'thread-1'}},
                stream_mode='messages'
            )
        )

    st.session_state['message_history'].append({'role':'user','content':ai_message})
