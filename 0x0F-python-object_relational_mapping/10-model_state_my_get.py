#!/usr/bin/python3
"""
A script that prints the State object with the name passed as argument from the
database hbtn_0e_6_usa.
"""

import sqlalchemy
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":

    usrnm, psswd, dtbs, st_nm = sys.argv[1:]
    link = "mysql+mysqldb://{}:{}@localhost/{}".format(usrnm, psswd, dtbs)
    engine = create_engine(link)

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    state = session.query(State).filter(State.name == st_nm).first()
    if state is not None:
        print(str(state.id))
    else:
        print("Not found")

    session.close()
