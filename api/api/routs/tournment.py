from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy import select
from sqlalchemy.orm import Session

from core.database import get_db
from models.Tournment import Tournament
from schemas.tournment import (
    TournamentCreate,
    TournamentUpdate,
    TournamentResponse,
)
from schemas.team import TeamResponse

router = APIRouter(
    prefix="/tournament",
    tags=["Tournament"],
)


# Create Tournament
@router.post(
    "/",
    status_code=status.HTTP_201_CREATED,
    response_model=TournamentResponse,
)
def create_tournament(
    tournament: TournamentCreate,
    db: Session = Depends(get_db),
):
    db_tournament = Tournament(**tournament.model_dump())

    db.add(db_tournament)
    db.commit()
    db.refresh(db_tournament)

    return db_tournament


# Get All Tournaments
@router.get(
    "/",
    response_model=list[TournamentResponse],
)
def get_tournaments(
    db: Session = Depends(get_db),
):
    stmt = select(Tournament)

    tournaments = db.execute(stmt).scalars().all()

    return tournaments


# Get Tournament By ID
@router.get(
    "/{tournament_id}",
    response_model=TournamentResponse,
)
def get_tournament(
    tournament_id: int,
    db: Session = Depends(get_db),
):
    stmt = (
        select(Tournament)
        .where(Tournament.id == tournament_id)
    )

    tournament = db.execute(stmt).scalar_one_or_none()

    if tournament is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Tournament not found",
        )

    return tournament


# Update Tournament
@router.put(
    "/{tournament_id}",
    response_model=TournamentResponse,
)
def update_tournament(
    tournament_id: int,
    tournament_update: TournamentUpdate,
    db: Session = Depends(get_db),
):
    stmt = (
        select(Tournament)
        .where(Tournament.id == tournament_id)
    )

    tournament = db.execute(stmt).scalar_one_or_none()

    if tournament is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Tournament not found",
        )

    update_data = tournament_update.model_dump(exclude_unset=True)

    for key, value in update_data.items():
        setattr(tournament, key, value)

    db.commit()
    db.refresh(tournament)

    return tournament


# Delete Tournament
@router.delete(
    "/{tournament_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
def delete_tournament(
    tournament_id: int,
    db: Session = Depends(get_db),
):
    stmt = (
        select(Tournament)
        .where(Tournament.id == tournament_id)
    )

    tournament = db.execute(stmt).scalar_one_or_none()

    if tournament is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Tournament not found",
        )

    db.delete(tournament)
    db.commit()


# Get Teams of a Tournament
@router.get(
    "/{tournament_id}/teams",
    response_model=list[TeamResponse],
)
def get_tournament_teams(
    tournament_id: int,
    db: Session = Depends(get_db),
):
    stmt = (
        select(Tournament)
        .where(Tournament.id == tournament_id)
    )

    tournament = db.execute(stmt).scalar_one_or_none()

    if tournament is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Tournament not found",
        )

    return tournament.teams