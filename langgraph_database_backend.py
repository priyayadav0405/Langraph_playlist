from langgraph.graph import StateGraph,START,END
from langchain_core.messages import HumanMessage,AIMessage,BaseMessage
from typing import TypedDict,List,Annotated
#we will use any other memory
# from langgraph.checkpoint.memory import InMemorySaver

from langgraph.checkpoint.sqlite import SqliteSaver

from langgraph.graph.message import add_messages
from langchain_groq import ChatGroq

from dotenv import load_dotenv
import sqlite3
load_dotenv()

api_key=''
llm = ChatGroq(model='llama-3.1-8b-instant',api_key=api_key)

class ChatState(TypedDict):
    messages : Annotated[list[BaseMessage], add_messages]

def chat_node(state : ChatState):
    messages = state['messages']

    response = llm.invoke(messages)
    return {'messages' : [response]}

conn = sqlite3.connect(database = 'chatbot.db', check_same_thread=False)
checkpointer = SqliteSaver(conn =conn)

graph=StateGraph(ChatState)
graph.add_node('chat_node' , chat_node)

graph.add_edge(START,'chat_node')
graph.add_edge("chat_node",END)
 
chatbot = graph.compile(checkpointer=checkpointer)

# CONFIG = {'configurable' : {'thread_id' : 'thread-2'}}

# response = chatbot.invoke(
#     {'messages' : [HumanMessage(content = 'india')]},
#     config= CONFIG
# )

# print(chatbot.get_state(config=CONFIG))

# print(checkpointer.list(None))
def retrieve_all_thread():
    all_threads = set()
    for checkpoint in checkpointer.list(None):

    # print(checkpoint.config['configurable']['thread_id'])
        all_threads.add(checkpoint.config['configurable']['thread_id'])

    print(list(all_threads))
    return list(all_threads)