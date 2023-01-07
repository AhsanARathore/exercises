from flask import Flask, request, render_template, redirect, flash
from flask_debugtoolbar import DebugToolbarExtension
from surveys import satisfaction_survey as survey

app = Flask(__name__)

app.config['SECRET_KEY'] = "secret"

responses = []

@app.route("/")
def start_page():
    return render_template("start_page.html", survey=survey)

@app.route("/begin", methods=["POST"])
def first_question():
   return redirect("/questions/0")

@app.route("/questions/<int:qnum>")
def show_question(qnum):
    question = survey.questions[qnum]
    if (len(responses) != qnum):
        flash("wrong question please answer this one first")
        return redirect(f"/questions/{len(responses)}")
    return render_template("question.html",question=question)

@app.route("/answer", methods=["POST"])
def answer():
    responses.append(request.form['answer'])
    if (len(responses) == len(survey.questions)):
        return redirect("/complete")
    else:
        return redirect(f"/questions/{len(responses)}")

@app.route("/complete")
def all_done():
    return render_template("complete.html")