#!/usr/bin/python3
"""state Module"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":

    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost/{}".
        format(sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True,
    )
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    Session = Session()
    states = Session.query(State).filter(State.name.like("%a%")) \
        .order_by(State.id)
    for state in states:
        print("{}: {}".format(state.id, state.name))
