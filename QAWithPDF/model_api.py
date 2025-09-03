import os
from dotenv import load_dotenv
import sys

from llama_index.llms.google_genai import GoogleGenAI
from IPython.display import Markdown, display
import google.generativeai as genai
from exception import customexception
from logger import logging

load_dotenv()

GOOGLE_API_KEY=os.getenv("googel_api_key")

genai.configure(api_key=GOOGLE_API_KEY)

def load_model():
    
    """
    Loads a Gemini-Pro model for natural language processing.

    Returns:
    - Gemini: An instance of the Gemini class initialized with the 'gemini-pro' model.
    """
    try:
        model = GoogleGenAI(
            model="gemini-2.0-flash",
            api_key=GOOGLE_API_KEY,  # uses GOOGLE_API_KEY env var by default
        )
        return model
    except Exception as e:
        raise customexception(e,sys)