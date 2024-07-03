from flask import Flask, render_template
from flask_socketio import SocketIO, join_room
from flask_cors import CORS

import string
from colormap import rgb2hex
import random


app = Flask(__name__)
socketio = SocketIO(app)
CORS(app, supports_credentials=True, responses={r"/*": {"origins": "*"}})

ids = []
queue = []


recv = False
recv_data = {}

_appname = ""
_welcome_message = ""
_title = ""


@app.route('/')
def main():
    return render_template("index.html", welcome_message=_welcome_message, appname=_appname, title=_title)


@socketio.on('connect')
def connect():
    new_id = ""
    while True:
        new_id = ''.join(random.choice(string.ascii_letters) for _ in range(7)) + "=" + ''.join(random.choice(string.ascii_letters) for _ in range(3))
        global ids
        if not new_id in ids:
            ids.append(new_id)
            break
    join_room(f"{new_id}")
    socketio.emit('set_id', new_id, to=new_id)
    queue.append(new_id)


def set_opened(data):
    global opened
    opened = data


def set_queue(data):
    global queue
    queue = data



@socketio.on('client_data')
def server_recv(data):
    global recv_data
    recv_data = data
    global recv
    recv = True


def send(id, msg: str = "", end: str = "\n", color: tuple | str = None, tag: str = "span"):
    if color != None:
        color = get_color(color)
    msg += end
    socketio.emit('server_data', {
                  'msg': msg, 'input_mode': False, 'color': color, 'tag': tag}, to=id)


def get_color(val):
    if type(val) == tuple:
        return rgb2hex(val[0], val[1], val[2])
    elif type(val) == str:
        if val[0] != "#" and len(val) <= 6:
            val = f"#{val}"
        return val


def get(id, msg: str = ""):
    socketio.emit('server_data', {'msg': msg, 'input_mode': True}, to=id)
    global recv
    while not recv:
        pass
    recv = False
    global recv_data
    return recv_data


def clear(id):
    socketio.emit('clear_logs', to=id)



def set_welcome_message(msg):
    global _welcome_message
    _welcome_message = msg


def set_appname(name):
    global _appname
    _appname = name


def set_title(title):
    global _title
    _title = title


def start_server():
    socketio.run(app, host='0.0.0.0', port=5002,
                 debug=True, use_reloader=False)


if __name__ == '__main__':
    start_server()
