from fastapi import APIRouter
from pydantic import BaseModel

from ..services import platform_api

class PublishRequest(BaseModel):
    video_path: str

router = APIRouter()

@router.post("/")
def publish_video(payload: PublishRequest):
    url = platform_api.publish_to_platform(payload.video_path)
    return {"url": url}
