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


class Deposit(Common, Base):
    __tablename__ = "deposits"
    id = Column(Integer, primary_key=True, autoincrement=True)
    investor_id = Column(Integer, ForeignKey("investors.id"), nullable=False)
    amount = Column(Numeric(10, 2), nullable=False)
    number = Column(String(30), nullable=False)
    date = Column(String(60), nullable=False)
    trans_id = Column(String(60), nullable=True)


    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            self.__setattr__(key, value)
