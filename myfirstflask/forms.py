from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,BooleanField
from  wtforms.validators import DataRequired,Length,Email,EqualTo
from wtforms.fields.simple import SubmitField

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(),Length(min=2,max=20)])
    email = StringField('Email', validators=[DataRequired(),Email()])
    password = PasswordField("Passport", validators=[DataRequired()])
    confirm_password = PasswordField('Confirm_Passport', validators=[DataRequired(),EqualTo(password)])
    submit = SubmitField('Sing up')
    
class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(),Email()])
    password = PasswordField('Passport', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')
    