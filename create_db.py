from src.db import SessionLocal, Transaction, init_db

import pandas as pd


def create_SQL_from_data():

    #read in csv
    df = pd.read_csv(r"data\mock_tmacs.csv")

    #create SQL session
    session = SessionLocal()

    session.bulk_insert_mappings(
        Transaction,
        df.to_dict(orient="records")
    )
    session.commit()
    session.close()

if __name__ == "__main__":

    init_db()
    create_SQL_from_data()


            




