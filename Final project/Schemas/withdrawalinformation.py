from sqlalchemy import Column, ForeignKey, String, Numeric, Integer
from Schemas import Base
import uuid
from sqlalchemy.orm import relationship
from Schemas.base import Common

"""
Investor withdrawal from the system
 Attributes
    ID : Unique id to identify the withdrawal
    Number : The number that received the withdrawal
    investor_id : The investor that issued the withdrawal
    amount : amount withdrawal
    number_type: Vendor of number
"""

class WithdrawalInfo(Common, Base):
    __tablename__ = "withdrawal_information"
    id = Column(Integer, autoincrement=True, primary_key=True)
    investor_id = Column(Integer, ForeignKey("investors.id"), nullable=False)
    number_type = Column(String(10), nullable=False)
    number = Column(String(30), nullable=False)
    fund_password = Column(String(30), nullable=False)
    name = Column(String(70), nullable=False)

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            self.__setattr__(key, value)


