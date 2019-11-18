from flask_wtf import FlaskForm, RecaptchaField
from wtforms import StringField, PasswordField, BooleanField, SubmitField, validators
import os

class SignInForm(FlaskForm):
    username = StringField('Username', [validators.DataRequired()])
    password = PasswordField('Password', [validators.DataRequired()])
    # recaptcha = RecaptchaField()
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Se connecter')