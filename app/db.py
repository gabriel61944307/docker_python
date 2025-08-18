# pylint: disable=C0114, C0115
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Configuração do banco de dados
DATABASE_URL = "postgresql+psycopg2://postgres:12345678@localhost:5432/postgres"

# Criação do engine
engine = create_engine(DATABASE_URL, echo=True)

# Criação da sessão
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base para classes ORM
Base = declarative_base()
