from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from schemas.tournment import TournamentCreate, TournamentResponse
from fastapi import HTTPException, status
from core.database import get_db
from models.Tournment import Tournament


router = APIRouter(
    prefix="/tournament",
    tags=["tournament"]
)


@router.post("/", status_code=201, response_model= TournamentResponse)
def create_tournament(tournament: TournamentCreate, db: Session = Depends(get_db)) -> TournamentResponse:
    db_tournament = Tournament(**tournament.dict())
    db.add(db_tournament)
    db.commit()
    db.refresh(db_tournament)
    return db_tournament

@router.get("/", status_code=200, response_model=list[TournamentResponse])
def get_tournaments(db: Session = Depends(get_db)) -> list[TournamentResponse]:
    tournaments = db.query(Tournament).all()
    return tournaments

@router.get("/{tournament_id}", status_code=200, response_model=TournamentResponse) 
def get_tournament(tournament_id: int, db: Session = Depends(get_db)) -> TournamentResponse:
  tournament = db.query(Tournament).filter(Tournament.id == tournament_id).first()
  if not tournament:
      raise HTTPException(status_code=404, detail="Tournament not found")
  return tournament