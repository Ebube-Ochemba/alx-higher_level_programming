#!/usr/bin/python3
"""
A script that changes the name of a State object from the database
hbtn_0e_6_usa.
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

    state = session.query(State).filter_by(id=2).first()
    state.name = "New Mexico"

    session.commit()
    session.close()
