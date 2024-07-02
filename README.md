# WebTerm Ver:1.1
## 起動方法
> 1. `pipenv sync`を使用して仮想環境を作成
> 2. `pipenv shell`で仮想環境を起動
> 3. pythonを使用してapp.pyを起動
## 使用方法
> app.pyのmain_program関数の中にコードを記載
> ### 特殊関数一覧
>> `send`:クライアントにメッセージを送信します。 Pythonのprint関数に相当します。 AAなどを送信する際は、tagを"pre"に設定してください。
>> `get`:クライアントにメッセージを要求します。 Pythonのinput関数に相当します。
>> `clear`:ターミナルのログを全て削除します。
>> `set_welcome_message`:ターミナル起動時の初期メッセージを設定します。
>> `set_appname`:タブに表示されるアプリケーション名を設定します。 初期値:WebTerm
>> `set_title`:タブに表示されるタイトルを設定します。