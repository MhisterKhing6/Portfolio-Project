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

@app.route("/shop")
def shop():
    if "number" in session_managment:
        investor = storage.get_investor_by_number(session_managment["number"])
        vip = storage.get_all_vip()
        investor_vip = storage.get_vip_by_id(investor.vip)
        return render_template("shops.html", investor=investor, vips=vip, investor_vip=investor_vip)
    else:
        return redirect(url_for('Main.login'))

@app.route("/purchase/<string:vip>")
def purchase(vip):
    if "number" in session_managment:
        number = session_managment["number"]
        investor = storage.get_investor_by_number(number)
        status = storage.upgrade_vip(investor.id, vip)
        if status == 4:
            flash("You already owns a higher shop")
            return redirect(url_for("Main.shop"))
        if status == 3:
            flash("You already owns the shop")
            return redirect(url_for("Main.shop"))
        if status == 2:
            flash("Your balance is low to purchase this shop")
            return redirect(url_for("Main.shop"))
        if status == 1:
            flash("Congratulations you are now shop {} owner".format(vip))
            return redirect(url_for("Main.shop"))
    else:
        return redirect(url_for("Main.login"))

