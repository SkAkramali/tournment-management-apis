from core.database import Base
from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy import ForeignKey

class Scorecard(Base):
  __tablename__ = "scorecards"

  id: Mapped[int] = mapped_column(primary_key=True)
  player_id: Mapped[int] = mapped_column(ForeignKey("players.id"), nullable=False)
  score: Mapped[int] = mapped_column(nullable=False)
  runs: Mapped[int] = mapped_column(nullable=False)
  balls: Mapped[int] = mapped_column(nullable=False)
  sixes: Mapped[int] = mapped_column(nullable=False)
  wickets: Mapped[int] = mapped_column(nullable=False)
  overs: Mapped[int] = mapped_column(nullable=False)
