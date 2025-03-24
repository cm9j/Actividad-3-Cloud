from dataclasses import dataclass


@dataclass
class UserBO:
    id: int | None = None
    email: str = ""
    password: str = ""
    external_id: int | None = None
