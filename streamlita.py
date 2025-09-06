import streamlit as st
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_community.document_loaders import TextLoader
from langchain.schema import Document
from dotenv import load_dotenv

load_dotenv()


st.set_page_config(page_title="Minimal RAG")


docs= TextLoader("/Users/parmeetsingh/Desktop/Ai agents/myvenv/sample_text.txt").load()
chunks=RecursiveCharacterTextSplitter(chunk_size=300, chunk_overlap= 50).split_documents(docs)
vs = FAISS.from_documents(chunks, OpenAIEmbeddings())
retriever=vs.as_retriever(search_kwargs= {"k":3})
llm=ChatOpenAI()

prompt=ChatPromptTemplate.from_messages([
    ("system","Answer using context only. If unknown, say you don't know"),
    ("user","Q:{q}\n\n Context:\n{ctx}")]
)

chain={"ctx": retriever, "q":RunnablePassthrough()} | prompt | llm |StrOutputParser()

st.title("Minimal RAG UI")
q = st.text_input("Ask a question:")

if q:
    st.write("**Answer:**", chain.invoke(q))    