from flask import Flask
from flask import Flask, request

app = Flask(__name__)


@app.route('/')
def inex():
    return 'Respons Data'

@app.route('/another')
def another():
    return 'Another Response'

@app.route('/test_request')
def test_request():
    return f'test_request:{request.args.get("dummy")}'

@app.route('/practice_request/<user_input>')
def test_request():
    return f'test_request:{request.args.get("user_imput")}'