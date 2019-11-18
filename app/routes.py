from flask import render_template, flash, redirect, request, session, url_for
from app import app 
from app.forms import SignInForm

##
# INDEX ROUTE
##
@app.route('/')
def index():
    form = SignInForm()

    #Send form if condictions = OK and redirect
    if request.method == 'POST' and form.validate_on_submit():
        session.permanent = True
        user = request.form
        session["user"] = user
        flash('Bienvenue à vous {}, remember_me={}'.format(form.username.data, form.remember_me.data, "info"))
        return redirect(url_for('index'))
    else:
        if "user" in session: 
            return redirect(url_for('dashboard'))
        
        return render_template('signin.html', title='Sign In', form=form)
   
