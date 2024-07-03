from sysfiles.WebTerm import set_appname, set_title, start_server, set_opened, set_queue, set_welcome_message
from sysfiles.socsys import socsys
import threading

run = [False]
queue = []


# アプリケーション名(任意)
app_name = ""
# ページタイトル(任意)
title = ""
# 参加時のメッセージ(任意)
welcome_message = ""


class main(socsys):
    def __init__(self, id):
        self.id = id
        # メインプログラムをここに記載
        pass


if __name__ == '__main__':
    set_opened(run)
    set_queue(queue)
    set_appname(app_name)
    set_title(title)
    set_welcome_message(welcome_message)
    
    server_thread = threading.Thread(target=start_server)
    server_thread.start()
    while True:
        if len(queue) != 0:
            main_thread = threading.Thread(target=main, args=(queue[0],))
            main_thread.start()
            queue.pop(0)
