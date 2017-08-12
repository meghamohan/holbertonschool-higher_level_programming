#!/usr/bin/python3
"""
script that prints the State object with the
 name passed as argument from the database hbtn_0e_6_usa
"""


import sys
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from model_state import Base, State

if __name__ == "__main__":
    usr = sys.argv[1]
    passwd = sys.argv[2]
    database = sys.argv[3]
    hostname = "localhost"
    port = 3306
    stateName = sys.argv[4]

    engine = create_engine('mysql+mysqldb://{}:{}@{}:{}/{}'.format(usr,
                                                                   passwd,
                                                                   hostname,
                                                                   port,
                                                                   database))
    Session = sessionmaker(bind=engine)
    session = Session()

    states = session.query(State).filter(State.name == stateName).first()
    if states:
        print(states.id)
    else:
        print("Not found")
    session.close()
