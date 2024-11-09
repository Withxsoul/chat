from flask import Flask, render_template
from flask_socketio import SocketIO
app = Flask(__name__)
socketio = SocketIO(app)
@app.route('/')
def index():
    return render_template('index.html')
@socketio.on('send_message')
def handle_message(data):
    socketio.send(data)
if __name__ == '__main__':
    socketio.run(app.run(host='0.0.0.0', port=5000))