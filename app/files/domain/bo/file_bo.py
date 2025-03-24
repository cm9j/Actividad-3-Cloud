from dataclasses import dataclass
from datetime import datetime


@dataclass
class FileBO:
    id: int | None = None
    filename: str = ""
    content_type: str = ""
    uploaded_at: datetime | None = None
