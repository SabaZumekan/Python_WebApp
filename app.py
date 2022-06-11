from flask import Flask

app = Flask(__name__)


@app.route('/')
def inex():
    return 'Respons Data'

@app.route('/another')
def another():
    return 'Another Response'