# Import the Base class
from app.db import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import validates
import bcrypt
# Import the regular expression object
import re

# Generate the salt -> defaults to 12 rounds
salt = bcrypt.gensalt()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String(50), nullable=False, unique=True)
    email = Column(String(50), nullable=False, unique=True)
    firstname = Column(String(50), nullable=False)
    lastname = Column(String(50), nullable=False)
    password = Column(String(100), nullable=False)

    # Validation for email
    @validates('email')
    def validate_email(self, key, email):
        pattern = re.compile('[A-Za-z0-9_]+\.?[A-Za-z0-9_]+@[A-Za-z0-9]+\.[A-Za-z]{2,4}')
        assert re.match(pattern,email)

        return email

    # Validation for password
    @validates('password')
    def validate_password(self, key, password):
        assert len(password) > 4

        # encrypt password
        return bcrypt.hashpw(password, salt)

    # Verify that the correct password was entered
    def verify_password(self, password):
        return bcrypt.checkpw(password.encode('utf-8'), self.password.encode('utf-8'))

