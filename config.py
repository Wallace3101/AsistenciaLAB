import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY', 'mi_secreto')
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://root:12345@localhost/dbAsistenciaLab'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
