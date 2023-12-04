from pydantic import BaseModel


class FundDTO(BaseModel):
    name: str
    start_year: int
    alias: str
    nationality: str
    manager: str
    companies: list
