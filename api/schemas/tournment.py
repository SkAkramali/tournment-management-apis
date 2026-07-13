from pydantic import BaseModel, Field

class TournamentResponse(BaseModel):
  id: int
  name: str
  sport: str
  season: str


class TournamentCreate(BaseModel):
  name: str = Field(..., max_length=50)
  sport: str = Field(..., max_length=50)
  season: str = Field(..., max_length=50)
