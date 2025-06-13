from pydantic import BaseModel

class BrainstormRequest(BaseModel):
    topic: str
    tone: str
    audience: str
    video_type: str
