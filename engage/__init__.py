# Put the components together
from flask import Flask

app = Flask(__name__, instance_relative_config=True)
app.config.from_object('config')
# For loading from the instance/config.py file
app.config.from_pyfile('config.py')
