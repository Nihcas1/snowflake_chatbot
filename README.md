# 📚 Snowflake Conversational Assistant

![image](https://github.com/user-attachments/assets/be23eea5-a72b-461c-8338-64bbfa17eff5)

***Overview***  
This project is a conversational assistant that interacts with PDF documents to help you answer questions related to Snowflake, using Google Generative AI and Pinecone for vector-based searches.  
The assistant allows you to upload PDFs and retrieve specific answers from both the provided documents and official Snowflake documentation.  
It integrates LangChain for text processing and Google’s Gemini Pro model for generating detailed answers.

---

**✨ Features**  
- 🔍 **PDF Document Search**: Upload multiple PDFs and extract text for question-answering.  
- 💬 **Conversational Memory**: Save chat history to enable better flow in conversations.  
- 🌐 **Snowflake Documentation Search**: Automatically search the official Snowflake documentation for any queries not provided in PDFs.  
- 🧠 **Pinecone Vector Store**: Store document chunks in Pinecone to make your queries more efficient through vector-based similarity searches.  
- 🤖 **Generative AI Response**: Use Google’s Generative AI model (Gemini Pro) to generate highly accurate and detailed responses.  
- 🛠️ **Streamlit Interface**: Simple and interactive user interface powered by Streamlit.

---

**🚀 Installation**  
1. **Clone the repository**:  
   ```bash
   git clone https://github.com/nihcas1/snowflake-chatbot.git 


---

📝 **Usage**  
- **Upload PDFs**: In the sidebar, upload one or more PDF files that contain relevant documentation.  
- **Ask Questions**: Type in your questions in the main text box.  
- **Get Answers**: The assistant will search the uploaded PDFs and Snowflake's official documentation, then respond with the most relevant answer.

---

🔧 **Tech Stack**  
- **Streamlit**: Interactive web interface  
- **LangChain**: Text processing and chain management  
- **Pinecone**: Vector-based search engine  
- **Google Generative AI (Gemini Pro)**: Used for embedding and response generation  
- **PyPDF2**: PDF text extraction  
- **BeautifulSoup**: Web scraping for Snowflake documentation search  

---

🌟 **Future Enhancements**  
- **Add Chat Export**: Ability to export chat history in multiple formats (PDF, JSON).  
- **Multilingual Support**: Integrate multi-language support for broader use.  
- **Enhanced Documentation Search**: Improve the ranking and retrieval accuracy from Snowflake's documentation.  
- **Improved Memory**: Introduce more advanced memory features for longer and more contextual conversations.

---

🎯 **How It Works**  
- **PDF Processing**: Uploaded PDFs are parsed using PyPDF2, and the text is split into chunks using LangChain’s RecursiveCharacterTextSplitter.  
- **Embedding**: The text chunks are embedded using Google Generative AI Embeddings and stored in Pinecone for fast vector-based search.  
- **Question Answering**: When a question is asked, the assistant retrieves relevant document chunks from Pinecone and generates an answer using Gemini Pro. If the answer isn’t found in the documents, the app will scrape the Snowflake documentation for additional context.  
- **Conversational Flow**: The app keeps track of chat history and leverages previous conversations to create a seamless, contextual experience.

---

   
   
