#!/usr/bin/python3
"""
Write a script that changes the name of a State
object from the database hbtn_0e_6_usa
"""

if __name__ == "__main__":
    from model_state import Base, State
    from sqlalchemy import create_engine
    from sqlalchemy.orm import Session
    from sys import argv

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
                            argv[1], argv[2], argv[3]), pool_pre_ping=True)

    session = Session(engine)
    
    state = session.query(State).filter(State.id == 2).first()
    state.name = 'New Mexico'

    session.commit()
    session.close()
