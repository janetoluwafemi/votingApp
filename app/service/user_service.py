from app.model import User
from app import db
from werkzeug.security import generate_password_hash, check_password_hash

class UserService:
    def __init__(self):
        pass
    @staticmethod
    def register_user(first_name, last_name, email, password, role):
        existing_user = User.query.filter_by(email=email).first()
        if existing_user:
            return "User already exists"
        hashed_password = generate_password_hash(password)
        user = User(first_name=first_name, last_name=last_name, email=email, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        return user.id
