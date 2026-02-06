from sqlalchemy import Column, String, Float, Date, Integer, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker


Base = declarative_base() #declaritive base creates an Object Relation Mapping that allows the class that inherits it's properties to be represented as a table. It is the tie
                          #between Python and SQL turning Python type language into SQL language

class Transaction(Base):
    __tablename__ = "Transactions" #since Base is in there the Prices class knows that the created table is Prices

    id = Column(Integer, primary_key=True, autoincrement=True)


    DATAAREAID = Column(String)#declare date column. Works ensure unique values in rows but here it is paired with ticker to ensure only unique values between the two
    FSMAKEBUYDECISIONID = Column(String)# columns can have the same date, they can have the same ticker, but they can never have the same date and ticker simultaneously
    SORTINGID = Column(Integer)
    ProductionID = Column(String) 
    Hours = Column(Float) 
    Category = Column(String) 
    RouteID = Column(String) 
    NAME = Column(String) 
    PartCategory = Column(String)
    Lvl4FSDs = Column(Float)
    Lvl1FSDs = Column(Float)
    Ops = Column(Integer)
    OpsComplete = Column(Integer)
    ProductPool = Column(String)
    Cost = Column(Float)
    V_DIE_PURCHASE_COMPONENT = Column(Float)
    V_DIE_MSD_COST = Column(Float)
    V_DIE_LSD = Column(Float)
    V_DIE_MSD = Column(Float)
    V_DIE_FSD = Column(Float)
    V_DIE_COST = Column(Float)

engine = create_engine("sqlite:///data/mock_tmacs.db") #the engine effectively knows how to talk to the database. it executes the SQL that is derived from code
SessionLocal = sessionmaker(bind=engine)#this creates an object that when called makes engages the engine to make a connection to the database and do work

def init_db():
    """
    This function creates a table instance of all ORM models. 
    if the tables already existed it would not overwrite them, only creating any new tables that were added
    """
    Base.metadata.create_all(engine)


