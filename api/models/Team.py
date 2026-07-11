from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from sqlalchemy import String
from sqlalchemy import ForeignKey

from api.core.database import Base


class Team(Base):

  __tablename__ = "teams"

  id: Mapped[int] = mapped_column(primary_key=True)

  name: Mapped[str] = mapped_column(
        String(100)
  )

  city: Mapped[str] = mapped_column(
        String(100)
    )

  tournament_id: Mapped[int] = mapped_column(
        ForeignKey("tournaments.id")
    )

  tournament = relationship(
        "Tournament",
        back_populates="teams"
    )
  players = relationship(
    "Player",
    back_populates="team"
  )