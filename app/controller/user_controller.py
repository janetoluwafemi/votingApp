from app.model import User
from app import db

def register_user(data):
    name = data.get('name')
    user = User(name=name)
    db.session.add(user)
    db.session.commit()
    return {"message": f"User {name} registered!"}


class UserController:
    pass
