from sqlalchemy import Column, String, Float, Date, Integer, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker


Base = declarative_base() #declaritive base creates an Object Relation Mapping that allows the class that inherits it's properties to be represented as a table. It is the tie
                          #between Python and SQL turning Python type language into SQL language

class Transaction(Base):
    __tablename__ = "Transactions" #since Base is in there the Prices class knows that the created table is Prices

    sale_id = Column(String, primary_key = True)#declare date column. Works ensure unique values in rows but here it is paired with ticker to ensure only unique values between the two
    order_id = Column(String, primary_key = True)# columns can have the same date, they can have the same ticker, but they can never have the same date and ticker simultaneously
    sale_date = Column(String) 
    channel = Column(String) 
    quantity = Column(Integer) 
    unit_price = Column(Float) 
    net_revenue = Column(Float) 
    sku_id = Column(String) 
    product_name = Column(String)
    category = Column(String)
    sub_category = Column(String)
    brand = Column(String)
    supplier_id = Column(String)
    supplier_name = Column(String)
    region = Column(String)


engine = create_engine("sqlite:///data/supplier_transactions.db") #the engine effectively knows how to talk to the database. it executes the SQL that is derived from code
SessionLocal = sessionmaker(bind=engine)#this creates an object that when called makes engages the engine to make a connection to the database and do work

def init_db():
    """
    This function creates a table instance of all ORM models. 
    if the tables already existed it would not overwrite them, only creating any new tables that were added
    """
    Base.metadata.create_all(engine)


