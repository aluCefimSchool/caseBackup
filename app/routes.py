from flask import render_template, flash, redirect, request, session, url_for
from flask_login import current_user, login_user

from app import app 
from app.forms import SignInForm, SignUpForm
from app.models import User


##
# INDEX / LOGIN ROUTE
##
@app.route('/', methods=['GET', 'POST'])
def index():
    form = SignInForm()

    #IF USER CONNECTED REDIRECT TO DASHBOARD
    if current_user.is_authenticated:
        return redirect(url_for('dashboard'))
    #Send form if condictions = OK and redirect
    if request.method == 'POST' and form.validate_on_submit():
        session.permanent = True
        user = request.form
        session["user"] = user
        flash('Bienvenue à vous {}, remember_me={}'.format(form.username.data, form.remember_me.data, "info"))
        return redirect(url_for('dashboard'))

        found_user = users.query.filter_by(name = user).first()
        if found_user:
            session["email"] = found_user.email
        else:
            usr = users(user, "")
            db.session.add(usr)
            db.session.commit()

    else:
        if "user" in session: 
            return redirect(url_for('dashboard'))
        
        return render_template('signin.html', title='Sign In', form=form)
   

##
# SIGNUP ROUTE
##
@app.route('/signup', methods=['GET', 'POST'])
def signUp():
    form = SignUpForm()

    #Send form if conditions = OK and redirect
    if request.method == 'POST' and form.validate_on_submit():
        flash('Votre inscription a été prit en compte {}. Veuillez vérifier vos email pour confirmer votre inscription'.format(form.username.data, "info"))
        return redirect(url_for('index'))
    else: 
        if "user" in session:
            flash(f"Vous êtes déja inscrit sur notre application !", "info")
            return redirect(url_for("dashboard"))
    
    return render_template('signup.html', title='Sign Up', form=form)

##
# LOGOUT ROUTE
##
@app.route('/logout')
def logOut():
    if "user" in session:
        user = session["user"]
        flash(f"Vous avez été déconnecté de l'application !", "info")
    
    session.pop("user", None)
    return redirect(url_for("index"))

##
# DASHBOARD ROUTE
##
@app.route('/dashboard')
def dashboard():
    if "user" in session:
        user = session["user"]

        #Return template index.html with data
        return render_template('dashboard.html', title='Dashboard', user=user)
    
    else:
        #Redirect to signin route
        return redirect(url_for("index"))

##
# PROFIL ROUTE
##
@app.route('/profil')
def profil():
    if "user" in session:
        user = session["user"]

        if request.method == "POST" and form.validate_on_submit():
            email = request.form["email"]
            session["email"] = email
        else:
            if "email" in session:
                email = session["email"]

        #Return template index.html with data
        return render_template('profil.html', title='Profil', email=email)
    
    else:
        #Redirect to signin route
        return redirect(url_for("index"))