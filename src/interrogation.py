from src.db import Transaction
from sqlalchemy.inspection import inspect
from src.llm import call_sqlcoder

def get_schema():
    mapper = inspect(Transaction)
    lines = ["Table: Transactions", "Columns:"]
    for column in mapper.columns:
        lines.append(f"- {column.name} ({column.type})")
    return "\n".join(lines)


SQL_SYSTEM_PROMPT = """
You are an assistant that writes SQL queries for a SQLite database.

Rules:
- Use ONLY the tables and columns listed in the schema.
- Return ONLY SQL. No explanation, no markdown.
- Use simple SQL unless the question requires complexity.
- Use correct column names exactly as provided.
- If the question is ambiguous, choose the most reasonable interpretation.
"""

def build_sql_prompt(schema: str, question: str) -> str:
    return f"""
Write a SQL query.
Use only the tables and columns in the schema.
Do not invent tables or columns.
Return only SQL. No explanation, no comments, no markdown.
If the schema does not contain the required data, return:
The schema does not contain the required data.
Schema:
{schema}
Question:
{question}
SQL:
"""


def generate_sql(schema: str, question: str) -> str:

    prompt = build_sql_prompt(schema, question)

    response = call_sqlcoder(prompt)

    sql = response.strip()

    return sql