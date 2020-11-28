from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from src.config import postgres_db_uri, secret_key

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = postgres_db_uri
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = secret_key

db = SQLAlchemy(app)

login_mgr = LoginManager()
login_mgr.init_app(app)
login_mgr.login_view = 'users.login'

from src.division.core.views import core_bp
from src.division.users.views import users_bp
from src.division.error_handlers.handler import error_handler_bp

app.register_blueprint(core_bp)
app.register_blueprint(users_bp)
app.register_blueprint(error_handler_bp)



