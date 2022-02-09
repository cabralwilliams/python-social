from app.models import User, Post, Comment, Upvote, Downvote
from app.db import Session, Base, engine

# Drop and recreate database
Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)

db = Session()

db.add_all([
    User(username='cabby',firstname='Cabral',lastname='Williams',email='cabby@email.com',password='password123'),
    User(username='cabby2',firstname='Cab',lastname='Wilson',email='cabby2@email.com',password='password123')
])

db.commit()

db.add_all([
    Post(title='First Post',post_text='This is the very first post in the database.',user_id=1),
    Post(title='Second Post',post_text='This is the second post in the database.',user_id=2)
])

db.commit()

db.close()