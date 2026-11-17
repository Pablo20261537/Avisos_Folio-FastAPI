from sqlalchemy import create_engine
from sqlalchemy.orm import Session, declarative_base, sessionmaker
from urllib.parse import quote_plus
from config import DATABASE_URL_AVSF


engine_AVSF = create_engine(
    DATABASE_URL_AVSF,
    pool_pre_ping=True
)

SessionLocalAvsf = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine_AVSF
)

Base = declarative_base()

def get_db_avsf():
    db: Session = SessionLocalAvsf()

    try:
        yield db
    finally:
        db.close()              