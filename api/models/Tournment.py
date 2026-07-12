from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String
from core.database import Base

class Tournament(Base):
  __tablename__ = "tournaments"
  id: Mapped[int] = mapped_column(primary_key= True)
  name: Mapped[str] = mapped_column(String(50), nullable = False)
  sport: Mapped[str] = mapped_column(String(50), nullable = False)
  season: Mapped[str] = mapped_column(String(50), nullable = False)
  teams = relationship(
      "Team",
      back_populates="tournament"
  )