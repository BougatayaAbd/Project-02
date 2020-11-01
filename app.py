from flask import Flask,render_template

app = Flask(__name__)

@app.route('/')
def index():
    names=["Abdoullah", "Abdourrahman", "Fatema", "Hamza", "Zainab"]
    return render_template("index.html", names=names)