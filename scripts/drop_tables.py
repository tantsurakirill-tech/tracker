from models import Base

from settings import engine


Base.metadata.drop_all(engine)