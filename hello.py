#flaskからFlaskクラスをインポート
from flask import Flask
#Flaskクラスのインスタンスを作って app 変数に入れる
app = Flask(__name__)

#/(ルート)にアクセスしたら次に書く変数(hello_world)を実行するという宣言.
@app.route("/") #"/" は「ルート」と呼ばれる部分で、つまりWebサイトの一番最初のページにアクセスしたら以下の関数を実行するという意味
def hello_world():
    return "<p>Hello,World!<p>"
