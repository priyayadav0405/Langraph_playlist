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

#streaming is added here not invoke

# stream = chatbot.stream(
#     {'messages' : [HumanMessage(content='What is the recipe to make pasta?')]},

#     config = {'configurable' : {'thread_id' : 'thread-1'}}
# ) 

#the class will be generator
#the stream has two obvject inside it meta data and message chunk
# print(type(stream))


# for message_chunk, metadata in chatbot.stream(
#     {'messages' : [HumanMessage(content = 'what is the recipe to make pasta?')]},
#     config = {'configurable' : {'thread_id' : 'thread-1'}},
#     stream_mode='messages'
# ):
#     if message_chunk.content:
#         print(message_chunk.content , end =" " , flush=True)


