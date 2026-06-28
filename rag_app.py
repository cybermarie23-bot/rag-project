from pydantic import BaseModel
from fastapi import FastAPI, HTTPException
import os
from dotenv import load_dotenv
import google.generativeai as genai
from fastapi import FastAPI
class QueryRequest(BaseModel):
    question: str
def validate_user_input(text: str):
    if text is None or text.strip() == "":
        raise HTTPException(status_code=400, detail="Question cannot be empty")

    if len(text) < 5:
        raise HTTPException(status_code=400, detail="Question is too short")

    if len(text) > 500:
        raise HTTPException(status_code=400, detail="Question is too long")
def validate_model_output(text: str):
    if text is None or text.strip() == "":
        raise HTTPException(status_code=500, detail="AI returned an empty response")

    if len(text) < 10:
        raise HTTPException(status_code=500, detail="AI response is too short")
def review_model_output(original_answer: str):
    review_prompt = f"""
You are reviewing an AI-generated response.

Your job:
- If the response is unclear, incomplete, or poorly written, improve it.
- If the response is already good, return it unchanged.

AI response to review:
{original_answer}
"""

    review_model = genai.GenerativeModel("gemini-3.5-flash")
    review_response = review_model.generate_content(review_prompt)

    return review_response.text

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
@app.post("/query")
def query_ai(request: QueryRequest):
    validate_user_input(request.question)

    primary_model = genai.GenerativeModel("gemini-3.5-flash")
    primary_response = primary_model.generate_content(request.question)

    raw_answer = primary_response.text

    validate_model_output(raw_answer)

    reviewed_answer = review_model_output(raw_answer)

    return {
        "question": request.question,
        "answer": reviewed_answer
    }