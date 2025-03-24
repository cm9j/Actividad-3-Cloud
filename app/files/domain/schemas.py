from datetime import datetime

from pydantic import BaseModel


class FileResponse(BaseModel):
    id: int
    user_id: int
    filename: str
    uploaded_at: datetime
