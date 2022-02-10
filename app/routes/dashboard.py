from flask import Blueprint, render_template, session, jsonify, request
from app.db import get_db
from app.models import User, Post, Comment, Upvote, Downvote
from app.utils.auth import login_required

bp = Blueprint('/dashboard', __name__, url_prefix='/dashboard')

@bp.route('/')
@login_required
def dashboard():
    db = get_db()
    # user = db.query(User).where(User.id == session.get('user_id'))
    posts = (
        db.query(Post)
        .filter(Post.user_id == session.get('user_id'))
        .order_by(Post.created_at.desc())
        .all()
    )

    return render_template('dashboard.html', posts = posts, user = { 'firstname': session.get('firstname'), 'lastname': session.get('lastname')}, loggedIn = session.get('loggedIn'))
