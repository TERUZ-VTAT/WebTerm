# WebTerm Ver:1.1
## 起動方法
> 1. `pipenv sync`を使用して仮想環境を作成
> 2. `pipenv shell`で仮想環境を起動
> 3. pythonを使用してapp.pyを起動
## 使用方法
> app.pyの`# メインプログラムをここに記載`と書かれた場所の下にコードを記載
> ### 特殊関数一覧: self.{特殊関数名}と記載することで使用
>> `send`:クライアントにメッセージを送信します。 Pythonのprint関数に相当します。 AAなどを送信する際は、tagを"pre"に設定してください。
>> 
>> `get`:クライアントにメッセージを要求します。 Pythonのinput関数に相当します。
>> 
>> `clear`:ターミナルのログを全て削除します。
