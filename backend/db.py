# backend/db.py
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base

# URL do banco. Pega do ambiente (docker-compose já passa essa variável)
DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql+psycopg2://dietask:dietask@localhost:5432/dietask"
)

# Engine = "motor" de conexão com o Postgres
engine = create_engine(DATABASE_URL, echo=False, future=True)

# Base = classe-mãe dos modelos (tabelas)
Base = declarative_base()