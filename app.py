from operator import truediv
from flask import Flask, render_template, request, session, url_for
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.secret_key = '1q2w3e$R'

@app.route('/', methods=['POST', 'GET'])
def index():
    if 'username' in session:
        render_template("index.html", )
    #return 'Hello, My First Flask!'
    return render_template("index.html")

@app.route("/market")
def MarketInfo():
    return render_template("market.html")

@app.route("/about")
def AboutUs():
    return render_template("about.html")

@app.route("/board")
def board():
    return render_template('board.html')

@app.route("/login")
def login():
    return "login"

@app.route("/registration")
def registration():
    return "registration"


if __name__ == "__main__":
    app.run(debug=True)
