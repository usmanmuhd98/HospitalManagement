from flask_sqlalchemy import SQLAlchemy
from department import app

db = SQLAlchemy(app)

class Department(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    head = db.Column(db.Integer, db.ForeignKey('doctor.id'))
