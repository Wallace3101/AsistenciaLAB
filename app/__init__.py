from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from config import Config

db = SQLAlchemy()
login_manager = LoginManager()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = 'main.login'

    from app.models import Participant  # Importación local para evitar problemas de circularidad
    @login_manager.user_loader
    def load_user(user_id):
        return Participant.query.get(int(user_id))

    from app.views import main
    app.register_blueprint(main)

    return app
