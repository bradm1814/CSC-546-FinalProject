from src.llm import call_mistral
from sqlalchemy import text
from src.db import SessionLocal
from src.interrogation import build_sql_prompt, generate_sql, SQL_SYSTEM_PROMPT
from src.execution import validate_sql, execute_sql

def summarize(rows, question, sql):
    prompt = f"""
You are summarizing the result of a SQL query.

SQL:
{sql}

Rows:
{rows}

Question:
{question}

Write a short, direct answer using ONLY the rows above.
Do not speculate. Do not contradict the SQL.

    """
    answer = call_mistral(prompt)

    return answer


def answer_question(question: str, schema: str):

    sql = generate_sql(schema, question)

    print(sql)

    if validate_sql(sql):
        rows = execute_sql(sql)
        answer = summarize(rows, question, sql)

        return {
            "sql": sql,
            "rows": rows,
            "answer": answer
        }
