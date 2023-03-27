"""Blogly application."""

from flask import Flask, request, render_template, redirect, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, User

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///blogly'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

connect_db(app)
db.create_all()

@app.route('/')
def home():
    users = User.query.order_by(User.last_name, User.first_name).all()
    return render_template('user_index.html', users=users)

@app.route("/new_user", methods=["POST", "GET"])
def users_new():
    """Handle form submission for creating a new user"""

    if request.method == "POST" : 
        print(request.form)
        print(request.args) 
        image_url = request.form['image_url']
        if image_url == "":
            image_url = None
        new_user = User(
        first_name=request.form['first_name'],
        last_name=request.form['last_name'],
        image_url=image_url)
        db.session.add(new_user)
        db.session.commit()

        return redirect("/")
    else:
        return render_template("new_user.html")
        
@app.route('/<int:user_id>')
def show_user(user_id):
    user = User.query.get_or_404(user_id)
    return render_template("user_page.html", user=user)

@app.route('/<int:user_id>/delete', methods=["POST"])
def delete_user(user_id):
    user = User.query.get_or_404(user_id)
    db.session.delete(user)
    db.session.commit()
    return redirect("/")

@app.route('/<int:user_id>/edit', methods=["POST", "GET"])
def edit_user(user_id):
    
    if request.method == "POST":
        user = User.query.get_or_404(user_id)
        user.first_name = request.form['first_name']
        user.last_name = request.form['last_name']
        user.image_url = request.form['image_url']
        db.session.add(user)
        db.session.commit()
        return redirect('/')
    else:
        user = User.query.get_or_404(user_id)
        return render_template("edit_user.html", user=user)
