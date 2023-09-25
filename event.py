# models/event.py

from datetime import datetime
from app import db  # Assuming 'db' is the SQLAlchemy instance

class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    is_driving_safe = db.Column(db.Boolean)
    vehicle_id = db.Column(db.String(255))
    location_type = db.Column(db.String(255))
