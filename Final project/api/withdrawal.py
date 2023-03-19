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


@app.route("/withdraw", methods=["POST", "GET"])
def withdraw():
    if "number" in session_managment:
        investor = storage.get_investor_by_number(session_managment["number"])
        investor_vip = storage.get_vip_by_id(investor.vip)
        with_info = None
        if len(investor.withdrawal_info) != 0:
            with_info = investor.withdrawal_info[0]

        if request.method == 'POST':
                amount = int(request.form["amount"])
                password = request.form["pass"]
                status = storage.pending_withdrawal(investor.id, amount, password)
                if status == 1:
                    flash("Sorry withdrawal is one per 15 days. You have {} days before the next withdrawal.".format(investor.withdrawal_status))
                    return render_template("withdrawalpage.html", with_info=with_info, investor=investor, investor_vip=investor_vip)
                if status == 2:
                    flash("Sorry Owners of shop Level 0 cant withdraw")
                    return render_template("withdrawalpage.html", with_info=with_info, investor=investor, investor_vip=investor_vip)
                if status == 5:
                    flash("Wrong Fund Password")
                    return render_template("withdrawalpage.html", with_info=with_info, investor=investor, investor_vip=investor_vip)
                if status == 3:
                    flash("Balance Low")
                    return render_template("withdrawalpage.html", with_info=with_info, investor=investor, investor_vip=investor_vip)
                return redirect(url_for("Main.pending_record"))

        else:
            return render_template('withdrawalpage.html', with_info=with_info, investor=investor, investor_vip=investor_vip)
    else:
        return redirect(url_for("Main.login"))



