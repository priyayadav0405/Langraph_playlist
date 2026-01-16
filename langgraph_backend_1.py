from langchain_groq import ChatGroq
from langgraph.graph import START,END,StateGraph
from langgraph.checkpoint.memory import InMemorySaver,MemorySaver
from langgraph.graph.message import add_messages
from typing import Annotated,TypedDict
from dotenv import load_dotenv
from langchain_core.messages import BaseMessage
load_dotenv()

api_key=''
llm = ChatGroq(model='llama-3.1-8b-instant',api_key=api_key)

class ChatState(TypedDict):
    messages : Annotated[list[BaseMessage] , add_messages]

def chat_node(state : ChatState)->ChatState:
    messages  = state['messages']
    responses = llm.invoke(messages)

    return {'messages' : responses}


checkpointer = InMemorySaver()

graph = StateGraph(ChatState)

graph.add_node('chat_node',chat_node)
graph.add_edge(START,"chat_node")
graph.add_edge("chat_node",END)

chatbot = graph.compile(checkpointer=checkpointer)
