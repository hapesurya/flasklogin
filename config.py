import os

class Config:
    # SECRET_KEY = os.urandom(32)
    SECRET_KEY = os.environ.get('SECRET_KEY') or os.urandom(32)
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///site.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    BCRYPT_LOG_ROUNDS = 12
    PERMANENT_SESSION_LIFETIME = 60 * 15 #set session lifetime to 15 minutes
    SESSION_COOKIE_HTTPONLY = True
    SESSION_COOKIE_SECURE = True
    MAIL_USE_SSL = False
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('EMAIL_USER')
    MAIL_PASSWORD = os.environ.get('EMAIL_PASS')

