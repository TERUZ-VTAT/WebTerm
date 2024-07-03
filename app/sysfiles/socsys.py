from sysfiles.WebTerm import send, get, clear


class socsys:
    id = ""

    def send(self, msg: str = "", end: str = "\n", color: tuple | str = None, tag: str = "span"):
        """
        クライアントにメッセージを送信します。
        Pythonのprint関数に相当します。
        AAなどを送信する際は、tagを"pre"に設定してください。
        """
        return send(self.id, msg, end, color, tag)

    def get(self, msg: str = ""):
        """
        クライアントにメッセージを要求します。
        Pythonのinput関数に相当します。
        """
        data = get(self.id, msg)
        client_msg = data['msg']
        client_id = data['id']
        self.id = client_id
        return client_msg

    def clear(self):
        """
        ターミナルのログを全て削除します。
        """
        return clear(self.id)
