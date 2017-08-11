#!/usr/bin/python3
"""
contains the class definition of a State and
 an instance Base = declarative_base():
"""
from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class State(Base):
    """
    class that defines state table properties
    """
    __tablename__ = "states"
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=Flase)
