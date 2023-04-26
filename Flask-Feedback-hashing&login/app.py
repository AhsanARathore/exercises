from flask import Flask, render_template, redirect, session, flash
from flask_debugtoolbar import DebugToolbarExtension
from models import  db, connect_db, User, Feedback
from forms import Userform, LoginForm, FeedbackForm

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql:///flask_feedback"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_ECHO"] = True
app.config["SECRET_KEY"] = "abc123"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

connect_db(app) 
db.create_all()

toolbar = DebugToolbarExtension(app)

@app.route('/')
def redirect_to_register():
    return redirect('/login')

@app.route('/register', methods=['GET','POST'])
def register_user():
    form = Userform()
    if "username" in session:
        redirect(f'/users/{session["username"]}')
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        email = form.email.data
        first_name = form.first_name.data
        last_name = form.last_name.data
        new_user = User.register(username, password, email, first_name, last_name)

        db.session.add(new_user)
        db.session.commit()
        session['username'] = new_user.username
        flash('welcome, thanks for registering!', 'success')
        
        return redirect(f'/users/{new_user.username}')
    
    
    return render_template("register.html", form=form)

@app.route('/login', methods=["GET","POST"])
def login_user():
    form = LoginForm()
    if "username" in session:
        return redirect(f"/users/{session['username']}")
        
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data

        user = User.authenticate(username, password)
        if user:
            flash(f"Welcome Back, {user.username}!", "primary")
            session['username'] = user.username
            return redirect(f'/users/{user.username}')
        else:
            form.username.errors = [' invalid Username or Password']

    return render_template("login.html", form=form)

@app.route('/users/<username>')
def user_page(username):
    user = User.query.get(username)
    return render_template('user.html', user=user)

@app.route('/logout')
def logout_user():
    session.pop('username')
    return redirect("/")

@app.route('/users/<username>/delete', methods=["POST"])
def delete_user(username):

    if "username" not in session or username != session['username']:
        flash("You are not that user", 'danger')
        return redirect(f"/users/{session['username']}")

    user = User.query.get_or_404(username)
    db.session.delete(user)
    db.session.commit()
    session.pop('username')
    return redirect("/")

@app.route('/users/<username>/feedback/add', methods=["GET", "POST"])
def user_feedback(username):
    form = FeedbackForm()
    if "username" not in session or username != session['username']:
        return redirect('/')
    if form.validate_on_submit():
        title = form.title.data
        content = form.content.data
        db.session.add(Feedback(title = title, content=content, username=username ))
        db.session.commit()
        return redirect(f"/users/{session['username']}")
    
    return render_template('add_feedback.html', form=form)

@app.route('/feedback/<int:id>/update', methods=["GET", "POST"])
def update_feedback(id):

    feedback = Feedback.query.get_or_404(id)

    if feedback.username != session['username']:
        flash("You are not that user", 'danger')
        return redirect(f"/users/{session['username']}")
    
    form = FeedbackForm(obj=feedback)

    if form.validate_on_submit():
        feedback.title = form.title.data
        feedback.content = form.content.data
        db.session.commit()
        return redirect(f"/users/{session['username']}")
    
    return render_template('edit_feedback.html', form=form, feedback=feedback)


@app.route('/feedback/<int:id>/delete', methods=["POST"])
def delete_feedback(id):

    if "username" not in session or feedback.username != session['username']:
        flash("You are not this user", "danger")
        return redirect("/")

    feedback = Feedback.query.get_or_404(id)
    db.session.delete(feedback)
    db.session.commit()
    return redirect("/")