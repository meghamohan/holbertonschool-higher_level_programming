#!/usr/bin/python3
"""
script that adds the State object "Louisiana" to the database hbtn_0e_6_usa
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

    engine = create_engine('mysql+mysqldb://{}:{}@{}:{}/{}'.format(usr,
                                                                   passwd,
                                                                   hostname,
                                                                   port,
                                                                   database))
    Session = sessionmaker(bind=engine)
    session = Session()

    session.add(State(name="Louisiana"))
    session.commit()
    LouisianaId = session.query(State).filter(State.name == "Louisiana")\
                                      .order_by(State.id.desc()).first()
    print(LouisianaId.id)
    session.close()
