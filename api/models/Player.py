from core.database import Base
from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship


class Player(Base):
    __tablename__ = "players"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    age: Mapped[int] = mapped_column(nullable=False)

    role: Mapped[str] = mapped_column(String(50))

    team_id: Mapped[int] = mapped_column(ForeignKey("teams.id"))

    team = relationship(
        "Team",
        back_populates="players",
    )