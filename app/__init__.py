from flask import Flask
from flask_wtf.csrf import CSRFProtect
from config import Config


app = Flask(__name__, template_folder='templates')
app.config.from_object("config.Config")
csrf = CSRFProtect()
csrf.init_app(app) 

from .views import *
