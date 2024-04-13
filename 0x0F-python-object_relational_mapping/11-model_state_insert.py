#!/usr/bin/python3
"""
A script that adds the State object “Louisiana” to the database hbtn_0e_6_usa.
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

    new_state = State(name='Louisiana')
    session.add(new_state)

    state = session.query(State).filter_by(name='Louisiana').first()
    print(str(state.id))

    session.commit()
    session.close()
