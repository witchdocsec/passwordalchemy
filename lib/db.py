#imports
from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.orm import sessionmaker, declarative_base
from os.path import exists
from os import mkdir
from contextlib import contextmanager

#sql alchemy base for tables to inherit from
Base = declarative_base()

# Ensure the directory for the database exists
if not exists("db"):
    mkdir("db")

# Define the Password model
class Password(Base):
    __tablename__ = "Password"
    domain = Column("domain", String, primary_key=True)
    ccred = Column("ccred", String)
    
    def __init__(self, domain, ccred):
        self.domain = domain
        self.ccred = ccred
   

# Database setup
engine = create_engine("sqlite:///db/creds.db")
Base.metadata.create_all(bind=engine)

Session = sessionmaker(bind=engine)

#manage context
@contextmanager
def get_session():
    session = Session()
    try:
        yield session
        session.commit()
    except Exception as e:
        session.rollback()
        print(f"Database error: {e}")
    finally:
        session.close()

#store credential
def store(domain,ccred):
    p = Password(domain,ccred)
    with get_session() as session:
        try:
            session.add(p)
            return "Stored credential"
        except Exception as e:
            return "Error storing password: {e}"

#load credemtial
def fetch(domain):
	#with context manager
    with get_session() as session:

    	#query passwords by domain
        p = session.query(Password).filter(Password.domain == domain).first()

        #if one is found
        if p:
        	return p.ccred

        #error
        else:
            return f"No cred found for '{domain}'"
def fetchall():
	#with context manager
    with get_session() as session:

    	#query passwords by domain
        p = session.query(Password)

        #if one is found
        if p:
        	return p

        #error
        else:
            return "No creds found"
#load credemtial
def update(domain,ccred):
	#with context manager
    with get_session() as session:

    	#query passwords by domain
        p = session.query(Password).filter(Password.domain == domain).first()

        #if one is found
        if p:
        	p.ccred=ccred
        	return "updated credential"

        #error
        else:
            return f"No cred found for '{domain}'"