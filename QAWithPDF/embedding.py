from llama_index.core import VectorStoreIndex
from llama_index.core import StorageContext, load_index_from_storage
from llama_index.embeddings.google_genai import GoogleGenAIEmbedding
from llama_index.core import Settings
from llama_index.core.node_parser import SentenceSplitter

from QAWithPDF.data_ingestion import load_data
from QAWithPDF.model_api import load_model
import google.generativeai as genai
import os
import sys
from exception import customexception
from logger import logging

from dotenv import load_dotenv
load_dotenv()
google_api_key = os.getenv('google_api_key')
genai.configure(api_key=google_api_key)

def download_gemini_embedding(model,document):
    """
    Downloads and initializes a Gemini Embedding model for vector embeddings.

    Returns:
    - VectorStoreIndex: An index of vector embeddings for efficient similarity queries.
    """
    try:
        logging.info("")
        gemini_embed_model = GoogleGenAIEmbedding(
            model_name="text-embedding-004",
            embed_batch_size=100,
            api_key=google_api_key,
        )
        Settings.llm = model
        Settings.embed_model = gemini_embed_model
        Settings.node_parser = SentenceSplitter(chunk_size=800, chunk_overlap=20)
        Settings.num_output = 512
        Settings.context_window = 3900
        
        logging.info("")
        index = VectorStoreIndex.from_documents([document])
        index.storage_context.persist()

        logging.info("")
        query_engine = index.as_query_engine()
        return query_engine
    except Exception as e:
        raise customexception(e,sys)