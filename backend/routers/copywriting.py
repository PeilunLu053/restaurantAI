from fastapi import APIRouter
from pydantic import BaseModel

from ..services import llm_generator

class CopyRequest(BaseModel):
    keywords: str
    tone: str = "friendly"

router = APIRouter()

@router.post("/")
def generate_copy(payload: CopyRequest):
    text = llm_generator.generate_promotional_copy(payload.keywords, payload.tone)
    return {"copy": text}
