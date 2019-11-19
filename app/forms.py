from flask_wtf import FlaskForm, RecaptchaField
from wtforms import StringField, PasswordField, BooleanField, SubmitField, validators
from wtforms.validators import DataRequired
from wtforms.fields.html5 import EmailField, DateField

class SignInForm(FlaskForm):
    username = StringField('Username', [validators.DataRequired()])
    password = PasswordField('Password', [validators.DataRequired()])
    recaptcha = RecaptchaField()
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Se connecter')

class SignUpForm(FlaskForm):
    lastname = StringField('Nom', [validators.DataRequired()])
    firstname = StringField('Prénom', [validators.DataRequired()])
    username = StringField('Nom d\'utilisateur', [validators.DataRequired()])
    email = EmailField('Email', [validators.DataRequired()])
    password = PasswordField('Mot de passe', [validators.DataRequired()])
    confirmPass = PasswordField('Confimer le mot de passe', [
        validators.DataRequired(), 
        validators.EqualTo('password', 'La donnée saisie ne correspond pas à votre mot de passe !')
    ])
    # birthday = DateField('Date de naissance', [validators.DataRequired()])
    accept_tos = BooleanField('Termes d\'Utilisation', [validators.DataRequired()])
    recaptcha = RecaptchaField()
    submit = SubmitField('S\'enregistrer')