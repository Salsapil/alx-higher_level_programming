#!/usr/bin/python3
"""States Module"""

import sys
from relationship_city import Base, City
from relationship_state import State
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
    Session.add(City(name="San Francisco", state=State(name="California")))
    Session.commit()
