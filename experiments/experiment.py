import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Function to ensure environment variables are set
def set_if_undefined(var_name: str, prompt: str):
    if not os.environ.get(var_name):
        os.environ[var_name] = input(f"{prompt}: ").strip()

# Ensure API keys are set
set_if_undefined("GEMINI_API_KEY", "Enter your GEMINI API key")
set_if_undefined("WEATHER_API_KEY", "Enter your Weather API key")
set_if_undefined("SERPER_API_KEY", "Enter your Serper API key")
set_if_undefined("AMADEUS_API_KEY", "Enter your Amadeus API key")
set_if_undefined("AMADEUS_API_SECRET", "Enter your Amadeus API secret")
set_if_undefined("GROQ_API_KEY", "Enter your Groq API Key")
set_if_undefined("GEMINI_API_KEY", "Enter your OPENAI API Key")


# Retrieve the API keys from environment variables
#openai_api_key = os.getenv("OPENAI_API_KEY")
weather_api_key = os.getenv("WEATHER_API_KEY")
serper_api_key = os.getenv("SERPER_API_KEY")
amadeus_api_key = os.getenv("AMADEUS_API_KEY")
amadeus_api_secret = os.getenv("AMADEUS_API_SECRET")
groq_api_key = os.getenv("GROQ_API_KEY")
gemini_api_key = os.getenv("OPENAI_API_KEY")


# Print confirmation (for debugging; remove in production)
print("API keys loaded successfully.")



from taskflowai import Agent, OpenrouterModels, Task, AmadeusTools, OpenaiModels, WikipediaTools, WebTools, set_verbosity
import streamlit as st

set_verbosity(True)

# Define agents
web_research_agent = Agent(
    role="Web Research Agent",
    goal="Research destinations and find relevant images",
    attributes="diligent, thorough, comprehensive, visual-focused",
    llm=GeminiModels.gemini_2_5_flash,
    tools=[WebTools.serper_search, WikipediaTools.search_articles, WikipediaTools.search_images]
)

travel_agent = Agent(
    role="Travel Agent",
    goal="Assist travelers with their queries",
    attributes="friendly, hardworking, and detailed in reporting back to users",
    llm=GeminiModels.gemini_2_5_flash,
    tools=[AmadeusTools.search_flights, WebTools.get_weather_data]
)

reporter_agent = Agent(
    role="Travel Report Agent",
    goal="Write comprehensive travel reports with visual elements",
    attributes="friendly, hardworking, visual-oriented, and detailed in reporting",
    llm=GeminiModels.gemini_2_5_flash
)
       