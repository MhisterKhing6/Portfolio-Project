from sqlalchemy import Column, ForeignKey, String, Numeric,  Integer
from Schemas import Base
from Schemas.base import Common
import uuid
from sqlalchemy.orm import relationship


"""
Investor withdrawal from the system
 Attributes
    ID : Unique id to identify the Deposits
    Number : Number Use for Deposits
    investor_id : The investor that issued the withdrawal
    amount : Amount Deposited

"""


class Deposits_numbers(Common, Base):
    __tablename__ = "deposit_numbers"
    id = Column(Integer, primary_key=True, autoincrement=True)
    type = Column(String(10), nullable=False)
    name = Column(String(60), nullable=False)
    number = Column(String(30), nullable=False)


    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            self.__setattr__(key, value)
