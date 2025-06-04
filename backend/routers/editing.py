from fastapi import APIRouter
from pydantic import BaseModel

from ..services import ai_editor

class EditRequest(BaseModel):
    script: str
    video_path: str

router = APIRouter()

@router.post("/")
def edit_video(payload: EditRequest):
    result = ai_editor.automate_editing(payload.video_path, payload.script)
    return {"output": result}
