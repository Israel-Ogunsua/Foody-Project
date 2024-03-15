from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField, SubmitField
from wtforms.validators import DataRequired, Email,EqualTo, Length, ValidationError
from main.model import User  

class loginForm(FlaskForm):
    username = StringField(label ="Username", validators=[ DataRequired(), Length(min = 2, max= 40)])
    password = PasswordField(label= "Password", validators=[DataRequired()])
    submit = SubmitField(label= "Login")

class registrationForm(FlaskForm):
    username = StringField(label ="Username", validators=[ DataRequired(), Length(min = 2, max= 40)])
    email =StringField(label= "Email", validators=[DataRequired(), Email()])
    password = PasswordField(label= "Password", validators=[DataRequired()])
    repassword =PasswordField(label="Confirm Password", validators = [DataRequired(),EqualTo("password")])
    submit = SubmitField(label= "Create account ")

    def validate_username(self, username):
        user = User.query.filter_by(username = username.data).first()
        if user:
            raise ValidationError("This username is been taken please chose a different one")
    

    def validate_email(self, email):
        user_email = User.query.filter_by(email = email.data).first()
        if user_email:
            raise ValidationError("Sorry this email has been taken please chose a diffent one")
