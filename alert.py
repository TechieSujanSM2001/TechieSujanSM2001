# models/alert.py

from datetime import datetime
from app import db  # Assuming 'db' is the SQLAlchemy instance

class Alert(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    message = db.Column(db.String(255))
    location_type = db.Column(db.String(255))
