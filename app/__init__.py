from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config
from flask_login import LoginManager

db = SQLAlchemy()




def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    app.config['SECRET_KEY'] = 'billowing'
    login = LoginManager(app)
    login.login_view = 'auth.login'
    
    @login.user_loader
    def load_user(id):
        return User.query.get(int(id))

    # Register blueprints
    from .routes.game_routes import game_bp
    app.register_blueprint(game_bp)

    from .routes.auth import auth_bp
    app.register_blueprint(auth_bp, url_prefix='/auth')
    
    return app
