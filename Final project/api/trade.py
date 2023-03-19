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

@app.route("/trade")
def trade():
    if "number" in session_managment:
        investor = storage.get_investor_by_number(session_managment["number"])
        vip = storage.get_all_vip()
        investor_vip = storage.get_vip_by_id(investor.vip)
        return render_template("trade.html", investor=investor, investor_vip=investor_vip)
    else:
        session_managment.pop("number")
        return redirect(url_for("Main.login"))

@app.route("/peform_trade")
def perform_trade():
    if "number" in session_managment:
        number = session_managment["number"]
        investor = storage.get_investor_by_number(number)
        status = storage.perform_task(investor.id)
        if status == 3:
            flash("Sorry Owners at shop level zero cant withdraw")
            return redirect(url_for("Main.trade"))
        if status == 2:
            flash("You have already traded  for the day")
            return redirect(url_for("Main.trade"))
        if status == 1:
            flash("Success")
            return redirect(url_for("Main.trade"))
    else:
        return redirect(url_for("Main.login"))