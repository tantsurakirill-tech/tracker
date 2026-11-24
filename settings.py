from dotenv import load_dotenv

import os

from sqlalchemy import create_engine, URL

from sqlalchemy.orm import sessionmaker

load_dotenv()

url = URL.create(drivername="postgresql+psycopg2", username=os.getenv("DB_USER"), password=os.getenv("DB_PASSWORD"),
                    host=os.getenv("DB_HOST"), port=os.getenv("DB_PORT"), database=os.getenv("DB_NAME"))

engine = create_engine(url)

Session = sessionmaker(bind=engine)