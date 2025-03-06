from datetime import date
from flask import Flask, abort, render_template, redirect, url_for, flash, jsonify
from flask_bootstrap import Bootstrap5
from flask_ckeditor import CKEditor
from flask_gravatar import Gravatar
from flask_login import UserMixin, login_user, LoginManager, current_user, logout_user, login_required
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship, DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Text
from functools import wraps
from werkzeug.exceptions import Unauthorized
from werkzeug.security import generate_password_hash, check_password_hash
from forms import CreatePostForm,RegisterForm,LoginForm,CommentForm
from datetime import datetime


'''
Make sure the required packages are installed: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from the requirements.txt for this project.
'''

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
ckeditor = CKEditor(app)
Bootstrap5(app)
login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    return db.session.get(User,user_id)

# CREATE DATABASE
class Base(DeclarativeBase):
    pass
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
db = SQLAlchemy(model_class=Base)

gravatar = Gravatar(app,
                    size=100,
                    rating='g',
                    default='retro',
                    force_default=False,
                    force_lower=False,
                    use_ssl=False,
                    base_url=None)


# CONFIGURE TABLES
class User(UserMixin, db.Model):
    __tablename__ = "user_data"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    email: Mapped[str] = mapped_column(String(100), unique=True)
    password: Mapped[str] = mapped_column(String(100))
    name: Mapped[str] = mapped_column(String(100))
    posts = relationship("BlogPost", back_populates="author")
    comments = relationship("Comment" , back_populates="comment_author")


class BlogPost(db.Model):
    __tablename__ = "blog_posts"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    author_id: Mapped[int] = mapped_column(Integer, db.ForeignKey("user_data.id"))
    author = relationship("User", back_populates="posts")

    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    subtitle: Mapped[str] = mapped_column(String(250), nullable=False)
    date: Mapped[str] = mapped_column(String(250), nullable=False)
    body: Mapped[str] = mapped_column(Text, nullable=False)
    img_url: Mapped[str] = mapped_column(String(250), nullable=False)
    comments = relationship("Comment" , back_populates="parent_post")

class Comment(db.Model):
    __tablename__ = "comment"
    id:Mapped[int] = mapped_column(Integer , primary_key=True)
    text:Mapped[str] = mapped_column(Text , nullable=False)
    author_id:Mapped[int] = mapped_column(Integer,db.ForeignKey("user_data.id"))
    post_id:Mapped[int] = mapped_column(Integer,db.ForeignKey("blog_posts.id"))
    comment_author = relationship("User" , back_populates="comments")
    parent_post = relationship("BlogPost" , back_populates="comments")

db.init_app(app)
with app.app_context():
    db.create_all()

def admin_only(f):
    @wraps(f)
    @login_required
    def decorated_function(*args , **kwargs):
        if current_user.is_authenticated:  # if a user is logged in
            if current_user.id != 1:  # and is not the admin
                return abort(403)
        else:  # random stranger
            return abort(403)
        return f(*args, **kwargs)
    return decorated_function


@app.route('/register' , methods = ["GET" , "POST"])
def register():
    current_year = datetime.now().year
    registeration_form = RegisterForm()
    if registeration_form.validate_on_submit():
        result = db.session.execute(db.select(User).where(User.email == registeration_form.email.data))
        user = result.scalar()
        if user:
            flash("This email already exists log in.")
            return redirect(url_for("login"))
        hash_password = generate_password_hash(registeration_form.password.data , method = 'pbkdf2:sha256' , salt_length=8)
        new_user = User(
            email = registeration_form.email.data,
            password = hash_password,
            name = registeration_form.name.data
        )
        db.session.add(new_user)
        db.session.commit()
        login_user(new_user)
        return redirect(url_for("get_all_posts"))
    return render_template("register.html" , form=registeration_form,current_user=current_user,year=current_year)



@app.route('/login',methods = ["GET" , "POST"])
def login():
    current_year = datetime.now().year
    login_form = LoginForm()
    if login_form.validate_on_submit():
        email = login_form.email.data
        password = login_form.password.data
        result = db.session.execute(db.select(User).where(User.email == email))
        user = result.scalar()
        if not user:
            flash("The email doesn't exist.Sign Up")
            return redirect(url_for("login"))
        elif not check_password_hash(user.password , password):
            flash("Incorrect Password! Please try again...")
            return redirect(url_for("login"))
        else:
            login_user(user)
            return redirect(url_for("get_all_posts"))
        # if user and check_password_hash(user.password , password):
        #     login_user(user)
        #     return redirect(url_for("get_all_posts"))
    return render_template("login.html" , form = login_form , current_user=current_user,year=current_year)


@app.route('/logout')
def logout():
    current_year = datetime.now().year
    logout_user()
    return redirect(url_for('get_all_posts',year=current_year))


@app.route('/')
def get_all_posts():
    current_year = datetime.now().year
    result = db.session.execute(db.select(BlogPost))
    posts = result.scalars().all()
    return render_template("index.html", all_posts=posts,current_user=current_user,year=current_year)



@app.route("/post/<int:post_id>",methods=["GET","POST"])
def show_post(post_id):
    current_year = datetime.now().year
    requested_post = db.get_or_404(BlogPost, post_id)
    form = CommentForm()
    if form.validate_on_submit():
        if not current_user.is_authenticated:
            flash("You need to login or register to be able to comment.")
            return redirect(url_for("login"))
        new_comment = Comment(
            text = form.comment.data,
            author_id = current_user.id,
            post_id = requested_post.id
        )
        db.session.add(new_comment)
        db.session.commit()
    result = db.session.execute(db.select(Comment).where(Comment.post_id == post_id))
    comments  = result.scalars().all()
    return render_template("post.html", post=requested_post,comments=comments ,current_user=current_user,form=form,year=current_year)



@app.route("/new-post", methods=["GET", "POST"])
@admin_only
def add_new_post():
    current_year = datetime.now().year
    form = CreatePostForm()
    if form.validate_on_submit():
        new_post = BlogPost(
            title=form.title.data,
            subtitle=form.subtitle.data,
            body=form.body.data,
            img_url=form.img_url.data,
            author=current_user,
            date=date.today().strftime("%B %d, %Y")
        )
        db.session.add(new_post)
        db.session.commit()
        return redirect(url_for("get_all_posts"))
    return render_template("make-post.html", form=form,current_user=current_user,year=current_year)



@app.route("/edit-post/<int:post_id>", methods=["GET", "POST"])
@admin_only
def edit_post(post_id):
    current_year = datetime.now().year
    post = db.get_or_404(BlogPost, post_id)
    edit_form = CreatePostForm(
        title=post.title,
        subtitle=post.subtitle,
        img_url=post.img_url,
        author=post.author,
        body=post.body
    )
    if edit_form.validate_on_submit():
        post.title = edit_form.title.data
        post.subtitle = edit_form.subtitle.data
        post.img_url = edit_form.img_url.data
        post.author = current_user
        post.body = edit_form.body.data
        db.session.commit()
        return redirect(url_for("show_post", post_id=post.id))
    return render_template("make-post.html", form=edit_form, is_edit=True,current_user=current_user,year=current_year)



@app.route("/delete/<int:post_id>")
@admin_only
def delete_post(post_id):
    current_year = datetime.now().year
    post_to_delete = db.get_or_404(BlogPost, post_id)
    db.session.delete(post_to_delete)
    db.session.commit()
    return redirect(url_for('get_all_posts',year=current_year))


@app.route("/about")
def about():
    current_year = datetime.now().year
    return render_template("about.html",current_user=current_user,year=current_year)


@app.route("/contact")
def contact():
    current_year = datetime.now().year
    return render_template("contact.html",current_user=current_user,year=current_year)




if __name__ == "__main__":
    app.run(debug=True, port=5002)
