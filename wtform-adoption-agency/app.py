from flask import Flask, request, render_template,  redirect, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Pet
from forms import AddPetForm, EditPetForm

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///petadopt'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = "password"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)

connect_db(app)

@app.route("/pets")
def pets_list():
    """renders pet index"""
    pets = Pet.query.all()
    return render_template('pet_index.html', pets=pets)

@app.route("/new_pet", methods=["GET", "POST"])
def new_pet():
    form = AddPetForm()
    if form.validate_on_submit():
        name = form.name.data
        species = form.species.data
        photo_url = form.photo_url.data
        age = form.age.data
        notes = form.notes.data
        pet = Pet(name=name, species=species, photo_url=photo_url, age=age, notes=notes)
        db.session.add(pet)
        db.session.commit()
        return redirect("/pets")
    else:
        return render_template("add_pet_form.html", form=form)
    
@app.route("/pets/<int:id>", methods=["Get","Post"])
def edit_pet(id):
    pet = Pet.query.get_or_404(id)
    form= EditPetForm(obj=pet)
    if form.validate_on_submit():
        pet.photo_url = form.photo_url.data
        pet.notes = form.notes.data
        pet.available = form.available.data
        db.session.commit()
        return redirect("/pets")
    else:
        return render_template('edit_pet_form.html', form=form, pet=pet)
        
@app.route('/pets/<int:id>/delete', methods=["POST"])
def delete_user(id):
    id = Pet.query.get_or_404(id)
    db.session.delete(id)
    db.session.commit()
    return redirect("/pets")