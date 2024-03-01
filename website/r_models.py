from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from . import db,login_manager
from flask import current_app
import os,secrets

class User(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True, nullable=True)
    email = db.Column(db.String(255), unique=True, nullable=True)
    username = db.Column(db.String(255), unique=True, nullable=True)
    password = db.Column(db.String(255), nullable=True)

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
         return check_password_hash(self.password, password)

    # def save_user(self):
    #     db.session.add(self)
    #     db.session.commit()

class Concert(db.Model):
    __tablename__ = 'concerts'
    id = db.Column(db.Integer,primary_key=True)
    poster_url = db.Column(db.String(255),nullable=True)
    description = db.Column(db.Text,nullable=True)
    date = db.Column(db.DateTime,nullable=True)
    ticket_price = db.Column(db.Float,nullable=True)
    location = db.Column(db.String(255),nullable=True)

    # def save_concert(self):
    #     db.session.add(self)
    #     db.session.commit()

    #     def __repr__(self):
    #         return f'Concert {self.id}'

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


# def upload_img(post_img):
#     random_hex = secrets.token_hex(8)
#     _, f_ext = os.path.splitext(post_img.filename)
#     picture_filename = random_hex + f_ext
#     picture_path = os.path.join(
#         current_app.root_path, "static/photos", picture_filename
#     )
#     post_img.save(picture_path)
#     return picture_filename

# def upload_img(post_img):
#     random_hex = secrets.token_hex(8)
#     _, f_ext = os.path.splitext(post_img.filename)
#     picture_filename = random_hex + f_ext
#     picture_directory = os.path.join(current_app.root_path, "static/photos")

#     # Create the directory if it doesn't exist
#     os.makedirs(picture_directory, exist_ok=True)

#     picture_path = os.path.join(picture_directory, picture_filename)
#     post_img.save(picture_path)
#     return picture_filename 

def upload_img(post_img):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(post_img.filename)
    picture_filename = random_hex + f_ext
    picture_directory = os.path.join(current_app.root_path, "static/photos")

    # Create the directory if it doesn't exist
    os.makedirs(picture_directory, exist_ok=True)

    picture_path = os.path.join(picture_directory, picture_filename)
    post_img.save(picture_path)
    return picture_filename 