from src.db import Transaction
from sqlalchemy.inspection import inspect

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
    You are an assistant that writes SQL queries for a SQLite database.

Rules:
- Use ONLY the tables and columns listed in the schema.
- Do NOT invent tables or columns.
- If the schema does not contain the required data, respond exactly with:
  "The schema does not contain the required data."
- Return ONLY SQL. No explanation, no markdown.
- Use simple SQL unless the question requires complexity.
- Use correct column names exactly as provided.
- If the question is ambiguous, choose the most reasonable interpretation.

Schema:
{schema}

User Question:
{question}
"""


def generate_sql(llm, schema: str, question: str) -> str:
    prompt = build_sql_prompt(schema, question)

    response = llm(
        system=SQL_SYSTEM_PROMPT,
        prompt=prompt,
        max_tokens=300,
        temperature=0
    )

    sql = response.strip()

    if not sql.lower().startswith("select"):
        raise ValueError("Generated SQL does not start with SELECT statement")
    
    return sql