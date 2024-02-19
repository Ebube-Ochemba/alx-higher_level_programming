#!/usr/bin/python3
"""
A script that lists all State objects that contain the letter a from the
database hbtn_0e_6_usa.
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

    s = '%a%'
    states = session.query(State).filter(State.name.like(s)).order_by(State.id)
    for state in states:
        print("{}: {}".format(state.id, state.name))

    session.close()
