from src import db, login_mgr
from flask_login import UserMixin
from flask_bcrypt import generate_password_hash, check_password_hash

@login_mgr.user_loader
def load_user(user_id):
    return User.query.get(user_id)

class User(db.Model, UserMixin):

    __tablename__ = 'users'

    id = db.Column(db.BigInteger, primary_key = True, index = True)
    email = db.Column(db.String(64), unique = True, nullable = False, index = True)
    telegram_id = db.Column(db.BigInteger, unique = True, index = True)
    hashed_password = db.Column(db.String(150), nullable = False)

    def __init__(self, email, password):
        self.email = email
        self.hashed_password = generate_password_hash(password).decode('utf-8')

    def check_password(self, password):
        return check_password_hash(self.hashed_password, password)

    def __repr__(self):
        return f'UserID: {self.id}'