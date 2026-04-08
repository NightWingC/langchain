from langchain_community.vectorstores import Chroma
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
from langchain_classic.retrievers import MultiQueryRetriever
from langchain_google_genai import GoogleGenerativeAI, GoogleGenerativeAIEmbeddings
import streamlit as st
from mll.mll import mll
from config import (
    EMBEDDING_MODEL,
    CHROMA_DB_PATH,
    QUERY_MODEL,
    GENERATION_MODEL,
    SEARCH_TYPE,
    SEARCH_K,
    MMR_DIVERSITY_LAMBDA,
    MMR_FETCH_K,
)

from prompts import (
    MULTI_QUERY_PROMPT,
    RAG_TEMPLATE
)


def initialize_rag_system():
    vectorestore = Chroma(
        embedding_function=GoogleGenerativeAIEmbeddings(model=EMBEDDING_MODEL),
        persist_directory=CHROMA_DB_PATH,
    )
    
    # Modelos
    llm_query = GoogleGenerativeAI(model=QUERY_MODEL, temperature=0)
    llm_generation = GoogleGenerativeAI(model=GENERATION_MODEL, temperature=0)
    
    # Retriver MMR (Maximal Marginal Relevance)
    base_retriver = vectorestore.as_retriever(
        search_type=SEARCH_TYPE,
        search_kwargs={
            "k": SEARCH_K,
            "lambda_mult": MMR_DIVERSITY_LAMBDA,
            "fetch_k": MMR_FETCH_K,
        }
    )
    
    # Definir un prompt personalizado para el retriever
    multi_query_prompt = PromptTemplate.from_template(MULTI_QUERY_PROMPT)
    
    # MultiQueryRetriver con prompt personalizado
    mmr_multi_retriever = MultiQueryRetriever.from_llm(
        retriever=base_retriver,
        llm=llm_query,
        query_prompt=multi_query_prompt,
    )
    
    prompt = PromptTemplate.from_template(RAG_TEMPLATE)
    
    rag_chain = (
        {
            "context": mmr_multi_retriever,
            "question": RunnablePassthrough(),
        } 
        | prompt 
        | llm_generation 
        | StrOutputParser()
    )
    
    return rag_chain, mmr_multi_retriever