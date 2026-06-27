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

