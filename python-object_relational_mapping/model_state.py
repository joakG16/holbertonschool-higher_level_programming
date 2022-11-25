#!/usr/bin/python3
""" Write a python file that contains the class definition
of a State and an instance Base = declarative_base()
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
# Making use of the Declarative system or mapping, the components 
# of the user-defined class as well as the Table metadata to which 
# the class is mapped are defined at once


class State(Base):
    """ This class represents a state table in the database """
    __tablename__ = "states"
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
