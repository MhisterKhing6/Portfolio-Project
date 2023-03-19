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

@app.route("/withdrawal_info")
def withdrawal_info():
    if "number" in session_managment:
        withdrawal = None
        investor = storage.get_investor_by_number(session_managment["number"])
        if len(investor.withdrawal_info) != 0:
            withdrawal = investor.withdrawal_info[0]
        return render_template("withdrawal_info_page.html", winfo=withdrawal)
    else:
        return redirect(url_for('Main.login'))

@app.route("/bind_info", methods=["POST", "GET"])
def bind_info():
    if request.method == 'POST':
        if "number" in session_managment:
            number = request.form["number"]
            name = request.form["name"]
            confirm_number = request.form["cnumber"]
            fund_password = request.form['pass']
            confirm_fund_password = request.form['pass1']
            vendor = request.form['option']
            if len(number) < 10 or len(number) > 10:
                flash("Withdrawal number shouldn't contain country code and must be 10")
                return render_template("addWinfo.html")
            if number != confirm_number:
                flash("Tel Numbers dont match")
                return render_template("addWinfo.html")
            if len(fund_password) < 4:
                flash("Fund Password must contain at least 4 characters")
                return render_template("addWinfo.html")
            if confirm_fund_password != fund_password:
                flash("Fun passwords dont match")
                return render_template("addWinfo.html")
            investor = storage.get_investor_by_number(session_managment["number"])
            info = {"name": name, "investor_id": investor.id, "number_type": vendor, "number": session_managment["number"],"fund_password":fund_password}
            storage.add_winfo(session_managment["number"], info)
            return redirect(url_for("Main.withdrawal_info"))

        else:
            return redirect(url_for('Main.login'))
    else:
        return render_template('addWinfo.html')



