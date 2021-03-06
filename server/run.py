"""
    Web server for the speech learning task app.
"""

from flask import Flask, request
from threading import Thread

from pepper_server import serve_grpc, CommandBridge
from slack_bot import publish_hostname

app = Flask(__name__, static_url_path='')


@app.route('/')
def home():
    return app.send_static_file('index.html')


@app.route('/pubCommand', methods=['POST'])
def pubCommand():
    req = request.get_json()
    print(req)
    cb = CommandBridge()
    cb.send_command(req)
    return "Ok"


@app.route('/control', defaults={'path': ''})
def index(path):
    return app.send_static_file('index.html')


if __name__ == '__main__':
    publish_hostname()
    grpc = Thread(target=serve_grpc)
    grpc.start()
    app.run(host='0.0.0.0', port='5002')
