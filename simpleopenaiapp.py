import streamlit as st
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# LangSmith Tracking
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_PROJECT_ID"] = "QandA ChatBot with OpenAI"


# Cache and Initialize the LLM
@st.cache_resource
def initialize_llm(api_key, model_name, temperature, max_tokens):
    return ChatOpenAI(
        api_key=api_key,
        model=model_name,
        temperature=temperature,
        max_tokens=max_tokens,
    )


# Prompt Template
prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You are a AI coder proficient in python with SQL skills and an AI Assistant, please respond as requested",
        ),
        ("user", "Question:{question}"),
    ]
)


def generate_response(question, api_key, model_name, temperature, max_tokens):
    llm = initialize_llm(api_key, model_name, temperature, max_tokens)
    chain = prompt | llm | StrOutputParser()
    return chain.invoke({"question": question})


# Streamlit APP
st.title("Q&A Chatbot with OpenAI")

# Sidebar configurations
api_key = st.sidebar.text_input("Enter OpenAI API Key", type="password")
model_name = st.sidebar.selectbox(
    "Select Open AI LLM Model",
    ["gpt-3.5-turbo", "gpt-4-0125-preview", "gpt-4-turbo-preview"],
)
temperature = st.sidebar.slider(
    "Select Temperature", min_value=0.0, max_value=1.0, value=0.7, step=0.1
)
max_tokens = st.sidebar.slider(
    "Select Max Tokens", min_value=50, max_value=500, value=200, step=50
)

# Main Chat Interface
st.write("Ask your question")
user_input = st.text_input("Enter your question here")

if user_input:
    if not api_key:
        st.warning("Please enter your OpenAI API key!", icon="⚠️")
    else:
        response = generate_response(
            user_input, api_key, model_name, temperature, max_tokens
        )
        st.write(response)
        st.write("By Ravi but Powered by OpenAI")
else:
    st.write("Please enter your question")
