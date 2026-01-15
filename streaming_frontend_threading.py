import streamlit as st

#calling the graph
from langgraph_backend_2 import chatbot
from langchain_core.messages import HumanMessage


import uuid #for thread id generation
# CONFIG ={'configurable' : {'thread_id' : 'thread-1'}}

#--------------------------------utility functin------------------------------
def generate_thread_id():
    thread_id = uuid.uuid64()
    return thread_id

if 'message_history' not in st.session_state:
    st.session_state['message_history'] = []

#in state of session we can muliple keys like conversation history ,threadid etc
if 'thread_id' not in st.session_state:
    st.session_state['thread_id'] = generate_thread_id()
#--------------------------------------SIDEBAR UI------------------

st.sidebar.title('Langgraph Chatbot')
st.sidebar.button('New Chat')

st.sidebar.header('My Conversation')




#-------------------------MAIN UI---------------------------------------------------------------->
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
