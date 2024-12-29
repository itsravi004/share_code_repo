import streamlit as st
import openai
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate, BaseChatPromptTemplate, ChatMessagePromptTemplate

import os
from dotenv import load_dotenv

#langsmith Tracking
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_PROJECT_ID"]="QandA ChatBot with OpenAI"

#Prompt Template
prompt = ChatPromptTemplate.from_messages(
    [
        ("system","You are a AI coder proficient in python with SQL skills and an AI Assistant, please respond as requested"),
        ("user","Question:{question}")
    ]
)

def generate_response(question,api_key,llm,temperature,max_tokens):
    openai.api_key = api_key
    llm = ChatOpenAI(model=llm)
    outputparser = StrOutputParser()
    chain = prompt|llm|outputparser
    answer = chain.invoke(question=question,temperature=temperature,max_tokens=max_tokens)
    return answer

# Streamlit APP
st.title("Q&A Chatbot with OpenAI")
api_key = st.sidebar.text_input("Ender OpenAI API Key",type="password")
# Dropdown for LLM Model
llm = st.sidebar.selectbox("Select Open AI LLM Model",["gpt-3.5-turbo","gpt-4o-2024-11-20","gpt-4o-mini-2024-07-18","o1-mini-2024-09-12"])  

#Adjust Temprature and Max Tokens
temperature = st.sidebar.slider("Select Temprature",min_value=0.0,max_value=1.0,value=0.9,step=0.1)
max_tokens = st.sidebar.slider("Select Max Tokens",min_value=50,max_value=500,value=200,step=50)

# Main Chat Interface
st.write("Ask your question")
user_input = st.text_area("Enter your question here")

if user_input:
    response = generate_response(user_input,api_key,llm,temperature,max_tokens)
    st.write(response)
    st.write("By Ravi but Powered by OpenAI")
else:
    st.write("Please enter your question")