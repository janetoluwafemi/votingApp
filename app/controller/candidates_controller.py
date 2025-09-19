from app.model import Candidates
from app import db

def login_as_a_candidate(data):
    name = data.get('email')
    candidate = Candidates(name=name)
    db.session.add(candidate)
    db.session.commit()
    return {"message": f"Candidate {name} Successfully Logged in!"}

class CandidatesController:
    pass