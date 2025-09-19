from app import db
class Candidates(db.Model):
    __tablename__ = 'candidates'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    party = db.Column(db.String(100), nullable=False)
    bio = db.Column(db.Text, unique=True, nullable=False)
    image = db.Column(db.String(225), unique=True, nullable=False)
