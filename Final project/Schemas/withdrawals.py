from sqlalchemy import Column, ForeignKey, String, Numeric, Integer
from Schemas import Base
import uuid
from sqlalchemy.orm import relationship
from Schemas.base import Common
"""
Investor withdrawal from the system
 Attributes
    ID : Unique id to identify the withdrawal
    Number : The number that recieved the withdrawal
    investor_id : The investor that issued the withdrawal
    amount : amount withdrawal   
"""


class Withdrawal(Common, Base):
    __tablename__ = "withdrawals"
    id = Column(Integer, primary_key=True, autoincrement=True)
    investor_id = Column(Integer, ForeignKey("investors.id"), nullable=False)
    amount = Column(Numeric(10, 2), nullable=False)
    number = Column(String(30), nullable=False)
    date = Column(String(30), nullable=False)

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            self.__setattr__(key, value)


