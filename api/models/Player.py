from api.core.database import Base
from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy import String
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

class Player(Base):
  __tablename__ = "players"

  id: Mapped[int] = mapped_column(primary_key=True)
  name: Mapped[str] = mapped_column(String(100), nullable=False)
  age: Mapped[int]

  role: Mapped[str] = mapped_column(
        String(50)
  )

  team_id: Mapped[int] = mapped_column(
        ForeignKey("teams.id")
  )

  team = relationship(
        "Team",
        back_populates="players"
  )