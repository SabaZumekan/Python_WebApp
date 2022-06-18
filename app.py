from flask import Flask
from flask import Flask, request
from flask import render_template

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

@app.route('/practice/<user_input>')
def practice(user_input):
    return user_input


@app.route('/show_html')
def show_html():
    return render_template('test_html.html')

@app.route('/exercise_html')
def exercise_html():
    return render_template('exercise.html')

@app.route('/exercise')
def exercise():
    return 'exercise:{request.args.get("my_name")'