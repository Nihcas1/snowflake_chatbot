import os
import streamlit as st
from PyPDF2 import PdfReader
import google.generativeai as genai
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain.vectorstores import Pinecone as LangchainPinecone
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chains.question_answering import load_qa_chain
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv
import requests
from bs4 import BeautifulSoup
from pinecone import Pinecone, ServerlessSpec
from langchain.docstore.document import Document

# Load environment variables
load_dotenv()
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "D:/snowflake/credentials.json"
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Initialize Pinecone
pc = Pinecone(api_key=os.getenv("PINECONE_API_KEY"))

index_name = "snowflake-chatbot"
if index_name not in pc.list_indexes().names():
    pc.create_index(
        name=index_name,
        dimension=1536,
        metric="euclidean",
        spec=ServerlessSpec(cloud='aws', region='us-west-2')
    )

def get_pdf_text(pdf_docs):
    text = ""
    for pdf in pdf_docs:
        pdf_reader = PdfReader(pdf)
        for page in pdf_reader.pages:
            text += page.extract_text()
    return text    

def get_text_chunks(text):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=2000, chunk_overlap=200)
    chunks = text_splitter.split_text(text)
    return chunks

def get_vector_store(text_chunks):
    documents = [Document(page_content=chunk) for chunk in text_chunks]
    embeddings = GoogleGenerativeAIEmbeddings(model='models/embedding-001')
    vector_store = LangchainPinecone.from_documents(documents, embedding=embeddings, index_name=index_name)

def get_conversational_chain():
    prompt_template = """
    Answer the question as detailed as possible from the provided context. If the answer is not in the provided context, explain with examples and use cases from your knowledge.
    \n\n
    Context:\n {context}?\n
    Question:\n{question}\n
    
    Answer:
    """
    model = ChatGoogleGenerativeAI(model='gemini-pro', temperature=0.5)
    prompt = PromptTemplate(template=prompt_template, input_variables=["context", "question"])
    chain = load_qa_chain(model, chain_type="stuff", prompt=prompt)
    return chain

def search_snowflake_documentation(query):
    search_url = f"https://docs.snowflake.com/en/search.html?q={query.replace(' ', '+')}"
    response = requests.get(search_url)

    if response.ok:
        soup = BeautifulSoup(response.text, 'html.parser')
        results = soup.find_all('a', class_='result-link')
        if results:
            return results[0].get_text()  # Return the first relevant result text
    return "No relevant information found in the Snowflake documentation."

def user_input(user_question, memory):
    # Load embeddings for similarity search
    embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
    new_db = LangchainPinecone.from_existing_index(index_name=index_name, embedding=embeddings)
    
    # Search Pinecone for relevant documents
    docs = new_db.similarity_search(user_question)

    # Initialize the chain
    chain = get_conversational_chain()
    
    # Start combining the retrieved documents and web search results
    combined_context = ""
    
    if docs:
        # If documents are retrieved from Pinecone, combine their content
        combined_context = " ".join([doc.page_content for doc in docs])
    
    # Search the Snowflake documentation as well
    snowflake_result = search_snowflake_documentation(user_question)
    
    # Add the Snowflake documentation result to the context
    combined_context += f"\nSnowflake Documentation Result: {snowflake_result}"
    
    # Generate the final response using the combined context
    # Now we pass the retrieved documents from Pinecone as `input_documents` and the combined context to the model.
    response = chain(
        {"input_documents": docs, "question": user_question, "context": combined_context},
        return_only_outputs=True
    )["output_text"]

    # Store the user question and response in memory
    if memory.get("chat_history") is None:
        memory["chat_history"] = []
    memory["chat_history"].append({"question": user_question, "response": response})
    
    return response

def main():
    st.set_page_config("Chat with PDF")
    st.header("Clear doubts on Snowflake")
    
    if "memory" not in st.session_state:
        st.session_state.memory = {}

    user_question = st.text_input("Ask a question which you have a doubt")

    if user_question:
        response = user_input(user_question, st.session_state.memory)
        st.write("Reply: ", response)
    
    with st.sidebar:
        st.title("Menu:")
        pdf_docs = st.file_uploader("Upload your PDF files", accept_multiple_files=True)
        if st.button("Submit & Process"):
            with st.spinner("Processing..."):
                raw_text = get_pdf_text(pdf_docs)
                text_chunks = get_text_chunks(raw_text)
                get_vector_store(text_chunks)
                st.success("Done")

if __name__ == "__main__":
    main()
