#!/usr/bin/python3
"""
Write a script that lists all State objects
from the database hbtn_0e_6_usa
"""


if __name__ == "__main__":  # only execute when called "directly"
    from model_state import Base, State
    from sqlalchemy import create_engine, MetaData
    from sqlalchemy.orm import Session
    import sys

    user = sys.argv[1]  # mysql username
    passwrd = sys.argv[2]  # mysql password
    db = sys.argv[3]  # database name

    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(user, passwrd, db),
        pool_pre_ping=True)  # creating conection to database (hbtn_0e_6_usa)
    session = Session(engine)
    for state in session.query(State).order_by(State.id):
        print("{}: {}".format(state.id, state.name))
    session.close()
    #  state is the model mapped to the state table in the database
