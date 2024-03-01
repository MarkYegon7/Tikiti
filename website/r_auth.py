from flask import render_template, redirect, url_for, flash,Blueprint,request
from flask_login import login_user, login_required, current_user, logout_user
from .r_models import User,Concert,upload_img
from . import db
#from .auth import auth
from .auth_forms import LoginForm,SignupForm,ConcertForm
from .request_api import get_seatgeek_event_info

auth = Blueprint("auth",__name__)


@auth.route("/")
@login_required
def home():
        return render_template("home.html")

@auth.route("/dashboard")
@login_required
def dashboard():
        return render_template("dashboard.html")

# @auth.route('/login', methods=['GET', 'POST'])
# def login():
#     form = LoginForm()

#     if form.validate_on_submit():
#         username = form.username.data
#         password = form.password.data

#         user = User.query.filter_by(username=username).first()

#         #if user and user.check_password(password):
#         if user:
#             login_user(user)
#             flash('Login successful', 'success')
#             return redirect(url_for('auth.dashboard'))
#         else:
#             flash('Invalid username or password', 'error')

#     return render_template('login.html', form=form)

# @auth.route('/login', methods=['GET', 'POST'])
# def login():
#     form = LoginForm()
#     if form.validate_on_submit():
#         #  user = User.query.filter_by(username=form.username.data).first()
#         #  if user and user.check_password(form.password.data):
#         #          print("Logged in")
#         #          login_user(user)
                 
#                  return redirect(url_for('auth.dashboard'))
#         #  else:
#         #       flash('Invalid username or password','error')
#     return render_template('login.html', form=form)

@auth.route('/login/', methods=('GET', 'POST'))
def login():
    form = LoginForm()
    if form.validate_on_submit():
        login_user(form.user)
        flash("Logged in successfully.")
        return redirect("auth.dashboard")
    return render_template('login.html', form=form)


@auth.route('/register', methods=['GET', 'POST'])
def sign_up():
    form = SignupForm()

    # if current_user.is_authenticated:
    #     return redirect(url_for('auth.home'))

    if request.method == 'POST':
        email = request.form.get('email')
        username = request.form.get('username')
        password = request.form.get('password')

        existing_user = User.query.filter_by(username=username).first()
        if existing_user:
            flash('Username already exists', 'error')
        else:
            new_user = User(email=email, username=username, password=password)
            new_user.set_password(password)
            db.session.add(new_user)
            db.session.commit()
            #login_user(new_user,remember=True)
            flash('Registration successful', 'success')
            return redirect(url_for('auth.login'))

    return render_template('signup.html',form=form)


@auth.route('/add_concert', methods=['GET', 'POST'])
def add_concert():
    form = ConcertForm()

    if form.validate_on_submit():
        # try:
            #poster_filename = upload_img(form.poster.data)
            new_concert = Concert(
                #poster_url=upload_img(form.poster.data),
                description=form.description.data,
                date=form.date.data,
                ticket_price=form.ticket_price.data,
                location=form.location.data
            )
            
            db.session.add(new_concert)
            db.session.commit()

            flash('Concert added successfully', 'success')
            return redirect(url_for('auth.concerts'))

        # except Exception as e:
        #     print(f"Error adding concert: {str(e)}")
        #     flash('Error adding concert', 'error')

    return render_template('add_concert.html', form=form)

@auth.route('/concerts')
def concerts():
    concerts = Concert.query.all()
    return render_template('concerts.html',concerts=concerts)



@auth.route('/display_event')
def seatgeek_event():
    event_info = get_seatgeek_event_info()  # You need to implement the function to make the API request
    return render_template('events.html', event_info=event_info)



@auth.route("/log-out")
@login_required
def log_out():
    logout_user()
    flash('Logged out successfully', 'info')
    return redirect(url_for('views.home'))