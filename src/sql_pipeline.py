from src.llm import call_llm
from sqlalchemy import text
from src.db import SessionLocal
from src.interrogation import build_sql_prompt, generate_sql, SQL_SYSTEM_PROMPT
from src.execution import validate_sql, execute_sql

def summarize(rows, question):
    prompt = f"""
The SQL query returned these rows:
{rows}

provide a clear, concise answer to the question:
{question}
    """
    answer = call_llm(prompt)

    return answer


def answer_question(question: str, schema: str):

    prompt = build_sql_prompt(schema, question)

    sql = generate_sql(
        llm=lambda **kwargs: call_llm(
            prompt=kwargs["prompt"],
            system=kwargs.get("system", "")
        ),
        schema=schema,
        question=question
    )

    validate_sql(sql)

    if validate_sql:
        rows= execute_sql(sql)

        answer = summarize(rows, question)

        return {"sql": sql,
                "rows": rows,
                "answer": answer}