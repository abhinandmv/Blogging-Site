from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.fields.simple import EmailField, PasswordField, TextAreaField
from wtforms.validators import DataRequired, URL
from flask_ckeditor import CKEditorField


# WTForm for creating a blog post
class CreatePostForm(FlaskForm):
    title = StringField("Blog Post Title", validators=[DataRequired()])
    subtitle = StringField("Subtitle", validators=[DataRequired()])
    img_url = StringField("Blog Image URL", validators=[DataRequired(), URL()])
    body = CKEditorField("Blog Content", validators=[DataRequired()])
    submit = SubmitField("Submit Post")



class RegisterForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired()])
    email = EmailField("Email" , validators=[DataRequired()])
    password = PasswordField("password" , validators = [DataRequired()])
    register = SubmitField("Sign Up")


class LoginForm(FlaskForm):
    email = EmailField("Email" , validators=[DataRequired()])
    password = PasswordField("Password" , validators=[DataRequired()])
    login = SubmitField("Sign In")


class CommentForm(FlaskForm):
    comment = CKEditorField("Comment",validators=[DataRequired()])
    submit = SubmitField("Comment")
