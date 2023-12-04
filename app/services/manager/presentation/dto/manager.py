from pydantic import BaseModel


class ManagerDTO(BaseModel):
    name: str
