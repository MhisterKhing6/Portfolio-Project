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

@app.route("/records")
def records():
    if "number" in session_managment:
        investor = storage.get_investor_by_number(session_managment["number"])
        vip = storage.get_all_vip()
        investor_vip = storage.get_vip_by_id(investor.vip)
        return render_template("transaction_records.html", investor=investor, investor_vip=investor_vip)
    else:
        session_managment.pop("number")
        return redirect(url_for("Main.login"))

@app.route("/pending_record")
def pending_record():
    if "number" in session_managment:
        investor = storage.get_investor_by_number(session_managment["number"])
        vip = storage.get_all_vip()
        investor_vip = storage.get_vip_by_id(investor.vip)
        pendings = investor.pendings
        dpendings = investor.dpendings
        if len(pendings) == 0:
            pendings = None
        return render_template("pending_record.html", investor=investor, investor_vip=investor_vip, Wpendings=pendings, Dpendings=dpendings)
    else:
        session_managment.pop("number")
        return redirect(url_for("Main.login"))

@app.route("/deposit_record")
def deposit_record():
    if "number" in session_managment:
        investor = storage.get_investor_by_number(session_managment["number"])
        vip = storage.get_all_vip()
        investor_vip = storage.get_vip_by_id(investor.vip)
        deposit = investor.deposits
        if len(deposit) == 0:
            deposit = None
        return render_template("deposit_record.html", investor=investor, investor_vip=investor_vip, deposits=deposit)
    else:
        session_managment.pop("number")
        return redirect(url_for("Main.login"))

@app.route("/withdrawal_record")
def withdrawal_record():
    if "number" in session_managment:
        investor = storage.get_investor_by_number(session_managment["number"])
        vip = storage.get_all_vip()
        investor_vip = storage.get_vip_by_id(investor.vip)
        withdrawals = investor.withdrawals
        if len(withdrawals) == 0:
            withdrawal = None
        return render_template("withdrawal_record.html", investor=investor, investor_vip=investor_vip, withdrawals=withdrawals)
    else:
        session_managment.pop("number")
        return redirect(url_for("Main.login"))

@app.route("/team_record")
def team_record():
    if "number" in session_managment:
        investor = storage.get_investor_by_number(session_managment["number"])
        vip = storage.get_all_vip()
        teams = storage.get_teams(investor)
        investor_vip = storage.get_vip_by_id(investor.vip)
        if len(teams) == 0:
            teams = None
        return render_template("teams_record.html", investor=investor, investor_vip=investor_vip, teams=teams)
    else:
        session_managment.pop("number")
        return redirect(url_for("Main.login"))
