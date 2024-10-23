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
   
