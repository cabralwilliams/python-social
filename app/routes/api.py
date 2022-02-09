from flask import Blueprint, session, request, jsonify
from app.models import User, Post, Comment, Vote
from app.db import get_db
import sys
from sqlalchemy import or_

bp = Blueprint('/api', __name__, url_prefix='/api')

@bp.route('/users', methods=['POST'])
def signup():
    data = request.get_json()

    # Get the database and save it to db
    db = get_db()

    try:
        newUser = User(
            username = data['username'],
            firstname = data['firstname'],
            lastname = data['lastname'],
            email = data['email'],
            password = data['password']
        )

        # Attempt to save user in database
        db.add(newUser)
        db.commit()

    except:
        print(sys.exc_info()[0])

        db.rollback()
        return jsonify(message = 'Sign up failed'), 500

    session.clear()
    session['user_id'] = newUser.id
    session['loggedIn'] = True

    return jsonify(id = newUser.id)

@bp.route('/users/login', methods = ['POST'])
def login():
    data = request.get_json()

    # Get the database and save it to db
    db = get_db()

    # Check for existing username/email
    try:
        user = db.query(User).filter(
            or_(
                User.email == data['username'],
                User.username == data['username']
            )
        ).one()
    except:
        print(sys.exc_info()[0])

        return jsonify(message = 'Incorrect credentials'), 400
    
    # Check for correct password
    if user.verify_password(data['password']) == False:
        return jsonify(message = 'Incorrect credentials'), 400

    session.clear()
    session['user_id'] = user.id
    session['loggedIn'] = True