from llama_index.core import SimpleDirectoryReader
from llama_index.core import Document

import sys
from exception import customexception
from logger import logging
import os

def load_data(data):
    """
    Load PDF documents from a specified directory.

    Parameters:
    - data (str): The path to the directory containing PDF files.

    Returns:
    - A list of loaded PDF documents. The specific type of documents may vary.
    """
    try:
        if data is not None:
            if data.name.endswith(".txt"):
                text = data.read().decode("utf-8")

            elif data.name.endswith(".pdf"):
                from PyPDF2 import PdfReader
                reader = PdfReader(data)
                text = "\n".join(page.extract_text() for page in reader.pages if page.extract_text())

            # Create LlamaIndex Document object
            doc = Document(text=text, metadata={"name": data.name})
            return doc

    except Exception as e:
        logging.info("exception in loading data...")
        raise customexception(e,sys)