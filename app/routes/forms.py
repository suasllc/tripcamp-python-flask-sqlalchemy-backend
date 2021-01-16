from flask_wtf import FlaskForm
from wtforms.fields import (
    PasswordField, StringField, SubmitField
)
from wtforms.fields.html5 import EmailField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    username = StringField("Username", [DataRequired()])
    password = PasswordField("Password", [DataRequired()])
    submit = SubmitField("Login")


class SinupForm(FlaskForm):
    username = StringField("Username", [DataRequired()])
    email = EmailField("Email", [DataRequired()])
    password = PasswordField("Password", [DataRequired()])
    confirm_password = PasswordField("confirm Password", [DataRequired()])
    submit = SubmitField("Signup")
