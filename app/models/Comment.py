# Import the Base class
from app.db import Base
from sqlalchemy import Column, String, ForeignKey, Integer, DateTime
from datetime import datetime
from sqlalchemy.orm import relationship

class Comment(Base):
    __tablename__ = 'comments'
    id = Column(Integer, primary_key=True)
    comment_text = Column(String(280), nullable=False)
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)
    user_id = Column(Integer, ForeignKey('users.id'))
    post_id = Column(Integer, ForeignKey('posts.id'))

    user = relationship('User')
