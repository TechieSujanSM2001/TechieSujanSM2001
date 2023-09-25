import os

class Config:
    # Database settings (SQLite as an example, replace with your actual database URL)
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///your_database.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Secret key for session management (replace with a secure, random key)
    SECRET_KEY = os.environ.get('SECRET_KEY')

    # Other configurations...
