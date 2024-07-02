from WebTerm import send, get, clear, set_welcome_message, set_appname, set_title, start_server
import threading


def main_program():
    # メインプログラムをここに記載
    pass

if __name__ == '__main__':
    server_thread = threading.Thread(target=start_server)
    server_thread.start()

    main_program()
