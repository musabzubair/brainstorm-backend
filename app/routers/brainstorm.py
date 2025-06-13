from fastapi import APIRouter
from models.schema import BrainstormRequest
import os
import requests

router = APIRouter()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
API_URL = "https://api.groq.com/openai/v1/chat/completions"

headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {GROQ_API_KEY}"
}

def build_prompt(topic: str, tone: str, audience: str, video_type: str) -> str:
    return (
        f"Generate 5 unique and creative niche content ideas for {video_type} videos. "
        f"The topic is '{topic}', the tone should be '{tone}', and the target audience is '{audience}'. "
        f"Make sure the ideas are engaging and trend-aware."
    )

def query_groq(prompt: str):
    payload = {
        "model": "meta-llama/llama-4-scout-17b-16e-instruct",
        "messages": [
            {"role": "user", "content": prompt}
        ]
    }
    response = requests.post(API_URL, headers=headers, json=payload)
    response.raise_for_status()
    data = response.json()
    
    # Extract generated text from Groq response structure
    # Usually: data['choices'][0]['message']['content']
    return data["choices"][0]["message"]["content"]

@router.post("/")
async def generate_ideas(request: BrainstormRequest):
    prompt = build_prompt(request.topic, request.tone, request.audience, request.video_type)
    try:
        result = query_groq(prompt)
        ideas = [idea.strip() for idea in result.split("\n") if idea.strip()]
        return {"ideas": ideas[:5]}  # Return top 5 ideas

    except Exception as e:
        return {"error": str(e)}
