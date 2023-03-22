from boggle import Boggle
from flask import Flask, request, render_template, session

app = Flask(__name__)
app.config["SECRET_KEY"] = "secret"

boggle_game = Boggle()

@app.route("/")
def board_page():
    board = boggle_game.make_board()
    session['board'] = board
    return render_template('index.html', board=board)