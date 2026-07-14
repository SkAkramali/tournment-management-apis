from core.database import Base
from sqlalchemy.orm import mapped_column, Mapped
from fastapi import APIRouter, Depends, HTTPException
from schemas.team import TeamCreate, TeamResponse
from sqlalchemy.orm import Session
from core.database import get_db
from models.Team import Team
from sqlalchemy import select

router = APIRouter(
  prefix="/teams",
  tags=["teams"]
)

@router.get("/", status_code=200, response_model=list[TeamResponse])
def get_teams(db: Session = Depends(get_db)) -> list[TeamResponse]:
  stmt = select(Team)
  teams = db.execute(stmt).scalars().all()
  return teams


@router.get("/{team_id}", status_code=200, response_model=TeamResponse)
def get_team(team_id: int, db: Session = Depends(get_db)) -> TeamResponse:
   stmt = select(Team).where(Team.id == team_id)
   team = db.execute(stmt).scalar_one_or_none()
   if not team:
      raise HTTPException(status_code=404, detail="Team not found")
   
   return team

@router.post("/", status_code=201, response_model=TeamResponse)
def create_team(team: TeamCreate, db: Session = Depends(get_db)) -> TeamResponse:
  db_team = Team(**team.dict())
  db.add(db_team)
  db.commit()
  db.refresh(db_team)
  return db_team

@router.delete("/{team_id}", status_code=204) 
def delete_team(team_id: int, db: Session = Depends(get_db)):
  stmt  = select(Team).where(Team.id == team_id)
  team = db.execute(stmt).scalar_one_or_none()
  if not team:
    raise HTTPException(status_code=404, detail="Team not found")
  db.delete(team)
  db.commit()


@router.put("/updateDetails/", response_model=TeamResponse, status_code=200) 
def upadate_details(team: TeamResponse, db: Session = Depends(get_db)) -> TeamResponse:
  stmt = select(Team).where(Team.id == team.id)
  db_team = db.execute(stmt).scalar_one_or_none()
  if not db_team:
    raise HTTPException(status_code=404, detail="Team not found")
  for key, value in team.dict().items():
    setattr(db_team, key, value)
  db.commit()
  db.refresh(db_team)
  return db_team