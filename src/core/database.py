from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlmodel import Session, SQLModel

from src.core.config import settings

engine = create_engine(str(settings.database_url), echo=True)


def create_db_and_tables():
    try:

        SQLModel.metadata.create_all(engine)
        print("Tablas creadas con éxito.")
    except Exception as e:
        print(f"Error al crear las tablas: {e}")


SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
    class_=Session,
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
