from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

@app.get("/")
def home():
    return {"message": "AI Decision Assistant is running!"}

@app.get("/ask-ai")
def ask_ai(question: str):

    response = client.chat.completions.create(
        model="gpt-5.5",
        messages=[
    {
        "role": "system",
        "content": """
        You are a highly intelligent AI Decision Assistant.

Your goal is to help users make smart decisions.

Always provide:
- Pros
- Cons
- Risks
- Recommendation
- Short explanation

Be analytical and realistic.

Do not give generic advice.

Consider:
- Budget
- Long-term effects
- Risk level
- Emotional factors
- Financial factors

Use clear formatting.
        """
    },

    {
        "role": "user",
        "content": question
    }
]
    )

    answer = response.choices[0].message.content

    return {"answer": answer}