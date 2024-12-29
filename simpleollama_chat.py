import streamlit as st
from langchain_community.llms import Ollama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# LangSmith Tracking
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_PROJECT_ID"] = "QandA ChatBot with Local Model"

# Cache and Initialize the LLM
@st.cache_resource
def initialize_llm(engine):
    return Ollama(
        model=engine,
    )

# Prompt Template
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a AI coder proficient in python with SQL skills and an AI Assistant, please respond as requested"),
    ("user", "Question:{question}")
])

def generate_response(question, engine):
    llm = initialize_llm(engine)
    chain = prompt | llm | StrOutputParser()
    return chain.invoke({"question": question})

# Streamlit APP
st.title("Q&A Chatbot with Ollama")

# Sidebar configurations
# api_key = st.sidebar.text_input("Enter OpenAI API Key", type="password")
engine = st.sidebar.selectbox(
    "Select Engine of your LLM Model",
    ["llama3.1:latest", "phi3:mini", "mistral:latest"]
)

if st.button('Clear Cache'):
    st.cache_data.clear()
    st.success('Cache cleared successfully!')

# Main Chat Interface
st.write("Ask your question")
user_input = st.text_input("Enter your question here")

if user_input:
        response = generate_response(user_input, engine)
        st.write(response)
        st.write("By Ravi but Powered by Ollama")
else:
    st.write("Please enter your question")
