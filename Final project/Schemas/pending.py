from sqlalchemy import Column, ForeignKey, String, Numeric, Integer, Identity
from Schemas import Base
import uuid
from sqlalchemy.orm import relationship
from Schemas.base import Common
"""
Investor withdrawal from the system but has not been processed yet
 Attributes
    ID : Unique id to identify the transaction
    Number : The number to received the transaction
    investor_id : The investor that initiated the transaction
    amount : amount withdrawn

"""


class Pending(Common,Base):
    __tablename__ = "pendings"
    investor_id = Column(Integer, ForeignKey("investors.id"), nullable=False)
    amount = Column(Numeric(10, 2), nullable=False)
    id = Column(Integer, autoincrement=True, primary_key=True)
    number = Column(String(60), nullable=False)
    date = Column(String(60), nullable=False)


    def __init__(self, id_t, amount_t,number_t , date_t):
        self.investor_id = id_t
        self.amount = amount_t
        self.date = date_t
        self.number = number_t



