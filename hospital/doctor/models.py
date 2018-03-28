from flask_sqlalchemy import SQLAlchemy
from doctor import app

db = SQLAlchemy(app)

class Doctor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    contact_no = db.Column(db.Integer, nullable=False)
    department_id = db.Column(db.Integer, db.ForeignKey('department.id'))
    speciality = db.Column(db.String(50))
    qualifications = db.Column(db.String(50), nullable=False)
