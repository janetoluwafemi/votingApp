from app.model import Voter
from app.model import User
from app import db
from app.enum.role import Role

class VoterService:
    def __init__(self):
        pass

    @staticmethod
    def login_as_a_voter(email, password):
        existing_user = User.query.filter_by(email=email).first()
        if existing_user:
            if existing_user.role == Role.VOTER:
                voter = Voter(email=email, password=password)
                db.session.add(voter)
                db.session.commit()
                return voter.id

    @staticmethod
    def choose_party(bvn, party):
        existing_user = User.query.filter_by(id=id).first()
        if existing_user:
            voter = Voter(bvn=bvn, party=party)
            db.session.add(voter)
            db.session.commit()
            return voter.id

