from datetime import datetime

from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

from sqlalchemy import String, ForeignKey



class Base(DeclarativeBase):
    pass


class Task(Base):
    __tablename__ = 'tasks'
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    deadline: Mapped[datetime | None]
    user_id: Mapped[int | None] = mapped_column(ForeignKey('users.id'))
    category_id: Mapped[int | None] = mapped_column(ForeignKey('categories.id'))
    priority: Mapped[str] = mapped_column(String(6), nullable=False, default='low')
    is_closed: Mapped[bool] = mapped_column(nullable=False, default=False)


class Category(Base):
    __tablename__ = 'categories'
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100), nullable=True)


class User(Base):
    __tablename__ = 'users'
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100), nullable=True)
    experience: Mapped[int] = mapped_column( nullable=True)
    is_blocked: Mapped[bool] = mapped_column(nullable=False, default=False)
