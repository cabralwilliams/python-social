from flask import redirect, render_template, session, jsonify, Blueprint, request
from app.models import User, Post, Comment, Downvote, Upvote
from app.db import get_db
import sys
from app.utils.auth import login_required

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
        canEdit = False
        if session.get('loggedIn') == True:
            if session.get('user_id') == post.user_id:
                canEdit = True
    except:
        print(sys.exc_info()[0])

        return jsonify(message = 'Post not found'), 404
    
    return render_template('viewPost.html', post = post, loggedIn = session.get('loggedIn'), canEdit = canEdit)

@bp.route('/edit/<id>')
@login_required
def editPost(id):
    db = get_db()

    try:
        post = db.query(Post).where(Post.id == id).one()
        if post.user.id != session.get('user_id'):
            # redirect to the post's page if the user information doesn't match
            redirect_url = '/posts/' + id
            return redirect(redirect_url)
        
    except:
        print(sys.exc_info()[0])

        return jsonify(message = 'Post not found'), 404

    return render_template('editPost.html', post = post, loggedIn = session.get('loggedIn'), postAction = 'Edit Post', postTitle = post.title, postId = post.id, userId = session.get('user_id'), postValue = post.title, postPlaceholder = post.post_text, postContent = post.post_text, isEditing = True)