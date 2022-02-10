from flask import Blueprint, session, request, jsonify
from app.models import User, Post, Comment, Upvote, Downvote
from app.db import Session, get_db
import sys
from sqlalchemy import or_
from app.utils.auth import login_required

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
    session['firstname'] = newUser.firstname
    session['lastname'] = newUser.lastname

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
    session['firstname'] = user.firstname
    session['lastname'] = user.lastname

    return jsonify(id = user.id)

@bp.route('/users/logout', methods = ['POST'])
def logout():
    # Clear session variables
    session.clear()
    return '', 204

@bp.route('/posts', methods = ['POST'])
@login_required
def create_post():
    data = request.get_json()
    db = get_db()

    try:
        newPost = Post(
            title = data['title'],
            post_text = data['post_text'],
            user_id = session.get('user_id')
        )
    except:
        print(sys.exc_info()[0])

        db.rollback()
        return jsonify(message = 'Post creation failed'), 500

    return jsonify(id = newPost.id)

@bp.route('/posts/<id>', methods = ['PUT'])
@login_required
def update_post(id):
    data = request.get_json()
    db = get_db()

    try:
        post = db.query(Post).filter(Post.id == id).one()
        post.title = data['title']
        post.post_text = data['post_text']
        db.commit()
    except:
        print(sys.exc_info()[0])

        db.rollback()
        return jsonify(message = 'Post not found'), 404

    return '', 204

@bp.route('/posts/<id>', methods = ['DELETE'])
@login_required
def delete_post(id):
    db = get_db()

    try:
        db.delete(db.query(Post).filter(Post.id == id).one())
        db.commit()
    except:
        print(sys.exc_info()[0])

        db.rollback()
        return jsonify(message = 'Post not found'), 404

    return '', 204

@bp.route('/posts/upvote', methods = ['PUT'])
@login_required
def upvote():
    db = get_db()
    data = request.get_json()

    try:
        newVote = Upvote(post_id = data['post_id'], user_id = data['user_id'])
        db.add(newVote)
        db.commit()
    except:
        print(sys.exc_info()[0])

        db.rollback()
        return jsonify(message = 'Unable to register vote'), 500
    
    return '', 204

@bp.route('/posts/downvote', methods = ['PUT'])
@login_required
def downvote():
    db = get_db()
    data = request.get_json()

    try:
        newVote = Downvote(post_id = data['post_id'], user_id = data['user_id'])
        db.add(newVote)
        db.commit()
    except:
        print(sys.exc_info()[0])

        db.rollback()
        return jsonify(message = 'Unable to register vote'), 500
    
    return '', 204

@bp.route('/comments', methods = ['POST'])
@login_required
def addComment():
    db = get_db()
    data = request.get_json()

    try:
        comment = Comment(comment_text = data['comment_text'], post_id = data['post_id'], user_id = session.get('user_id'))
        print(str(comment))
        db.add(comment)
        db.commit()
    except:
        print(sys.exc_info()[0])

        db.rollback()
        return jsonify(message = 'Comment creation failed'), 500

    return '', 204