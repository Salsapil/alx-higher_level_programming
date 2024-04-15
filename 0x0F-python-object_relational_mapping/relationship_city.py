#!/usr/bin/python3
"""state Module"""

from sqlalchemy import Column, Integer, String
from model_state import Base


class City(Base):
    """city Class"""

    __tablename__ = "cities"
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, nullable=False, foreign_key=True)
