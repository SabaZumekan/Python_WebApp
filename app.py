from flask import Flask
from flask import Flask, request
from flask import render_template
from flask import jsonify

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
    return f'name:{request.args.get("my_name")}'

@app.route('/try_rest', methods=['POST'])
def try_rest():
    # リクエストデータをJSONとして受け取る
    request_json = request.get_json()
    print(request_json)
    print(type(request_json))
    name = request_json['name']
    print(name)
    response_json = {"response_json": request_json}
    return jsonify(response_json)

"""
@app.route('/practice_rest', methods=['POST'])
def practice_rest():
    request_json = request.get_json()
    print(request_json)
    print(type(request_json))
    friends = request_json['friends']
    print(friends)
    for array_friend in friends:
        print(array_friend)
    
    response_json = response.json()
    response_json['response_json']['friends']

"""