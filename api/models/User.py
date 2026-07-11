from core.database import Base
from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy import String


class User(Base):
  __tablename__  = "users"
  id: Mapped[int] = mapped_column(primary_key=True, index  = True)
  name: Mapped[str] = mapped_column(String(50), nullable = False)
  email: Mapped[str] = mapped_column(String(50), unique = True, index = True, nullable = False)
  password: Mapped[str] = mapped_column(String(50), nullable = False)
  role: Mapped[str] = mapped_column(String(50), nullable = False)