from flask import Flask, render_template
from flask_socketio import SocketIO
from flask_cors import CORS

import string
from colormap import rgb2hex


app = Flask(__name__)
socketio = SocketIO(app)
CORS(app, supports_credentials=True, responses={r"/*": {"origins": "*"}})

ids = []
chars = string.ascii_letters + string.punctuation


recv = False
recv_data = ""

opened = None

_appname = ""
_welcome_message = ""
_title = ""


@app.route('/')
def main():
    return render_template("index.html", welcome_message=_welcome_message, appname=_appname, title=_title)


@socketio.on('connect')
def connect():
    opened[0] = True
    pass


@socketio.on('client_data')
def server_recv(msg):
    global recv_data
    recv_data = msg
    global recv
    recv = True


def send(msg: str = "", end: str = "\n", color: tuple | str = None, tag: str = "span"):
    """
    クライアントにメッセージを送信します。
    Pythonのprint関数に相当します。
    AAなどを送信する際は、tagを"pre"に設定してください。
    """
    if color != None:
        color = get_color(color)
    msg += end
    socketio.emit('server_data', {
                  'msg': msg, 'input_mode': False, 'color': color, 'tag': tag})


def get_color(val):
    if type(val) == tuple:
        return rgb2hex(val[0], val[1], val[2])
    elif type(val) == str:
        if val[0] != "#" and len(val) <= 6:
            val = f"#{val}"
        return val


def set_opened(data):
    global opened
    opened = data


def get(msg: str = ""):
    """
    クライアントにメッセージを要求します。
    Pythonのinput関数に相当します。
    """
    socketio.emit('server_data', {'msg': msg, 'input_mode': True})
    global recv
    while not recv:
        pass
    recv = False
    global recv_data
    return recv_data


def clear():
    """
    ターミナルのログを全て削除します。
    """
    socketio.emit('clear_logs')


def set_welcome_message(msg):
    """
    ターミナル起動時の初期メッセージを設定します。
    """
    global _welcome_message
    _welcome_message = msg


def set_appname(name):
    """
    タブに表示されるアプリケーション名を設定します。
    初期値:WebTerm
    """
    global _appname
    _appname = name


def set_title(title):
    """
    タブに表示されるタイトルを設定します。
    """
    global _title
    _title = title


def start_server():
    socketio.run(app, host='0.0.0.0', port=5002,
                 debug=True, use_reloader=False)


if __name__ == '__main__':
    start_server()
