from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager

db = SQLAlchemy()
DB_NAME = "foodexpress"


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'ThisIsASimpleSecretKey'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:password@localhost/foodexpress'
    db.init_app(app)

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    from .models import User,Chef,Health_Expert, Delivery,Employee,\
        Expert_User_Report,Menu,Order,Payment,User_Health_Report,User_Taste_Form, Login

    create_database(app)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return Login.query.get(id)

    return app


def create_database(app):
    if not path.exists('localhost:3306' + DB_NAME):
        db.create_all(app=app)
        print('Created Database!')

