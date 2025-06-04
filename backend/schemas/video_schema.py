from pydantic import BaseModel


class VideoEditRequest(BaseModel):
    script: str
    video_path: str
