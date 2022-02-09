from app.db import Base
from sqlalchemy import Column, Integer, ForeignKey, Boolean

class Upvote(Base):
    __tablename__ = 'upvotes'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    post_id = Column(Integer, ForeignKey('posts.id'))