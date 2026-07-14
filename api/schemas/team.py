from pydantic import BaseModel


class TeamResponse(BaseModel):
  id: int
  name: str
  city: str
  tournament_id: int

class TeamCreate(BaseModel):
  name: str
  city: str
  tournament_id: int
