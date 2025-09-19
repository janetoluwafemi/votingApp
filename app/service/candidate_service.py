from app.model import Candidates
from app.model import User
from app.model.user import Role
from app import db

class CandidateService:
    def __init__(self):
        pass

    @staticmethod
    def login_as_a_candidate(email, password):
        existing_user = User.query.filter_by(email=email).first()
        if existing_user:
            if existing_user.role == Role.CANDIDATE:
                candidate = Candidates(email=email, password=password)
                db.session.add(candidate)
                db.session.commit()
                return candidate.id

