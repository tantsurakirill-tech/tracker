from datetime import datetime

from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

from sqlalchemy import String, ForeignKey



class Base(DeclarativeBase):
    pass


class Tasks(Base):
    __tablename__ = 'task'
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(nullable=True)
    deadline: Mapped[datetime] = mapped_column(nullable=True)
    user_id: Mapped[int] = mapped_column(ForeignKey('user.id'))
    category_id: Mapped[int] = mapped_column(ForeignKey('category.id'))


class Categories(Base):
    __tablename__ = 'categories'
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(nullable=True)


class User(Base):
    __tablename__ = 'user'
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100), nullable=True)
    experience: Mapped[int] = mapped_column( nullable=True)

