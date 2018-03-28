from flask_sqlalchemy import SQLAlchemy
from patient import app

db = SQLAlchemy(app)

class Doctor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    contact_no = db.Column(db.Integer, nullable=False,unique=True)
    age= db.Column(db.Integer,nullable=False)
    gender= db.Column(db.String(50))
    Address = db.Column(db.String(50), nullable=False)
