from app.models import User, Post, Comment, Vote
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

db.close()