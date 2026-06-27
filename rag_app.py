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
        
        # Step 1: Generate a short outline
        outline_prompt = "Create a short 3-point outline explaining what a large language model is."
        outline_response = model.generate_content(outline_prompt)
        outline = outline_response.text
        
        # Step 2: Use the outline to create a full explanation
        full_prompt = f"Using this outline, write a clear and detailed explanation of large language models:\n\n{outline}"
        full_response = model.generate_content(full_prompt)
        
        return {
            "status": "success",
            "step1_outline": outline,
            "step2_final_response": full_response.text
        }
        
    except Exception as e:
        return {"error": str(e)}