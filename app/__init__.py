from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

login_manager = LoginManager()
db = SQLAlchemy()


def create_app(settings_module='config.development'):
    app = Flask(__name__, instance_relative_config=True)
    # Cargamos los parámetros de configuracion según el entorno
    app.config.from_object(settings_module)
    # Cargamos la configuración del directorio instance
    if app.config.get('TESTING', False):
        app.config.from_pyfile('config-testing.py', silent=True)
    else:
        app.config.from_pyfile('config.py', silent=True)

    login_manager.init_app(app)
    login_manager.login_view = "auth.login"

    db.init_app(app)

    # Registro de los Blueprints
    from .auth import auth_bp
    app.register_blueprint(auth_bp)

    from .admin import admin_bp
    app.register_blueprint(admin_bp)

    from .public import public_bp
    app.register_blueprint(public_bp)

    return app


@login_manager.user_loader
def load_user(user_id):
    return User.get_by_id(int(user_id))