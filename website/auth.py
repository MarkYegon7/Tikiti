# from flask import Blueprint,render_template,url_for,redirect,flash,request
# from flask_wtf import FlaskForm
# from wtforms import StringField,PasswordField,SubmitField,FileField,FloatField,TextAreaField,validators,DateField
# from wtforms.validators import DataRequired,Email,Length,ValidationError
# from .models import User,Concert,upload_img
# from flask_login import login_user,logout_user,login_required,current_user
# from flask_wtf.file import FileAllowed
# from . import db
# # from . import bcrypt

# auth = Blueprint("auth",__name__)
# #bcrypt = Bcrypt(app)

# class SignupForm(FlaskForm):
#     email = StringField('Email Address', validators=[DataRequired(),Length(min=6,max=35),Email()])
#     username = StringField('Username' ,validators=[DataRequired(),Length(min=2,max=25)])
#     password = PasswordField('Password',validators=[DataRequired()])
#     submit = SubmitField('Sign up')

# class LoginForm(FlaskForm):
#     username = StringField('Username' ,validators=[DataRequired(),Length(min=2,max=25)])
#     password = PasswordField('Password',validators=[DataRequired()])
#     submit = SubmitField('Login')

# class ConcertForm(FlaskForm):
#     poster = FileField('Concert Poster', validators=[DataRequired(), FileAllowed(['jpg', 'png', 'jpeg'], 'Images only!')])
#     description = TextAreaField('Description', validators=[DataRequired()])
#     date = DateField('Date', validators=[DataRequired()])
#     ticket_price = FloatField('Ticket Price', validators=[DataRequired()])
#     location = StringField('Location', validators=[DataRequired(), Length(max=255)])
#     submit = SubmitField('Add Concert')

# # def validate_poster(self, field):
# #     try:
# #         if not upload_img(field.data):
# #             raise validators.ValidationError('Error uploading image')
# #     except Exception as e:
# #         raise validators.ValidationError(f'Error uploading image: {str(e)}')

# # @auth.route('/login', methods=['GET', 'POST'])
# # def login():
# #     if current_user.is_authenticated:
# #         flash('You are already logged in.', 'info')
# #         return redirect(url_for('auth.dashboard'))

# #     form = LoginForm()

# #     if form.validate_on_submit():
# #         user = User.query.filter_by(username=form.username.data).first()

# #         if user and user.check_password(form.password.data):
# #             login_user(user, remember=form.remember.data)
# #             return redirect(url_for('auth.dashboard'))

# #         flash('Invalid username or password', 'error')

# #     title = "Login"
# #     return render_template('login.html', form=form, title=title)

# # @auth.route('/login', methods=['GET', 'POST'])
# # def login():
# #     form = LoginForm()

# #     if request.method == 'POST':
# #         username = request.form.get("username")
# #         password = request.form.get("password")

# #         user = User.query.filter_by(username=username).first()
# #         if user:
# #             if user.check_password(password):
# #                 flash("Logged in!", category='success')
# #                 login_user(user, remember=True)
# #                 return redirect(url_for('auth.dashboard'))
# #             else:
# #                 flash('Credentials is incorrect', category='error')
# #         else:
# #             flash('Username does not exist.', category='error')
    
# #     return render_template("login.html",form=form)


# @auth.route('/login', methods=['GET', 'POST'])
# def login():
#     form = LoginForm()

#     # if current_user.is_authenticated:
#     #     return redirect(url_for('auth.dashboard'))

#     if form.validate_on_submit():
#         username = form.username.data
#         password = form.password.data

#         user = User.query.filter_by(username=username).first()

#         if user and user.check_password(password):
#             login_user(user, remember=True)
#             flash('Login successful', 'success')
#             print("Login successful")
#             return redirect(url_for('auth.concerts'))
#         else:
#             flash('Invalid username or password', 'error')

#     return render_template('login.html', form=form)


# @auth.route('/register', methods=['GET', 'POST'])
# def sign_up():
#     form = SignupForm()

#     if current_user.is_authenticated:
#         return redirect(url_for('views.home'))

#     if request.method == 'POST':
#         email = request.form.get('email')
#         username = request.form.get('username')
#         password = request.form.get('password')

#         existing_user = User.query.filter_by(username=username).first()
#         if existing_user:
#             flash('Username already exists', 'error')
#         else:
#             new_user = User(email=email, username=username, password=password)
#             new_user.set_password(password)
#             db.session.add(new_user)
#             db.session.commit()
#             login_user(new_user,remember=True)
#             flash('Registration successful', 'success')
#             return redirect(url_for('auth.login'))

#     return render_template('signup.html',form=form)


# @auth.route('/dashboard', methods=['GET', 'POST']) 
# @login_required
# def dashboard():
#     return render_template('dashboard.html')

# # @auth.route('/add_concert', methods=['GET', 'POST'])
# # def add_concert():
# #     form = ConcertForm()
# #     if form.validate_on_submit():
# #         poster_filename = upload_img(form.poster.data)
# #         new_concert = Concert(
# #             poster_url=poster_filename,
# #             description=form.description.data,
# #             date=form.date.data,
# #             ticket_price=form.ticket_price.data,
# #             location=form.location.data
# #         )
# #         db.session.add(new_concert)
# #         db.session.commit()
# #         flash('Concert added successfully', 'success')
# #         return redirect(url_for('auth.concerts'))  # Redirect to the add_concert page after successful submission
# #     return render_template('add_concert.html', form=form)

# @auth.route('/add_concert', methods=['GET', 'POST'])
# @login_required
# def add_concert():
#     form = ConcertForm()
#     if form.validate_on_submit():
#         try:
#             poster_filename = upload_img(form.poster.data)
#             new_concert = Concert(
#                 poster_url=poster_filename,
#                 description=form.description.data,
#                 date=form.date.data,
#                 ticket_price=form.ticket_price.data,
#                 location=form.location.data
#             )
#             new_concert.save_concert()
#             flash('Concert added successfully', 'success')
#             return redirect(url_for('auth.concerts'))
#         except Exception as e:
#             print(f"Error adding concert: {str(e)}")
#             flash('Error adding concert', 'error')
#     return render_template('add_concert.html', form=form)


# @auth.route('/concerts')
# def concerts():
#     concerts = Concert.query.all()
#     return render_template('concerts.html',concerts=concerts)


# @auth.route("/log-out")
# def log_out():
#     return "Log out"
