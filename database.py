from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "postgresql://admin:e7ua9juxJnVoclzo6v2cwBBP9Aw3NJIJ@dpg-ct3f1cjtq21c738r8de0-a.frankfurt-postgres.render.com/edb_2hli"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
