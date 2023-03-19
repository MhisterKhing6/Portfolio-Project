from flask import Flask, request,jsonify, url_for, redirect, flash, make_response
from flask import Blueprint, render_template
from api.run import session_managment
from api import app
from json import JSONDecoder
from Storage import storage
from Schemas.base import Common
from Schemas.vip import Vip
from Schemas.deposites import Deposit
from Schemas.pending import Pending
from Schemas.withdrawals import Withdrawal
from Schemas.deposites import Deposit
from Schemas.withdrawalinformation import WithdrawalInfo
from Schemas.Investor import Investor
from Schemas.deposit_pending import Deposit_pending
from Schemas.dposite_number import Deposits_numbers


@app.route("/deposit", methods=["POST", "GET"])
def deposit():
    if "number" in session_managment:
        investor = storage.get_investor_by_number(session_managment["number"])
        investor_vip = storage.get_vip_by_id(investor.vip)
        if request.method == 'POST':
                amount = int(request.form["amount"])
                vendor = request.form["option"]
                depsosite_number = storage.get_deposit_number(vendor)

                return render_template("deposite_completeform.html", investor=investor, investor_vip=investor_vip, deposit=depsosite_number, amount=amount)

        else:
            return render_template('deposit_amount.html', investor=investor, investor_vip=investor_vip)
    else:
        return redirect(url_for("Main.login"))

@app.route("/payed", methods=["POST"])
def payed():
    if "number" in session_managment:
        investor = storage.get_investor_by_number(session_managment["number"])
        amount = int(request.form["amount"])
        number = request.form["number"]
        trans = request.form["trans"]
        data = {"number": number, "amount": amount, "trans_id":trans, "investor_id" : investor.id}
        storage.depsoit_pending(data)
        return redirect(url_for('Main.pending_record'))


