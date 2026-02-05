from sqlalchemy import text
from src.db import SessionLocal


def validate_sql(sql: str):
    lowered = sql.lower()

    if not lowered.startswith("select"):
        raise ValueError("Only SELECT statements are allowed")
    
    forbidden = ["insert", "update", "delete", "drop", "alter", "create"]

    if any(word in lowered for word in forbidden):
        raise ValueError("Unsafe SQL Detected")
    
    return True

def execute_sql(sql: str):
    session = SessionLocal()
    try:
        result = session.execute(text(sql))
        rows = result.fetchall()
        columns = result.keys()
        return [dict(zip(columns, row)) for row in rows]
    finally:
        session.close()

