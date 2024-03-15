from flask.helpers import flash
from main import app, bcrypt,login_manager
from flask import render_template, url_for, flash, redirect, request
from flask_login import login_user, login_required, logout_user, current_user
from main.form import loginForm, registrationForm
from main.model import User, db
from flask_sqlalchemy import SQLAlchemy


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/login", methods=["GET","POST"])
def login():
    form = loginForm()

    if current_user.is_authenticated:
        redirect(url_for("home"))


    if form.validate_on_submit():
        flash(f'Check your uernsme or password {form.password.data}')
            
    else:  
        user = User.query.filter_by(username=form.username.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            flash(f'You are now logged-in as {user.username}', category="success")
            login_user(user)
            next_page = request.args.get("next")
            return redirect(next_page) if next_page else redirect(url_for("home"))
    return render_template("login.html", form = form)

@app.route("/register", methods=["GET","POST"])
def register():
    form = registrationForm()
    if current_user.is_authenticated:
        redirect(url_for("home"))
        
    if form.validate_on_submit():
        password_hash = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username = form.username.data, email= form.email.data,  password= password_hash)
        db.session.add(user)
        db.session.commit()
        flash(f'Your account have been  created as {form.username.data}!', category="success")
        return redirect(url_for("login"))
    return render_template("register.html", form = form)


@app.route("/account")
@login_required
def account():
    return render_template("account.html")

@app.route("/logout")
def logout():
    logout_user()
    return render_template("logout.html")