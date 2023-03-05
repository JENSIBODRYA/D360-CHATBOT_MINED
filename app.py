import flask
import os
from flask import send_from_directory, request
import jsonify
app = flask.Flask(_name_)

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/favicon.png')

@app.route('/')
@app.route('/home')
def home():
    return "Hello World"

@app.route('/webhook', methods=['POST'])
def webhook():
    req = request.get_json(force=True)
    print(req)
    return jsonify({
        'fulfillmentText': 'Hello from the other side.'
    })

if _name_ == "_main_":
    app.secret_key = 'ItIsASecret'
    app.debug = True
    app.run(port=5000)
