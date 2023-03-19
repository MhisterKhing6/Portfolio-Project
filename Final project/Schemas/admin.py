from sqlalchemy import Column, ForeignKey, String, Numeric, Integer, Identity,Boolean
from Schemas import Base
from Schemas.base import Common
"""
Define the investor
 Attributes
    ID : user id
    Number : user registered Number
    Superior ID : User invitor Id
    Balance : Amount Balance
    withdrwals : List of withdrawals
    pending_withdrawals : User current withdrawal not processed
    deposite : List of total amount deposited by the user
"""


class Admins(Common, Base):
    __tablename__ = "administrators"
    id = Column(Integer, Identity(start=40000, cycle=True), primary_key=True, autoincrement=True)
    number = Column(String(60), unique=True, nullable=False)
    name = Column(String(60), unique=True, nullable=False)
    password = Column(String(60), unique=True, nullable=False)





    def __init__(self, *args, **kwargs):
        if kwargs:
            for key, value in kwargs.items():
                self.__setattr__(key, value)


