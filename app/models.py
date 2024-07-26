from app import db
from flask_login import UserMixin

class Participant(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    apellido = db.Column(db.String(100), nullable=False)
    correo = db.Column(db.String(120), unique=True, nullable=False)
    numero_estudiante = db.Column(db.String(50), nullable=False)
    carrera = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(200), nullable=False)
    attendance = db.relationship('Attendance', backref='participant', lazy=True)

class Attendance(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    participant_id = db.Column(db.Integer, db.ForeignKey('participant.id'), nullable=False)
    timestamp = db.Column(db.DateTime, index=True, default=db.func.now())
