from sqlalchemy import Column, ForeignKey, String, Numeric, Integer, Identity
from Schemas import Base
import uuid
from sqlalchemy.orm import relationship
from Schemas.base import Common
"""
Investor withdrawal from the system but has not been processed yet
"""


class Deposit_pending(Common, Base):
    """
    Investor withdrawal from the system but has not been processed yet
     Attributes
        ID : Unique id to identify the transaction
        Number : The number to received the transaction
        investor_id : The investor that initiated the transaction
        amount : amount withdrawn
        date : The date the transaction incurred

    """
    __tablename__ = "deposit_pending"
    investor_id = Column(Integer, ForeignKey("investors.id"), nullable=False)
    amount = Column(Numeric(10, 2), nullable=False)
    id = Column(Integer, autoincrement=True, primary_key=True)
    trans_id = Column(String(60), nullable=False)
    date = Column(String(60), nullable=False)
    number = Column(String(60), nullable=False)

    def __init__(self, *args, **kwargs):
        if kwargs:
            for key, value in kwargs.items():
                self.__setattr__(key, value)
