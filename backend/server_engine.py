from sqlalchemy import create_engine, text
import os

DATABASE_URL = (
    f"postgresql+psycopg://"
    f"{os.getenv('DB_USER')}:"
    f"{os.getenv('DB_PASSWORD')}@"
    f"{os.getenv('DB_HOST')}:"
    f"{os.getenv('DB_PORT')}/"
    f"{os.getenv('DB_NAME')}"
)

engine = create_engine(
    DATABASE_URL,
    pool_pre_ping=True,
    echo=False
)


class Database:

    def query(self, sql: str, params: dict | None = None):

        with engine.connect() as conn:
            result = conn.execute(
                text(sql),
                params or {}
            )

            return [
                dict(row._mapping)
                for row in result
            ]

    def execute(self, sql: str, params: dict | None = None):

        with engine.begin() as conn:
            conn.execute(
                text(sql),
                params or {}
            )


clientes = db.query(
    """
    SELECT table_name 
    FROM information_schema.tables 
    WHERE table_schema = 'public' 
        AND table_type = 'BASE TABLE';
    """
)

print(clientes)