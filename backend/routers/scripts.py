from fastapi import APIRouter
from pydantic import BaseModel

from ..services import llm_generator

class ScriptRequest(BaseModel):
    idea: str

router = APIRouter()

@router.post("/")
def generate_script(payload: ScriptRequest):
    script = llm_generator.generate_video_script(payload.idea)
    return {"script": script}
