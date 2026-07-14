from fastapi import FastAPI

from core.database import Base, engine
from api.routs.player import router as player_router
from api.routs.teams import router as team_router
from api.routs.tournment import router as tournment_router
# 1. IMPORT ALL DATABASE MODELS HERE SO SQLALCHEMY REGISTERS THEM
from models.Player import Player
from models.Team import Team          #  This registers the 'Team' table
from models.Scorecard import Scorecard
from models.Tournment import Tournament # (Check your filename spelling)
from models.User import User


Base.metadata.create_all(engine)

app = FastAPI()
app.include_router(player_router)
app.include_router(team_router)
app.include_router(tournment_router)