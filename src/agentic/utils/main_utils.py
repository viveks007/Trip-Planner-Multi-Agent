import re
# from taskflowai import GeminiModels, set_verbosity
import os
from dotenv import load_dotenv
from src.agentic.logger import logging
from src.agentic.exceptions import CustomException
import sys
import google.generativeai as genai

# Load env variables
load_dotenv()

# Validate required API keys
required_keys = ["GEMINI_API_KEY"]
missing_keys = [key for key in required_keys if not os.getenv(key)]
if missing_keys:
    raise CustomException(sys, "missing required env variables: " + ','.join(missing_keys))

# Configure Gemini API
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))


class LoadModel:
    @classmethod
    def load_gemini_model(cls):
        """Load and return the Gemini model"""
        try:
            logging.info("Loading Gemini model")
            model = "gemini-2.5-flash"  # direct model name
            # quick test call to verify API connectivity
            genai.GenerativeModel(model).generate_content("test connection")
            logging.info("Gemini model loaded and API verified successfully")
            return model
        except Exception as e:
            logging.info("Failed to load Gemini model or verify API key")
            raise CustomException(sys, e)
