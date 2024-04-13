#!/usr/bin/python3
"""
A script that prints the first State object from the database hbtn_0e_6_usa
"""

import sqlalchemy
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":

    usrnm, psswd, dtbs = argv[1:]
    link = "mysql+mysqldb://{}:{}@localhost/{}".format(usrnm, psswd, dtbs)
    engine = create_engine(link)

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    first_state_query = session.query(State).order_by(State.id).first()
    if first_state_query is not None:
        print("{}: {}".format(first_state_query.id, first_state_query.name))
    else:
        print("Nothing")

    session.close()
