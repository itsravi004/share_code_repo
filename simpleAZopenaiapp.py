import os

# from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.chat_models import AzureChatOpenAI
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# LangSmith Tracking
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_PROJECT_ID"] = "AZ OpenAI Testbot"


def ask_question(question):
    # Initialize the Azure ChatGPT model
    model = AzureChatOpenAI(
        deployment_name="gpt-35-turbo-16k",  # Replace with your Azure deployment name
        temperature=0.5,
        openai_api_key=os.getenv("OPENAI_API_KEY"),
        openai_api_base=os.getenv("OPENAI_API_BASE"),
        openai_api_version=os.getenv("OPENAI_API_VERSION"),
        openai_api_type=os.getenv("OPENAI_API_TYPE"),
    )

    # Ask the question
    response = model(
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": question},
        ]
    )
    return response["choices"][0]["message"]["content"]


if __name__ == "__main__":
    # Test question
    question = "Who is the Prime Minister of France?"
    answer = ask_question(question)
    print("Answer:", answer)
