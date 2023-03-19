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

@app.route("/profile")
def profile():
    if "number" in session_managment:
        investor = storage.get_investor_by_number(session_managment["number"])
        vip = storage.get_all_vip()
        investor_vip = storage.get_vip_by_id(investor.vip)
        return render_template("profile.html", investor=investor, investor_vip=investor_vip)
    else:
        session_managment.pop("number")
        return redirect(url_for('Main.login'))

@app.route("/customer_service")
def customer_service():
    if "number" in session_managment:
        return render_template("contact_us.html")
    else:
        session_managment.pop("number")
        return redirect(url_for('Main.login'))
@app.route("/invite")
def invite():
    if "number" in session_managment:
        investor = storage.get_investor_by_number(session_managment["number"])
        vip = storage.get_all_vip()
        investor_vip = storage.get_vip_by_id(investor.vip)
        return render_template("invite.html", investor=investor, investor_vip=investor_vip)
    else:
        session_managment.pop("number")
        return redirect(url_for("Main.login"))

@app.route("/notice")
def notice():
    vip = storage.get_all_vip()
    return render_template("notice.html", vips=vip)


