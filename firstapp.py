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