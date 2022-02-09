from flask import redirect, render_template, session, jsonify, Blueprint, request
from app.models import User, Post, Comment, Downvote, Upvote
from app.db import get_db
import sys

bp = Blueprint('/', __name__, url_prefix='/')

@bp.route('/')
def index():
    # get all posts
    db = get_db()
    posts = db.query(Post).order_by(Post.created_at.desc()).all()

    return render_template('homepage.html', posts = posts, loggedIn = session.get('loggedIn'))

@bp.route('/login')
def login():
    if session.get('loggedIn') == None:
        return render_template('login.html')
    
    return redirect('/dashboard')

@bp.route('/posts/<id>')
def getpost(id):
    db = get_db()

    try:
        post = db.query(Post).where(Post.id == id).one()
    except:
        print(sys.exc_info()[0])

        return jsonify(message = 'Post not found'), 404
    
    return render_template('viewPost.html', post = post, loggedIn = session.get('loggedIn'))