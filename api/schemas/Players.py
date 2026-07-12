from pydantic import BaseModel, ConfigDict

class PlayerResponse(BaseModel):
  model_config = ConfigDict(from_attributes=True)

  id: int
  name: str
  age: int
  role: str
  team_id: int


class PlayerCreate(BaseModel):
  name: str
  age: int
  role: str
  team_id: int