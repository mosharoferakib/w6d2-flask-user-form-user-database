from flask import render_template, flash, redirect, url_for

from app.models import User 
from app import db


from . import bp 
from app.forms import RegisterForm


@bp.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        username = form.username.data
        user = User.query.filter_by(username=username).first()
        email = User.query.filter_by(email=form.email.data).first()
        if not email and not user:
            u = User(username=username,email=form.email.data,password=form.password.data)
            u.commit()
            flash(f"{username} registered")
            return redirect(url_for("main.home"))
        if user:
            flash(f'{username} already exist, please try again')
        else:
            flash(f'{form.email.data} already exist, please login')
    return render_template('register.jinja', form=form)

@bp.route('/signin')
def signin():
    return render_template('signin.jinja')

