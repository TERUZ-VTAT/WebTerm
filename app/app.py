from WebTerm import send, get, clear, set_welcome_message, set_appname, set_title, start_server, set_opened
import threading

run = [False]

# 参加時のメッセージをここに記載(任意)
welcome_message = ""


def main_program():
    # メインプログラムをここに記載
    pass


if __name__ == '__main__':
    set_opened(run)
    set_welcome_message(welcome_message)
    server_thread = threading.Thread(target=start_server)
    server_thread.start()
    while True:
        if run[0]:
            break
    main_program()
