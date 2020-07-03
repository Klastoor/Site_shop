from datetime import datetime
from app import db, lm
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin


class User(UserMixin, db.Model):
    __tablename__ = "Users"
    id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String(40), index=True, nullable=False, unique=True)
    email = db.Column(db.String(40), index=True, nullable=False, unique=True)
    name = db.Column(db.String(40), index=True, nullable=False)
    gender = db.Column(db.String(20))
    about = db.Column(db.String())
    password_hash = db.Column(db.String(120))
      

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    @lm.user_loader
    def load_user(user_id):
        return db.session.query(User).get(user_id)
