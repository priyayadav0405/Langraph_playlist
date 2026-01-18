import streamlit as st
import uuid
#calling the graph
from langgraph_database_backend import chatbot,retrieve_all_thread
from langchain_core.messages import HumanMessage


import uuid #for thread id generation
# CONFIG ={'configurable' : {'thread_id' : 'thread-1'}}

#--------------------------------utility functin------------------------------
def generate_thread_id():
    thread_id = uuid.uuid4()
    return thread_id

def reset_chat():
    thread_id = generate_thread_id()
    st.session_state['thread_id'] = thread_id
    add_thread(st.session_state['thread_id'])
    st.session_state['message_history'] =[]

def add_thread(thread_id):
    if thread_id not in st.session_state['chat_threads']:
        st.session_state['chat_threads'].append(thread_id)

def load_conversation(thread_id):
    return chatbot.get_state(config={'configurable' : {'thread_id' : thread_id}}).values['messages']


if 'message_history' not in st.session_state:
    st.session_state['message_history'] = []

#in state of session we can muliple keys like conversation history ,threadid etc
if 'thread_id' not in st.session_state:
    st.session_state['thread_id'] = generate_thread_id()
    # st.session_state['thread_id'] =  thread_id
    # st.session_state['message_history'] = []

if 'chat_threads' not in st.session_state:
    # print(type(retrieve_all_thread))
    threads=retrieve_all_thread()
    st.session_state['chat_threads'] = threads if threads else []

add_thread(st.session_state['thread_id'])
#--------------------------------------SIDEBAR UI------------------

st.sidebar.title('Langgraph Chatbot')
if st.sidebar.button('New Chat'):
    reset_chat()

for thread_id in st.session_state['chat_threads']:
    if st.sidebar.button(str(thread_id)):
        st.session_state['thread_id'] = thread_id
        messages = load_conversation(thread_id)

        temp_messages = []

        for msg in messages:
            if isinstance(msg, HumanMessage):
                role = 'user'
            else:
                role = 'assistant'

            temp_messages.append({'role' :role , 'content': msg.content})

        st.session_state['message_history'] = temp_messages

st.sidebar.header('My Conversation')

st.sidebar.text(st.session_state['thread_id'])


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
                config={'configurable' : {'thread_id' :st.session_state['thread_id']}},
                stream_mode='messages'
            )
        )

    st.session_state['message_history'].append({'role':'assistant','content':ai_message})
