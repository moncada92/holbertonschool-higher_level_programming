#!/usr/bin/python3
"""
create table states with ORM
"""

from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class City(Base):
    """City Class"""
    __tablename__ = 'cities'

    id = Column(Integer, autoincrement=True, primary_key=True,
                nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
