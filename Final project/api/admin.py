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
from Schemas.admin import Admins


@app.route("/admin_page")
def admin_page():
    """if "number" in session_managment:
        investor = storage.get_investor_by_number(session_managment["number"])
        vip = storage.get_all_vip()
        teams = storage.get_teams(investor)
        investor_vip = storage.get_vip_by_id(investor.vip)
        if len(teams) == 0:
            teams = None
        return render_template("teams_record.html", investor=investor, investor_vip=investor_vip, teams=teams)
    else:
        session_managment.pop("number")
        return redirect(url_for("Main.login"))"""
    return render_template("admin_pag.html")


@app.route("/admin_login", methods=["GET", "POST"])
def admin_login():
    """
        Check for validation
        :return:
        """
    if request.method == "POST":
        number = request.form["number"]
        password = request.form['pass']
        admin = storage.get_admin_by_number(number)
        if admin:
            if admin.password == password:
                session_managment["admin_number"] = number
                return redirect(url_for('Main.admin_page'))
            else:
                flash("Wrong Password")
                return render_template("admin_login.html")
        else:
            flash("Admin not found.")
            return render_template("admin_login.html")
    else:
        if "admin_number" in session_managment:
            return redirect(url_for("Main.admin_page"))
        return render_template("admin_login.html")


@app.route("/reset_fund", methods=["GET", "POST"])
def reset_fund():
    if request.method == "POST":
        number = request.form["number"]
        v = Investor()
        user = storage.get_investor_by_number(number)
        if len(user.withdrawal_info) != 0:
            user = user.withdrawal_info[0]
            return render_template("reset_fund.html", user=user, number=number)
        else:
            flash('The user has not bind any withdrawal information')
            return render_template("reset_fund.html")
    else:
        return render_template("reset_fund.html")

@app.route("/dep_clearing")
def deposit_clear():
    deposites = storage.get_all_deposite_pending()
    initial = None
    total = len(deposites)
    if total != 0:
        initial = deposites[0]
    return render_template("clear_deposite.html", initial=initial, total=total)

@app.route("/rej_clearing")
def withdrawal_clear():
    withdrwals = storage.get_all_withdrawal_pending()
    initial = None
    total = len(withdrwals)
    if total != 0:
        initial = withdrwals[0]
    return render_template("clear_withdrawal.html", initial=initial, total=total)


@app.route("/reject_deposit/<int:id>")
def reject_deposit(id):
    status = storage.reject_from_pending(id, "D")
    if status:
        flash("Operation Completed")
        return redirect(url_for("Main.deposit_clear"))
    else:
        return redirect(url_for("Main.deposit_clear"))

@app.route('/accept_deposit/<int:id>')
def accept_deposit(id):
    status = storage.accept_from_pending(id, "D")
    if status:
        flash("Operation Completed")
        return redirect(url_for("Main.deposit_clear"))
    else:
        return redirect(url_for("Main.deposit_clear"))

@app.route("/reject_withdrawal/<int:id>")
def reject_withdrawal(id):
    status = storage.reject_from_pending(id, "W")
    if status:
        flash("Operation Completed")
        return redirect(url_for("Main.deposit_clear"))
    else:
        return redirect(url_for("Main.deposit_clear"))

@app.route('/accept_withdrawal/<int:id>')
def accept_withdrawal(id):
    status = storage.accept_from_pending(id, "W")
    if status:
        flash("Operation Completed")
        return redirect(url_for("Main.deposit_clear"))
    else:
        return redirect(url_for("Main.deposit_clear"))
