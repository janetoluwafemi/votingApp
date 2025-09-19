from app import db
from app.enum.party import Party

class Voter(db.Model):
    __tablename__ = 'voters'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    image = db.Column(db.String(225), unique=True, nullable=False)
    bvn = db.Column(db.String, unique=True, nullable=False)
    vote = db.relationship('Vote', backref='voter', uselist=False)
    party = db.relationship(db.Enum(Party), uselist=False)