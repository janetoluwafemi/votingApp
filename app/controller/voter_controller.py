
from app.model import Voter
from app import db

def login_as_a_voter(data):
    name = data.get('name')
    voter = Voter(name=name)
    db.session.add(voter)
    db.session.commit()
    return {"message": f"Voter {name} Successfully Logged in!"}

class VoterController:
    pass