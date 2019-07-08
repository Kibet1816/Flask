from flask_wtf import FlaskForm
from wtforms import BooleanField,PasswordField,SubmitField,StringField,TextAreaField,ValidationError
from wtforms.validators import Required,Email,EqualTo
from ..models import User

class RegistrationForm(FlaskForm):
    """
    Form to register new users

    Args:
        FlaskForm:
    """
    email = StringField("Your email")
    username = StringField("Enter preferred username")
    password= PasswordField("Password")
    confirm_password= PasswordField("Confirm your password")
    submit= SubmitField("Submit")

    def validate_email(self,data_field):
        """
        Method to validate email
        """
        if User.query.filter_by(email = data_field.data ).first():
            raise ValidationError("This email is already taken")

    def validate_username(self,data_field):
        """
        Method to validate username
        """
        if User.query.filter_by(username = data_field.data).first():
            raise ValidationError("This username is already taken")

class LoginForm(FlaskForm):
    """
    Form field for users to login
    """
    email = StringField("Your email")
    password = PasswordField("Your password")
    remember = BooleanField("Remember Me")
    submit = SubmitField("Sign up")