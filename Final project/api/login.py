from flask import Flask, request,jsonify, url_for, redirect, flash
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


@app.route("/", methods=["GET"])
def hompage():
        if "number" in session_managment:
            investor = storage.get_investor_by_number(session_managment["number"])
            return render_template("hompage.html", name=investor.name.partition(" ")[0])
        else:
            return redirect(url_for("Main.login"))

def validate_user_loin_password(investor, password):
    if investor.password == password:
        return True
    else:
        return False

def validate_sinup_number(number):
    """
    Validate if number and password is in standard form
    :param number: The number for login
    :param password: for login
    :return: error codes
     error
        false if the number is not verifed
        -1 if password is lenght
    """
    if len(number) < 10:
        return False
    if "+" not in number:
        return False
    if number.index("+") != 0:
        return False
    if not number[1:len(number)].isnumeric():
        return False
    return True

def validate_signup_password(pas):
    if len(pas) < 5:
        return False
    return True

@ app.route("/login", methods=["POST", "GET"])
def login():
    """
    Check for validation
    :return:
    """
    if request.method == "POST":
        number = request.form["number"]
        password = request.form['pass']
        investor = storage.get_investor_by_number(number)
        if investor:
            if validate_user_loin_password(investor, password):
                session_managment["number"] = number
                return redirect(url_for('Main.hompage'))
            else:
                flash("Wrong Password")
                return render_template("login.html")
        else:
            flash("User not found. check number or create User")
            return render_template("login.html")
    else:
        if "number" in session_managment:
            return redirect(url_for("Main.hompage"))
        return render_template("login.html")

@app.route("/signup/<int:id>" , methods=["GET", "POST"])
def signup(id):
    if request.method == "POST":
        session_managment.pop("user", None)
        email = request.form.get("email")
        password = request.form.get("pass")
        confirm_pass = request.form.get("pass1")
        number = request.form.get("number")
        name = request.form.get("name")
        super_id = request.form.get("super_id")
        investor = storage.get_investor_by_number(number)
        if investor:
            flash("number already registered. Try to change the number or sign in with the number")
            return render_template("register.html", sid=super_id)
        if not validate_sinup_number(number):
            flash("Tel phone number format error. example +233xxxxxxx")
            return render_template("register.html", sid=super_id)
        if not validate_signup_password(password):
            flash("Password format error. Password must be more than 6 letters")
            return render_template("register.html", sid=super_id)
        if password != confirm_pass:
            flash("Passwords dont match, check passwords again")
            return render_template("register.html", sid=super_id)
        data = {"number": number, "email": email, "password": password, "name": name, "super_id":super_id}
        storage.create_investor(data)
        return redirect(url_for("Main.login"))
    else:
        return render_template("register.html", sid=id)



@app.route("/signup", methods=['POST', 'GET'])
def signup_2():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("pass")
        confirm_pass = request.form.get("pass1")
        number = request.form.get("number")
        name = request.form.get("name")
        super_id = request.form.get("super_id")
        investor = storage.get_investor_by_number(number)
        if investor:
            flash("number already registered. Try to change the number or sign in with the number")
            return redirect(url_for("Main.user_invite", id=super_id))
        if not validate_sinup_number(number):
            flash("Tel phone number format error. example +233xxxxxxx")
            return redirect(url_for("Main.user_invite", id=super_id))
        if not validate_signup_password(password):
            flash("Password format error. Password must be more than 6 letters")
            return redirect(url_for("Main.user_invite", id=super_id))
        if password != confirm_pass:
            flash("Passwords dont match, check passwords again")
            return redirect(url_for("Main.user_invite", id=super_id))
        data = {"number": number, "email": email, "password": password, "name": name, "super_id":super_id}
        storage.create_investor(data)
        return redirect(url_for("Main.login"))
    else:
        return redirect(url_for("Main.user_invite", id=super_id))



@app.route("/signout")
def logout():
    if "number" in session_managment:
        session_managment.pop("number")
        return redirect(url_for("Main.login"))

@app.route("/reset", methods=['GET', 'POST'])
def change_pwd():
    if request.method == "POST":
        password = request.form.get("pwd")
        confirm_pass = request.form.get("pass1")
        number = request.form.get("number")
        investor = storage.get_investor_by_number(number)
        if not investor:
            flash("Number not found, check number and try again" + password)
            return render_template("reset.html")
        if not validate_signup_password(password):
            flash("Password format error. Password must be more than 5 letters")
            return render_template("reset.html")
        if password != confirm_pass:
            flash("Passwords dont match, check passwords again")
            return render_template("reset.html")
        flash("Success")
        storage.change_password(number, password)
        return redirect(url_for("Main.login"))
    else:
        return render_template("reset.html")

    # Vip Purchases


