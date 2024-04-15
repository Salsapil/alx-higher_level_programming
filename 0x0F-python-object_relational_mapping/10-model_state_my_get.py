#!/home/salsabil/alx-higher_level_programming/.venv/bin/python
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
    states = Session.query(State).filter(State.name == sys.argv[4]).first()
    if states:
        print("{}: {}".format(states.id))
    else:
        print("Nothing")
