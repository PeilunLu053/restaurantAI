from fastapi import APIRouter
from pydantic import BaseModel

from ..services import platform_api

class FeedbackRequest(BaseModel):
    url: str

router = APIRouter()

@router.post("/")
def get_feedback(payload: FeedbackRequest):
    data = platform_api.fetch_performance(payload.url)
    return data
