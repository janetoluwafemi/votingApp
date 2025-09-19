from flask_sqlalchemy import SQLAlchemy
from flask import Flask, request, jsonify

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    from app.model.vote import Vote
    from app.model.user import User
    from app.model.voter import Voter
    from app.model.candidates import Candidates

    @app.route('/users', methods=['POST'])
    def register_user():
        data = request.get_json()
        return jsonify({'status': 'success', 'data': data}), 201
    @app.route('/loginAsVoter', methods=['POST'])
    def login_as_a_voter():
        data = request.get_json()
        return jsonify({'status': 'success', 'data': data}), 201
    @app.route('/loginAsCandidates', methods=['POST'])
    def login_as_a_candidate():
        data = request.get_json()
        return jsonify({'status': 'success', 'data': data}), 201
    with app.app_context():
        db.create_all()
    return app

