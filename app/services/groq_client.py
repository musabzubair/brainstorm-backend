import requests
from app.config import GROQ_API_KEY

API_URL = "https://api.groq.com/v1/chat/completions"
HEADERS = {
    "Authorization": f"Bearer {GROQ_API_KEY}",
    "Content-Type": "application/json",
}

def generate_ideas_with_groq(prompt: str) -> str:
    """
    Sends a prompt to the Groq API chat completion endpoint,
    and returns the generated text response.
    """
    payload = {
        "model": "mixtral-8x7b-chat",
        "messages": [{"role": "user", "content": prompt}],
    }

    response = requests.post(API_URL, headers=HEADERS, json=payload)
    response.raise_for_status()
    result = response.json()

    # Extract generated text from response
    return result["choices"][0]["message"]["content"]
