import streamlit as st

# from langchain_community.llms import Ollama
from langchain_ollama import OllamaLLM
from langchain_ollama import OllamaEmbeddings
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

# PDF Rag Chat
from langchain_community.document_loaders import PyPDFDirectoryLoader
from langchain_community.vectorstores import Chroma
from langchain.text_splitter import (
    CharacterTextSplitter,
    RecursiveCharacterTextSplitter,
)
from langchain.chains import RetrievalQA
from langchain_community.embeddings import OllamaEmbeddings
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains import create_retrieval_chain

dir_path = "/Users/giggso/Downloads/Books/PDF_Books/PDF_Test"

# Prompt from Template
prompt = ChatPromptTemplate.from_template(
    """
    Answer the questions based on the provided CONTENT ONLY. Do not use any external resources.
    context provided:
    {context}
    Question: {question}
    """
)
# Create Vector Embeddings


def create_vector_embedding():
    if "vectors" not in st.session_state:
        st.session_state.embeddings = OllamaEmbeddings(model="mistral:latest")
        st.session_state.loader = PyPDFDirectoryLoader(dir_path)
        st.session_state.docs = st.session_state.loader.load()
        st.session_state.text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000, chunk_overlap=300
        )
        st.session_state.final_docs = st.session_state.text_splitter.split_documents(
            st.session_state.docs[:50]
        )
        st.session_state.vectors = Chroma.from_documents(
            st.session_state.final_docs, st.session_state.embeddings
        )


# def generate_response(question, engine):
#    llm = initialize_llm(engine)
#    chain = prompt | llm | StrOutputParser()
#    return chain.invoke({"question": question})

llm = OllamaLLM(model="mistral:latest")

# Streamlit APP
st.title("Q&A Chatbot with Ollama RAG")

if st.button("Clear Cache"):
    st.cache_data.clear()
    st.success("Cache cleared successfully!")

user_prompt = st.text_input("Enter the context for the question")

if st.button("Document Embedding"):
    create_vector_embedding()
    st.write("Document Embedding Completed")

# Main Chat Interface
st.write("Ask your question")

# Create the LLM response
import time

if user_prompt:
    try:
        if "vectors" not in st.session_state:
            st.warning("Please create document embeddings first!")
            st.stop()

        retriever = st.session_state.vectors.as_retriever(
            search_type="similarity", search_kwargs={"k": 3}
        )

        qa_chain = RetrievalQA.from_chain_type(
            llm=llm,
            chain_type="stuff",
            retriever=retriever,
            return_source_documents=True,
        )

        start = time.process_time()
        response = qa_chain.invoke(user_prompt)
        elapsed_time = time.process_time() - start

        st.write("Answer:", response["result"])
        st.write(f"Response time: {elapsed_time:.2f} seconds")

        with st.expander("View Source Documents"):
            for i, doc in enumerate(response["source_documents"]):
                st.write(f"Document {i+1}:")
                st.write(doc.page_content)
                st.write("---")

    except Exception as e:
        st.error(f"Error generating response: {str(e)}")
