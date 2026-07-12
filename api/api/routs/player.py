from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session

from core.database import get_db
from models.Player import Player
# Import both your creation schema and your response schema
from schemas.Players import PlayerCreate, PlayerResponse 

router = APIRouter(
    prefix="/player",
    tags=["player"]
)

@router.get("/", status_code=status.HTTP_200_OK, response_model=list[PlayerResponse])
def get_players(db: Session = Depends(get_db)) -> list[PlayerResponse]:
    players = db.query(Player).all()
    return players

@router.get("/{player_id}", status_code=status.HTTP_200_OK, response_model=PlayerResponse)
def get_player(player_id: int, db: Session = Depends(get_db)) -> PlayerResponse:
    player = db.query(Player).filter(Player.id == player_id).first()
    if not player:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail=f"Player with id {player_id} not found"
        )
    return player

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=PlayerResponse)
# FIX: Use PlayerCreate schema for incoming request payload validation
def create_player(player_in: PlayerCreate, db: Session = Depends(get_db)) -> PlayerResponse:
    # Convert Pydantic payload dictionary into a SQLAlchemy instance
    new_player = Player(**player_in.model_dump()) 
    
    db.add(new_player)
    db.commit()
    db.refresh(new_player)
    return new_player
