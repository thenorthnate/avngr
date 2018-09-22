# AVNGR Application Server
# Analyze, Visualize, Navigate, then Go Render
# Nathan North


from flask import (
    Flask,
    jsonify,
    request,
    # render_template
)
from flask_cors import CORS
import os
from app.Helper import Helper


HLPR = Helper()

# configuration
DEBUG = True

# instantiate the app and set configuration items
app = Flask(__name__, static_folder="../client/dist/static", template_folder="../client/dist")
app.config.from_object(__name__)
app.config['SECRET_KEY'] = 'avngr-develop-key'
CORS(app)  # enable CORS
port = os.getenv("PORT")
if port is None:
    port = 5000


# @app.route('/')
# def index():
    # return render_template("index.html")

@app.route('/api/init', methods=['GET'])
def inital_request():
    return jsonify(HLPR.init_request())


@app.route('/api/data', methods=['POST'])
def handle_data():
    reply = {}
    if request.method == 'POST':
        requestJson = request.get_json()
        reply = HLPR.handle_request(requestJson, 'json')
    return jsonify(reply)


@app.route('/api/files', methods=['POST'])
def file_upload():
    reply = ""
    if request.method == 'POST':
        reply = HLPR.handle_request(request, 'file')
    return jsonify(reply)


if __name__ == '__main__':
    app.run(host='0.0.0.0')
