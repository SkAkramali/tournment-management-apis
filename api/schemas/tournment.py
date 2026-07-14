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


class TournamentUpdate(BaseModel):
  name: str | None = Field(default=None, max_length=50)
  sport: str | None = Field(default=None, max_length=50)
  season: str | None = Field(default=None, max_length=50)