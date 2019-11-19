import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') 

    RECAPTCHA_USE_SSL = False
    RECAPTCHA_PRIVATE_KEY = os.environ.get('CAPTCHA_PRIVATE_KEY') 
    RECAPTCHA_PUBLIC_KEY = os.environ.get('CAPTCHA_PUBLIC_KEY')

    #COOKIE / XSS
    SESSION_COOKIE_HTTPONLY = True
    REMEMBER_COOKIE_HTTPONLY = True
    