from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from settings import Config

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)

from . import views
from . import error_handlers
from . import cli_commands