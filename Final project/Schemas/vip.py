from sqlalchemy import Column, ForeignKey, String, Numeric
from Schemas import Base
import uuid
from sqlalchemy.orm import relationship



class Vip(Base):
    """
    Level of Vips and incomes
     Attributes
        id : Name of the vip level
        price: The price to purchase the vip
        daily_income : The amount the vip will generate each day
        daily_bonus : The daily profit the user will receive each day

    """

    __tablename__ = "vips"
    id = Column(String(60), primary_key=True)
    price = Column(Numeric(10, 2), nullable=False)
    yearly = Column(Numeric(10, 2), nullable=False)
    daily_income = Column(Numeric(10, 2), nullable=False)
    bonus = Column(Numeric(10, 2), nullable=False)
    image_name = Column(String(70), nullable=False)
    trade_type = Column(String(70), nullable=False)


    def __init__(self, id_t, amount_t, daily_income_t):
        self.id = id_t
        self.price = amount_t
        self.daily_income = daily_income_t


