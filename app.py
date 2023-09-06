from flask import Flask, render_template
from flask_socketio import SocketIO

app = Flask(__name__)
socketio = SocketIO(app)

@app.route("/")
def home():
    return render_template('index.html')

@socketio.on('chat msg')
def handle_message(data):
    socketio.emit("chat msg", data)

@socketio.on('connect')
def handle_message(data):
    print('new friend!')

if __name__ == '__main__':
    socketio.run(app)