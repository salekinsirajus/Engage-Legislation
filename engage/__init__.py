# Put the components together
from flask import Flask
# testing db load
from flask_pymongo import PyMongo
from flask_mail import Mail
import os

# Loading configs
app = Flask(__name__, instance_relative_config=True)
app.config.from_object('config')
# For loading from the instance/config.py file
app.config.from_pyfile('config.py')

# importing views
# Project Model taken from https://gist.github.com/cedbeu/5596125

# Move this config to a different place, putting it here for demo
app.config.update(dict(
    DEBUG = True,
    MAIL_SERVER = 'smtp.gmail.com',
    MAIL_PORT = 465,
    MAIL_USE_TLS = False,
    MAIL_USE_SSL = True,
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME'),
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
))

mail = Mail(app)
mongo = PyMongo(app)

from engage.controllers import subscribe, show, index
