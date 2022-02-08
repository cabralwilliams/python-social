# Import the Base class
from app.db import Base
from sqlalchemy import Integer, Column, String, ForeignKey, DateTime
from datetime import datetime
from sqlalchemy.orm import relationship

class Post(Base):
    __tablename__ = 'posts'
    id = Column(Integer, primary_key=True)
    title = Column(String(100), nullable=False)
    post_text = Column(String(280), nullable=False)
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)
    user_id = Column(Integer, ForeignKey('users.id'))

    user = relationship('User')
    # Remove comments associated with post upon deletion of post
    comments = relationship('Comment', cascade='all,delete')