from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String
from api.core.database import Base

class Tournament(Base):
  __tablename__ = "tournaments"
  id: Mapped[int] = mapped_columns(primary_key= True)
  name: Mapped[str] = mapped_column(String(50), nullable = False)
  sport: Mapped[str] = mapped_column(String(50), nullable = False)
  season: Mapped[str] = mapped_column(String(50), nullable = False)
