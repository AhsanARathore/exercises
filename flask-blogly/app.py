"""Blogly application."""

from flask import Flask, request, render_template, redirect, session
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, User, Post, Tag

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
        return redirect(f'/{user_id}')
    else:
        user = User.query.get_or_404(user_id)
        return render_template("edit_user.html", user=user, user_id=user.id)

@app.route('/<int:user_id>/posts/new', methods=["POST", "GET"])
def new_post(user_id):

    if request.method == "POST":
        user = User.query.get_or_404(user_id)
        tag_ids = [int(num) for num in request.form.getlist("tags")]
        tags = Tag.query.filter(Tag.id.in_(tag_ids)).all()
        new_post = Post(
        title = request.form["title"],
        content = request.form["content"],
        user_id=user.id, tags=tags)
        db.session.add(new_post)
        db.session.commit()
        return redirect(f'/{user_id}')
    else:
        user = User.query.get_or_404(user_id)
        tags = Tag.query.all()
        return render_template("new_post.html", user=user, user_id=user_id, tags=tags)
    
@app.route('/post/<int:post_id>')
def show_post(post_id):
    post = Post.query.get_or_404(post_id)
    user = User.query.get_or_404(post.user_id)
    return render_template("post_page.html", post=post, user=user)

@app.route('/post/<int:post_id>/delete', methods=["POST"])
def posts_destroy(post_id):

    post = Post.query.get_or_404(post_id)

    db.session.delete(post)
    db.session.commit()

    return redirect(f"/{post.user_id}")

@app.route('/post/<int:post_id>/edit', methods=["POST", "GET"])
def edit_post(post_id):
    
    if request.method == "POST":
        post = Post.query.get_or_404(post_id)
        user = User.query.get_or_404(post.user_id)

        post.title = request.form['title']
        post.content = request.form['content']

        tag_ids = [int(num) for num in request.form.getlist("tags")]
        post.tags = Tag.query.filter(Tag.id.in_(tag_ids)).all()
      
        db.session.add(post)
        db.session.commit()
        return redirect(f'/post/{post_id}')
    else:
        post = Post.query.get_or_404(post_id)
        user = User.query.get_or_404(post.user_id)
        tags = Tag.query.all()

        

        return render_template("edit_post.html", post=post, user=user, post_id=post_id, tags=tags)
    
@app.route('/tags')
def tags_index():
    tags = Tag.query.all()
    return render_template('tags_index.html', tags=tags)

@app.route('/tags/new', methods=["POST", "GET"])
def new_tag():
    if request.method == "POST":
        post_ids = [int(num) for num in request.form.getlist("posts")]
        posts = Post.query.filter(Post.id.in_(post_ids)).all()
        new_tag = Tag(name=request.form['name'], posts=posts)

        db.session.add(new_tag)
        db.session.commit()
        return redirect("/tags")
    else:
        posts = Post.query.all()
        return render_template('new_tag.html', posts=posts)

@app.route('/tags/<int:tag_id>')
def tags_show(tag_id):
    tag = Tag.query.get_or_404(tag_id)
    return render_template('show_tag.html', tag=tag)


@app.route('/tags/<int:tag_id>/edit', methods=["POST", "GET"])
def edit_tags(tag_id):
    if request.method == "POST":
        tag = Tag.query.get_or_404(tag_id)
        tag.name = request.form['name']
        post_ids = [int(num) for num in request.form.getlist("posts")]
        tag.posts = Post.query.filter(Post.id.in_(post_ids)).all()

        db.session.add(tag)
        db.session.commit()
    else:
        tag = Tag.query.get_or_404(tag_id)
        posts = Post.query.all()
        return render_template('edit_tag.html', tag=tag, posts=posts)
    

@app.route('/tags/<int:tag_id>/delete', methods=["POST"])
def tags_destroy(tag_id):
    tag = Tag.query.get_or_404(tag_id)
    db.session.delete(tag)
    db.session.commit()
    
    return redirect("/tags")
