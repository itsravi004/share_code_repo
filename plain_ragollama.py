# Import required libraries
from langchain_ollama import OllamaLLM, OllamaEmbeddings
from langchain_core.prompts import ChatPromptTemplate
from langchain_community.document_loaders import PyPDFDirectoryLoader
from langchain_community.vectorstores import Chroma
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chains import RetrievalQA


class DocumentQA:
    def __init__(self, dir_path, model_name="mistral:latest"):
        self.dir_path = dir_path
        self.model_name = model_name
        self.llm = OllamaLLM(model=model_name)
        self.vectors = None

    def create_embeddings(self):
        print("Creating embeddings...")
        embeddings = OllamaEmbeddings(model=self.model_name)
        loader = PyPDFDirectoryLoader(self.dir_path)
        docs = loader.load()
        print(f"Loaded {len(docs)} documents")

        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000, chunk_overlap=300
        )
        final_docs = text_splitter.split_documents(docs[:50])
        print(f"Created {len(final_docs)} text chunks")

        self.vectors = Chroma.from_documents(final_docs, embeddings)
        return "Embeddings created successfully"

    def ask_question(self, question):
        if not self.vectors:
            return "Please create embeddings first"

        print(f"Processing question: {question}")
        retriever = self.vectors.as_retriever(
            search_type="similarity", search_kwargs={"k": 3}
        )

        qa_chain = RetrievalQA.from_chain_type(
            llm=self.llm,
            chain_type="stuff",
            retriever=retriever,
            return_source_documents=True,
        )

        response = qa_chain.invoke(question)
        return {
            "answer": response["result"],
            "sources": [doc.page_content for doc in response["source_documents"]],
        }


# Usage example
if __name__ == "__main__":
    # Initialize the QA system
    pdf_dir = "/Users/giggso/Downloads/Books/PDF_Books/PDF_Test"
    qa_system = DocumentQA(pdf_dir)

    # Create embeddings (do this once)
    qa_system.create_embeddings()

    # Ask questions
    question = "What is the main topic of the documents?"
    result = qa_system.ask_question(question)

    print("\nAnswer:", result["answer"])
    print("\nSources used:")
    for i, source in enumerate(result["sources"], 1):
        print(f"\nSource {i}:")
        print(source)
