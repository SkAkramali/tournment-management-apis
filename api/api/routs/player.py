from unittest import result

from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session

from core.database import get_db
from models.Player import Player
from schemas.Players import PlayerCreate, PlayerResponse 
from sqlalchemy import select
router = APIRouter(
    prefix="/player",
    tags=["player"]
)

@router.get("/", status_code=status.HTTP_200_OK, response_model=list[PlayerResponse])
def get_players(db: Session = Depends(get_db)) -> list[PlayerResponse]:
    stmt = select(Player)
    result = db.execute(stmt).scalars().all()
    return result

@router.get("/sample", status_code=status.HTTP_200_OK)
def get_sample(db: Session = Depends(get_db)) -> list[PlayerResponse]:
  stmt = select(Player)
  result = db.execute(stmt).scalars().all()
  print(result)
  return result

@router.get("/{player_id}", status_code=status.HTTP_200_OK, response_model=PlayerResponse)
def get_player(player_id: int, db: Session = Depends(get_db)) -> PlayerResponse:
   stmt = select(Player).where(Player.id == player_id)
   result = db.execute(stmt).scalar_one_or_none()
   if result is None: 
    raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail={"message": "Player with Provided id not found"})
   return result

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=PlayerResponse)
def create_player(player_in: PlayerCreate, db: Session = Depends(get_db)) -> PlayerResponse:
    new_player = Player(**player_in.model_dump()) 
    db.add(new_player)
    db.commit()
    db.refresh(new_player)
    return new_player

@router.put("/{player_id}", status_code=status.HTTP_200_OK, response_model=PlayerResponse)
def update_player(player_id: int, player_in: PlayerCreate, db: Session = Depends(get_db)) -> PlayerResponse:
    stmt = select(Player).where(Player.id == player_id)
    result = db.execute(stmt).scalar_one_or_none()
    if result is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail={"message": "Player with Provided id not found"})
    for key, value in player_in.model_dump().items():
        setattr(result, key, value)
    db.commit()
    db.refresh(result)
    return result

@router.delete("/{player_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_player(player_id: int, db: Session = Depends(get_db)):
   stmt = select(Player).where(Player.id == player_id) 
   result = db.execute(stmt).scalar_one_or_none()
   if result is None:
       raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail={"message": "Player with Provided id not found"})
   db.delete(result)
   db.commit()