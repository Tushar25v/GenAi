from dotenv import load_dotenv
from google import genai
from google.genai import types
import os

load_dotenv()

apii_key = os.environ["GEM_API_KEY"]

# Only run this block for Gemini Developer API
client = genai.Client(api_key= apii_key)

user_input = str(input("Ask your question ?"))
system_prompt = f"""
You are an expert data scientist who explains complex topics in simple, friendly language.

Always respond in a concise, clear way. Use bullet points if helpful.

TASK:  {user_input} .
"""


response = client.models.generate_content(
    model='gemini-2.0-flash-001', contents= system_prompt,
)
print(response.text)

