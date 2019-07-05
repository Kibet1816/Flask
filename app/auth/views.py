from flask import render_template,redirect,url_for,flash,request
from . import auth
from ..models import User
from .forms import RegistrationForm,LoginForm
from .. import db
from flask_login import login_user,logout_user,login_required

@auth.route('/create_account', methods = ['GET','POST'])
def register():
    """
    Function to handle requests to register new users
    """
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(email = form.email.data,username = form.username.data,password = form.password.data)
        db.session.add(user)
        db.session.commit()

        return redirect(url_for('auth.login'))

    return render_template('auth/register.html' , register = form)

@auth.route('/login' ,methods = ['GET','POST'])
def login():
    """
    Function to login users
    """
    loginform = LoginForm()
    if loginform.validate_on_submit():
        user = User.query.filter_by(email = loginform.email.data).first()
        if user is not None and user.verify_password(loginform.password.data):
            login_user(user,loginform.remember.data)
            return redirect(request.args.get('next') or url_for('main.index'))
        flash("Invalid email or password")
    return render_template('auth/login.html',login = loginform)