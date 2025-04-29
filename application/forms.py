from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,BooleanField
from wtforms.validators import data_required,email,length,equal_to,ValidationError
from application.models import User

class LoginForm(FlaskForm):
    email = StringField("Email", validators=[data_required(),email()])
    password = StringField ("Password", validators=[data_required(),length(min=8,max=16)])
    remember_me = BooleanField("Remember Me")
    submit = SubmitField("Login")

class RegisterForm(FlaskForm):
    email = StringField("Email", validators=[data_required(),email()])
    password = StringField ("Password", validators=[data_required(),length(min=8,max=16)])
    password_check = StringField ("Re-Enter Password", validators=[data_required(),length(min=8,max=16),equal_to('password')])
    first_name = StringField ("First Name", validators=[data_required(),length(min=2,max=24)])
    last_name = StringField ("Last Name", validators=[data_required(),length(min=2,max=24)])
    submit = SubmitField("Register Now")

    def validate_email(self,email):
        user = User.objects(email=email.data).first()
        if user:
            raise ValidationError("This email is already in use; please provide another one.")