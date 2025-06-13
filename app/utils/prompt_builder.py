def build_prompt(topic: str, tone: str, audience: str, video_type: str) -> str:
    return (
        f"You're a social media strategist. Generate 5 creative, niche video content ideas for a '{video_type}' format. "
        f"The topic is '{topic}', with a '{tone}' tone, targeting '{audience}'. "
        f"Make sure each idea is unique, relevant to current trends, and written as a clear bullet point."
    )
