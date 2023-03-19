from sqlalchemy import Column, ForeignKey, String, Numeric, Integer, Identity,Boolean
from Schemas import Base
import uuid
from sqlalchemy.orm import relationship

from Schemas.deposites import Deposit
from Schemas.vip import Vip
from Schemas.withdrawalinformation import WithdrawalInfo
from Schemas.withdrawals import Withdrawal
from Schemas.pending import Pending
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


class Investor(Common, Base):
    __tablename__ = "investors"
    id = Column(Integer, Identity(start=40000, cycle=True), primary_key=True, autoincrement=True)
    number = Column(String(60), unique=True, nullable=False)
    super_id = Column(Integer, nullable=True)
    balance = Column(Numeric(10, 2), default=150)
    withdrawals = relationship("Withdrawal", backref="investor")
    deposits = relationship("Deposit", backref="investor")
    vip = Column(String(15), ForeignKey("vips.id"), default="VIP0")
    withdrawal_info = relationship("WithdrawalInfo", backref="investor")
    pendings = relationship("Pending", backref="pending", cascade="delete, all, delete-orphan")
    dpendings = relationship("Deposit_pending", backref="investor", cascade="delete, all, delete-orphan")
    password = Column(String(50), nullable=False)
    name = Column(String(100), nullable=False)
    task_performed = Column(Boolean, default=False)
    email = Column(String(100), nullable=False)
    total_income = Column(Numeric(10, 2), default=0)
    total_deposit = Column(Numeric(10, 2), default=0)
    total_withdrawal = Column(Numeric(10, 2), default=0)
    daily_income = Column(Numeric(10, 2), default=0)
    daily_team = Column(Numeric(10, 2), default=0)
    total_team = Column(Numeric(10, 2), default=0)
    current = Column(Integer, nullable=True)
    withdrawal_status = Column(Integer, default=0)





    def __init__(self, *args, **kwargs):
        if kwargs:
            for key, value in kwargs.items():
                self.__setattr__(key, value)


