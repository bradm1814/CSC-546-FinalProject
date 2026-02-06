from src.interrogation import get_schema
from src.sql_pipeline import answer_question

schema = get_schema()

import re

def clean_question(question: str) -> str:
    # Remove code fences and everything inside them
    question = re.sub(r"```.*?```", "", question, flags=re.DOTALL)

    # Remove Python function definitions
    question = re.sub(r"def\s+\w+\(.*?\):", "", question)

    # Remove imports
    question = re.sub(r"import\s+\w+", "", question)

    # Remove tracebacks
    if "Traceback" in question:
        question = question.split("Traceback")[0]

    # Remove HTML-like tags
    question = re.sub(r"<.*?>", "", question)

    return question.strip()

def main():

    while True:
        question = input("Ask a question about the data: ")

        question = clean_question(question)

        if question.lower() in ("exit", "quit"):
            break

        result = answer_question(question, schema)

        print("\n--- SQL Generated ---")
        print(result["sql"])

        print("\n--- Rows Returned ---")
        print(result["rows"])

        print("\n--- Answer ---")
        print(result["answer"])
        print("\n")

if __name__ == "__main__":
    main()
