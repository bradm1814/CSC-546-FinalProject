from src.interrogation import get_schema
from src.sql_pipeline import answer_question

schema = get_schema()
def main():

    while True:
        question = input("Ask a question about the data: ")

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
