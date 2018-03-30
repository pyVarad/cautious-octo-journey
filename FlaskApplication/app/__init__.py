from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config


app = Flask(__name__)
app.config.from_object(Config)
app.config['SECRET_KEY'] = 'my-super-development-key'
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from views.home import home
app.register_blueprint(home)

from app import models

