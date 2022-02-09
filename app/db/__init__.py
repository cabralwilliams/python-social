from os import getenv
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
from flask import g

# Load environment variables
load_dotenv()

print('Trying to connect')
print(getenv('DB_URL'))

# Create the database connection using imported environment variable
engine = create_engine(getenv('DB_URL'), echo=True, pool_size=20, max_overflow=0)
Session = sessionmaker(bind = engine)
# Grabs base class from sqlalchemy and use this as the parent class for all models(?)
Base = declarative_base()

#Close the database connection
def close_db(e=None):
    #When the function is called, the db property is removed from the global context
    db = g.pop('db', None)

    #If db is not None, close the db - guarantees that this won't run on every instance
    if db is not None:
        db.close()

def init_db(app):
    Base.metadata.create_all(engine)

    #This makes Flask run the close_db method along with its built-in teardown_appcontext method
    app.teardown_appcontext(close_db)

#Returns a sessionmaker object
def get_db():
    if 'db' not in g:
        # store db connection in app context
        g.db = Session()

    # A new db connection will only be created on the first invocation of this function
    return g.db