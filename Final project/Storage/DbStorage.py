from Schemas import Base
from Schemas.Investor import Investor
from Schemas.vip import Vip
from Schemas.withdrawalinformation import WithdrawalInfo
from Schemas.deposites import Deposit
from Schemas.withdrawals import Withdrawal
from Schemas.pending import Pending
from Schemas.deposit_pending import Deposit_pending
from Schemas.dposite_number import Deposits_numbers
from sqlalchemy import create_engine, Identity
from sqlalchemy.orm import sessionmaker, scoped_session
from datetime import datetime
from Schemas.admin import Admins


class Db_engine:
    """
    Creating the underlining engine to store the user information
    attributes:
        private engine which contains the engine
        private session which will contain the session

    """
    __engine = None
    __session = None

    def __init__(self):
        self.__engine = create_engine("mysql+mysqldb://root:root@localhost/test")
        Base.metadata.create_all(self.__engine)
        sess_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(sess_factory)
        self.__session = Session

    def get_all_vip(self):
        vips = self.__session.query(Vip)
        vt = [v for v in vips if v.id != "VIP0"]
        return vt
    def get_vip_by_id(self, id):
        return self.__session.query(Vip).filter(Vip.id == id).first()
    def get_deposit_number(self, vendor):
        return self.__session.query(Deposits_numbers).filter(Deposits_numbers.type == vendor).first()

    def create_investor(self, data):
        """
        Create a new Investor
        .Create an investor instance from data
        .Add teh instance to the database
        .Commit changes
        :param data: Contains the user information
        :return: None
        """

        investor = Investor(**data)
        self.__session.add(investor)
        self.__session.commit()
        return True

    def perform_task(self, id):
        """
        Update the balance of the user base on vip daily income
        .Get the Investor from the database on the investor id
            .if id doesn't give an investor from the database return false
        .Get the investor level of vip.
        .Add the vip daily income to the investor balance
        .Return True

        :param id: Investor id to update balance
        :return: true or false base on if the user perform the task correctly
        """

        investor = self.get_investor_by_id(id)
        if investor.vip == "VIP0":
            return 3
        vip = self.__session.query(Vip).filter(Vip.id == investor.vip).first()
        date = datetime.now()

        if date.isoweekday() != investor.current:
            investor.balance += vip.daily_income
            investor.daily_income += vip.daily_income
            investor.total_income += vip.daily_income
            investor.task_performed = True
            investor.current = date.isoweekday()
            self.__session.commit()
            return 1
        else:
            return 2
    def reject_from_pending(self, id, type):
        if type == 'W':
            trans =self.__session.query(Pending).filter(Pending.id == id).first()
            if trans:
                investor = self.__session().query(Investor).filter(Investor.id == trans.investor_id.firs).first()
                investor.balance += trans.amount
                trans.number = "R " + str(trans.number)
                data = {"date": trans.date, "number": trans.number, "investor_id": trans.investor_id, "amount":trans.amount}
                withdrawal = Withdrawal(**data)
                self.__session.add(withdrawal)
                self.__session.delete(trans)
                self.__session.commit()
                return True
            else:
                return False
        else:
            trans = self.__session.query(Deposit_pending).filter(Deposit_pending.id == id).first()
            if trans:
                investor = self.__session().query(Investor).filter(Investor.id == trans.investor_id).first()
                trans.number = "R" + str(trans.number)
                data = {"date": trans.date, "number": trans.number, "investor_id": trans.investor_id,
                        "amount": trans.amount, "trans_id": trans.trans_id}
                deposit = Deposit(**data)
                self.__session.add(deposit)
                self.__session.delete(trans)
                self.__session.commit()
                return True
            else:
                return False
    def accept_from_pending(self, id, type):
        if type == 'W':
            trans =self.__session.query(Pending).filter(Pending.id == id).first()
            if trans:
                investor = self.__session().query(Investor).filter(Investor.id == trans.investor_id).first()
                investor.balance -= trans.amount
                investor.total_withdrawal += trans.amount
                trans.number = "A " + str(trans.number)
                data = {"date": trans.date, "number": trans.number, "investor_id": trans.investor_id, "amount":trans.amount}
                withdrawal = Withdrawal(**data)
                self.__session.delete(trans)
                self.__session.add(withdrawal)
                self.__session.commit()
                return True
            else:
                return False
        else:
            trans = self.__session.query(Deposit_pending).filter(Deposit_pending.id == id).first()
            if trans:
                investor = self.__session().query(Investor).filter(Investor.id == trans.investor_id).first()
                trans.number = "A " + str(trans.number)
                investor.balance += trans.amount
                investor.total_deposit += trans.amount
                data = {"date": trans.date, "number": trans.number, "investor_id": trans.investor_id,
                        "amount": trans.amount, "trans_id": trans.trans_id}
                deposit = Deposit(**data)
                self.__session.add(deposit)
                self.__session.delete(trans)
                self.__session.commit()
                return True
            else:
                return False




    def get_all_deposite_pending(self):
        return self.__session().query(Deposit_pending).all()

    def get_all_withdrawal_pending(self):
        return self.__session().query(Pending).all()

    def add_admin(self, admin):
        self.__session.add(admin)
        self.__session.commit()

    def get_admin_by_number(self, number):
        return self.__session.query(Admins).filter(Admins.number == number).first()

    def upgrade_vip(self, id, vip_id):
        """
        Upgrade use Vip level
            .Get the Investor base on the vi
            .Get
        :param id: Investor id
        :return:
        Ruturn Codes:
            1: purchased
            2: Low balance
            False:The investor doesnt exist
        """
        investor = self.__session.query(Investor).filter(Investor.id == id).first()
        if investor:
            vip = self.__session.query(Vip).filter(Vip.id == vip_id).first()
            if investor.vip > vip_id:
                return 4
            if investor.vip == vip_id:
                return 3
            if vip:
                if investor.balance >= vip.price:
                    investor.balance -= vip.price
                    investor.vip = vip.id
                    superior = self.__session.query(Investor).filter(Investor.id == investor.super_id).first()
                    if superior:
                        superior.balance += vip.bonus
                else:
                    return 2
                self.__session.commit()
                return 1
            else:
                return 3



    def add_winfo(self, number, data):
        investor = self.get_investor_by_number(number)
        W_info = WithdrawalInfo(**data)
        wll = self.__session.query(WithdrawalInfo).filter(WithdrawalInfo.investor_id == investor.id).first()
        if wll:
            self.__session.delete(wll)
        self.__session.add(W_info)
        self.__session.commit()

    def pending_withdrawal(self, id, amount, pass1):
        """
        Withdraw from the Investor account.
         .Get the Investor by the ID
         .If the Investor id doesn't exist return false
         .If the investor vip level is at vip 0 withdrawal is not allowed return 1
         .if amount being withdrawn is greater than the total balance available return 2
         .else subtract the amount being withdrawn from the investor balance
         .create transaction and add it to the pending database
         .commit changes and add it to the database
        :param id: The investor id
        :param amount: The amount to withdraw
        :return: Integer base on specific output
        """
        investor = self.__session.query(Investor).filter(Investor.id == id).first()
        dt = datetime.now()
        date = dt.strftime("%m/%d/%Y")
        if investor:
            if investor.withdrawal_status > 0:
                return 1
            if investor.vip == "VIP0":
                return 2
            else:
                if investor.balance < amount:
                    return 3
                else:
                    investor.balance -= amount
                    with_info = investor.withdrawal_info[0]
                    if pass1 != with_info.fund_password:
                        return 5
                    transaction = Pending(id, amount, with_info.number, date)
                    investor.withdrawal_status = 15
                    self.__session.add(transaction)
                    self.__session.commit()
                    return 4

    def deposite(self, id, amount):
        investor = self.__session.query(Investor).filter(Investor.id == id).first()
        if investor:
            vip = self.__session.query(Vip).filter(Vip.id == investor.id)
            investor.balance += amount
            self.__session.commit()
            return True
        else:
            return False
    def depsoit_pending(self, data):
        dt = datetime.now()
        date = dt.strftime("%m/%d/%Y")
        data["date"] = date
        dpending = Deposit_pending(**data)
        self.__session.add(dpending)
        self.__session.commit()

    def remove_from_pending(self, id):
        transaction = self.__session.query(Pending).filter(Pending.id == id).first()
        if transaction:
            self.__session.remove(transaction)
            return True
        else:
            return False

    def get_investor_by_number(self, number):
        investor = self.__session.query(Investor).filter(Investor.number == number).first()
        if investor:
            return investor
        else:
            return False

    def get_investor_by_id(self, id):
        investor = self.__session.query(Investor).filter(Investor.id == id).first()
        if investor:
            return investor
        else:
            return False

    def change_password(self, number, pwd):
        self.get_investor_by_number(number).password = pwd
        self.__session.commit()

    def get_teams(self, investor):
        return self.__session.query(Investor).filter(Investor.super_id == investor.id).all()

