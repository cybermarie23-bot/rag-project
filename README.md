\## Week 4 Progress



\- Created virtual environment and installed dependencies

\- Set up .env file with Gemini API key (securely)

\- Created basic rag\_app.py with FastAPI

\- Health endpoint is working at http://127.0.0.1:8000/health

\- Learned how to load environment variables safely



Next week: Add actual Gemini calls and start building RAG logic.



\## Week 5 Progress



\- Successfully implemented first Gemini API call in backend

\- Created /test-gemini endpoint that returns AI-generated response

\- Learned how to use google-generativeai SDK

\- API key is securely loaded from .env file (never exposed)

\- Understood basic structure of calling LLMs from backend



Key Learning: Always keep API keys server-side and never hardcode them.



\## Week 6 Progress - Multi-Step Execution



\- Updated the /test-gemini endpoint to perform multi-step execution.

\- Step 1: Generate a short outline using Gemini.

\- Step 2: Use the outline from Step 1 to create a full detailed response.

\- Successfully tested the endpoint — the final answer now depends on the first step.

\- Learned how to chain multiple AI calls together inside the backend.



Challenges:

\- Fixed Python indentation errors.

\- Troubleshot model names and rate limits on the free Gemini tier.



This multi-step approach is important because real AI systems often need several stages to produce better, more structured results.



\# RAG Project



This is a Retrieval-Augmented Generation (RAG) project built as part of the GenAI Engineer course.



\## Week 7 Progress - Validating User Input and AI Output



\*\*What was built:\*\*

\- Input validation (`validate\_user\_input`) to reject empty, too short, or too long questions.

\- Output validation (`validate\_model\_output`) to reject empty or too short AI responses.

\- Second AI model call (`review\_model\_output`) to review and improve the first model's answer.

\- New `/query` POST endpoint that combines everything.



\*\*Successful Test:\*\*

\- Question: "What is retrieval augmented generation?"

\- Got a detailed, reviewed response from Gemini.



\*\*Validation Tests:\*\*

\- Empty question → Error: "Question cannot be empty"

\- Short question ("hi") → Error: "Question is too short"



\*\*Challenges:\*\*

\- Persistent rate limit / quota issues with Gemini API.

\- Model name errors (had to use gemini-3.5-flash).

\- Had to add HTTPException import manually.

\- Fixed indentation errors multiple times.



This week focused on adding safety checks around AI calls — an important production practice.



\---



\## Project Structure

\- `rag\_app.py` - Main FastAPI application

\- `.env` - API keys (ignored)

\- `requirements.txt` - Dependencies



