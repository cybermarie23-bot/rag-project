import os
from dotenv import load_dotenv
import google.generativeai as genai
from fastapi import FastAPI

# Load environment variables
load_dotenv()

# Get API key
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

app = FastAPI(title="My RAG Project")

# Basic health check
@app.get("/health")
def health():
    return {"status": "ok", "message": "RAG app is running!"}

# Test Gemini connection
@app.get("/test-gemini")
def test_gemini():
    if not GEMINI_API_KEY:
        return {"error": "GEMINI_API_KEY is missing in .env file"}
    
    try:
        genai.configure(api_key=GEMINI_API_KEY)
        model = genai.GenerativeModel('gemini-3.5-flash')
        prompt = "Explain what a large language model is in one short paragraph."
        response = model.generate_content(prompt)
        return {
            "status": "success",
            "prompt": prompt,
            "response": response.text
        }
    except Exception as e:
        return {"error": str(e)}    