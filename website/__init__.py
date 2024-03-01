# from flask import Flask
# from flask_bootstrap import Bootstrap4
# from flask_sqlalchemy import SQLAlchemy
# from flask_login import LoginManager
# from flask_bcrypt import Bcrypt
# from flask_migrate import Migrate
# #from os import path
# #from os.path import exists
# # import psycopg2

# db = SQLAlchemy()
# bootstrap = Bootstrap4()
# bcrypt = Bcrypt()
# migrate = Migrate(db=db)

# def create_app():
#     app = Flask(__name__)
#     app.config['DEBUG'] = True
#     app.config['SECRET_KEY'] = 'zxcvbnm'
#     # app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://admin-1:Wildwave123@localhost:5432/tikiti_user'
#     app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://admin-1:Wildwave123@localhost:5432/tikiti_platform'


#     db.init_app(app)
#     bootstrap.init_app(app)
#     bcrypt.init_app(app)
#     migrate.init_app(app)
    

#     from .models import login_manager
#     login_manager.init_app(app)
#     #login_manager.login_view = "login"

#     from .views import views
#     from .auth import auth

#     app.register_blueprint(views, url_prefix="/")
#     app.register_blueprint(auth, url_prefix="/")

#     # with app.app_context():
#     #     create_database(app)

#     return app

# # def create_database(app):
# #     from .models import db
# #     db.create_all()
# #     print("Created database")

# # def create_database(app):
# #     if not path.exists("website" + db):
# #         db.create_all(app=app)
# #         print("Created database!")

# def create_database(app):
#         with app.app_context():
#             db.create_all()
#         #print("Created database!")



from flask import Flask
from flask_bootstrap import Bootstrap4
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
from flask_migrate import Migrate


db = SQLAlchemy()
bootstrap = Bootstrap4()
bcrypt = Bcrypt()
login_manager = LoginManager()
migrate = Migrate(db=db)

def create_app():
    app = Flask(__name__)
    app.config['DEBUG'] = True
    app.config['SECRET_KEY'] = 'zxcvbnm'
    # app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://admin-1:Wildwave123@localhost:5432/tikiti_user'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://admin-1:Wildwave123@localhost:5432/tikiti_platform'


    db.init_app(app)
    bootstrap.init_app(app)
    bcrypt.init_app(app)
    migrate.init_app(app)
    login_manager.init_app(app)
    #login_manager.login_view = 'auth.login'

    # from .models import login_manager
    # login_manager.init_app(app)
    # login_manager.login_view = "login"
    
    #from .views import views
    from .r_auth import auth

    #app.register_blueprint(views, url_prefix="/")
    app.register_blueprint(auth)

    # Added this
    # from .r_models import User
    
    # @login_manager.user_loader
    # def load_user(user_id):
    #     return User.query.get(int(user_id))
    
    return app


def create_database(app):
        with app.app_context():
            db.create_all()
#         #print("Created database!")







