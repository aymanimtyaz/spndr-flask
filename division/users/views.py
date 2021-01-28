from flask import render_template, redirect, url_for, request, Blueprint, flash, request
from flask_login import login_user, login_required, logout_user, current_user
from spndr_flask import db 
from spndr_flask.models.user_model import User
from spndr_flask.forms.login_form import LoginForm
from spndr_flask.forms.signup_form import SignupForm
from spndr_flask.forms.editaccount_form import EditAccountForm
from spndr_tg.db_engine import db_operations as dbo

users_bp = Blueprint('users', __name__)

@users_bp.route('/login', methods = ['GET', 'POST'])
def login():

    if current_user.is_authenticated:
        return redirect(url_for('core.dashboard'))

    form = LoginForm()
    incorrect_email_or_password = False

    if form.validate_on_submit():

        user = User.query.filter_by(email = form.email.data).first()
        if user is not None and user.check_password(form.password.data):

            login_user(user)

            page_to_redirect = request.args.get('next')
            if page_to_redirect is None or not page_to_redirect[0] == '/':

                page_to_redirect = url_for('core.dashboard')

            return redirect(page_to_redirect)
        
        incorrect_email_or_password = True
        
    return render_template('login.html', form = form, incorrect_email_or_password = incorrect_email_or_password)

@users_bp.route('/signup', methods = ['GET', 'POST'])
def signup():

    form = SignupForm()

    email_in_use = False

    if form.validate_on_submit():

        if User.query.filter_by(email = form.email.data).first() is None:

            new_spndr_user = User(email = form.email.data, 
                                  password = form.password.data) 
            
            db.session.add(new_spndr_user)
            db.session.commit()

            login_user(new_spndr_user)
            return redirect(url_for('core.dashboard'))
    
        email_in_use = True

    return render_template('signup.html', form = form, email_in_use = email_in_use)

@users_bp.route('/logout')
@login_required
def logout():

    logout_user()
    return redirect(url_for('core.index'))

@users_bp.route('/myaccount')
@login_required
def myaccount():

    return render_template('myaccount.html')

@users_bp.route('/editaccount', methods = ['GET', 'POST'])
@login_required
def editaccount():

    form = EditAccountForm()

    if form.validate_on_submit():

        if form.email.data is not (None or ''):
            if User.query.filter_by(email = form.email.data).first() is None:
                current_user.email = form.email.data
            else:
                form.email.errors.append('Email entered already in use, please use a different email')
                return render_template('editaccount.html', form = form)
        if (form.password.data is not (None or '')) and (form.confirm_password.data is not (None or '')) and (form.password.data == form.confirm_password.data):
            if current_user.check_password(form.password.data):
                form.password.errors.append('Please set a new password')
                return render_template('editaccount.html', form = form)
            current_user.generate_password(form.password.data)

        db.session.commit()

        return redirect(url_for('users.myaccount'))
    
    return render_template('editaccount.html', form = form)

@users_bp.route('/unlinktelegram')
@login_required
def unlinktelegram():

    current_user.telegram_id = None
    db.session.commit()
    return redirect(url_for('users.myaccount'))
        












        
            

