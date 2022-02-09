# Import the Base class
from app.db import Base
from sqlalchemy import Integer, Column, String, ForeignKey, DateTime, select, func, and_
from datetime import datetime
from sqlalchemy.orm import relationship, column_property
from .Upvote import Upvote
from .Downvote import Downvote

class Post(Base):
    __tablename__ = 'posts'
    id = Column(Integer, primary_key=True)
    title = Column(String(100), nullable=False)
    post_text = Column(String(280), nullable=False)
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)
    user_id = Column(Integer, ForeignKey('users.id'))
    up_votes = column_property(
        select([func.count(Upvote.id)]).where(Upvote.post_id == id)
    )
    down_votes = column_property(
        select([func.count(Downvote.id)]).where(Downvote.post_id == id)
    )

    user = relationship('User')
    # Remove comments associated with post upon deletion of post
    comments = relationship('Comment', cascade='all,delete')
    up_vote_count = relationship('Upvote', cascade='all,delete')
    down_vote_count = relationship('Downvote', cascade='all,delete')