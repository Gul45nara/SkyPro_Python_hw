from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


# Данные из вашего DBeaver
DB_USER = "postgres"
DB_PASSWORD = "gulnarochka45"
DB_HOST = "localhost"
DB_PORT = "5432"
DB_NAME = "postgres"

# Строка подключения
DATABASE_URL = (
    f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)

# Создаем движок и сессию
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
