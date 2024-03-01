from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField,SubmitField,FileField,TextAreaField,DateField,FloatField
from wtforms.validators import DataRequired,Email,Length,ValidationError
from flask_wtf.file import FileAllowed
from .r_models import User

from sqlalchemy.orm.exc import MultipleResultsFound, NoResultFound

class SignupForm(FlaskForm):
    email = StringField('Email Address', validators=[DataRequired(),Length(min=6,max=35),Email()])
    username = StringField('Username' ,validators=[DataRequired(),Length(min=2,max=25)])
    password = PasswordField('Password',validators=[DataRequired()])
    submit = SubmitField('Sign up')

# class LoginForm(FlaskForm):
#     username = StringField('Username' ,validators=[DataRequired(),Length(min=2,max=25)])
#     password = PasswordField('Password',validators=[DataRequired()])
#     submit = SubmitField('Login')

class LoginForm(FlaskForm):

    username = StringField(validators=[DataRequired()])
    password = StringField(validators=[DataRequired()])
    submit = SubmitField('Login')

    def validate_password(form, field):
        try:
            user = User.query.filter(User.username == form.username.data).one()
        except (MultipleResultsFound, NoResultFound):
            raise ValidationError("Invalid user")
        if user is None:
            raise ValidationError("Invalid user")
        if not user.check_password(form.password.data):
            raise ValidationError("Invalid password")
        
        form.user = user

class ConcertForm(FlaskForm):
    poster = FileField('Concert Poster', validators=[DataRequired(), FileAllowed(['jpg', 'png', 'jpeg'], 'Images only!')])
    description = TextAreaField('Description', validators=[DataRequired()])
    date = DateField('Date', validators=[DataRequired()])
    ticket_price = FloatField('Ticket Price', validators=[DataRequired()])
    location = StringField('Location', validators=[DataRequired(), Length(max=255)])
    submit = SubmitField('Add Concert')