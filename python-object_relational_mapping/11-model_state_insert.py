#!/usr/bin/python3
""" Write a script that adds the State object
“Louisiana” to the database hbtn_0e_6_usa """

if __name__ == "__main__":
    from model_state import Base, State
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from sys import argv

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    new_state = State(name='Louisiana')
    session.add(new_state)  # save the new state through the session
    session.commit()  # commits ("uploads") the current session to the database
    print(new_state.id)

    session.close()
