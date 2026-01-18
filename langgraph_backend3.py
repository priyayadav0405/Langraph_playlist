from langgraph.graph import StateGraph,START,END
from langchain_core.messages import HumanMessage,AIMessage,BaseMessage
from typing import TypedDict,List,Annotated
from langgraph.checkpoint.memory import InMemorySaver
from langgraph.graph.message import add_messages
from langchain_groq import ChatGroq

from dotenv import load_dotenv

load_dotenv()

api_key=''
llm = ChatGroq(model='llama-3.1-8b-instant',api_key=api_key)

class ChatState(TypedDict):
    messages : Annotated[list[BaseMessage], add_messages]

def chat_node(state : ChatState):
    messages = state['messages']

    response = llm.invoke(messages)
    return {'messages' : [response]}

checkpointer = InMemorySaver()

graph=StateGraph(ChatState)
graph.add_node('chat_node' , chat_node)

graph.add_edge(START,'chat_node')
graph.add_edge("chat_node",END)
 
chatbot = graph.compile(checkpointer=checkpointer)

# CONFIG = {'configurable' : {'thread_id' : 'thread-1'}}

# response = chatbot.invoke(
#     {'messages' : [HumanMessage(content = 'Hi my name is nitish')]},
#     config= CONFIG
# )

# print(chatbot.get_state(config=CONFIG))