#!/usr/bin/python3
"""
A script that deletes all State objects with a name containing the letter a
from the database hbtn_0e_6_usa.
"""

import sqlalchemy
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":

    usrnm, psswd, dtbs = sys.argv[1:]
    link = "mysql+mysqldb://{}:{}@localhost/{}".format(usrnm, psswd, dtbs)
    engine = create_engine(link)

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    states = session.query(State).filter(State.name.like('%a%'))
    for state in states:
        session.delete(state)

    session.commit()
    session.close()
