#自主学習
from flask import Flask, request, redirect, url_for
import datetime
app = Flask(__name__)
#アクセスによって異なるものを表示
@app.route("/")
def index():
    return """
    <h1>ようこそ！</h1>
    <p>トップページです。</p>
    <p><a href="/time">今の時間を知りたい？</a></p>
    <form action="/go_hello" method="post">
        <input type="text" name="username" placeholder="名前を入力してください">
        <input type="submit" value="移動">
    </form>
    """

# 入力を受け取り、/hello/<name> にリダイレクトする
@app.route("/go_hello", methods=["POST"])
def go_hello():
    name = request.form.get("username", "ゲスト")
    return redirect(url_for("hello", name=name))

@app.route("/time")
def time():
    now = datetime.datetime.now()
    return f"""
    <h1>Hello!</h1>
    <p>今の時間は {now:%Y-%m-%d %H:%M:%S} です。</p>
    <a href="/">トップページに戻る</a>
    """

@app.route("/hello/<name>")
def hello(name):
    return f"""
    <h1>Hello, {name}!</h1>
    <p>ここは{name}のためだけの空間です。ちょっとくらいゆっくりしていってよ</p>
    <a href="/again">トップページに戻る</a>
    """

@app.route("/again")
def again():
    return f"""
    <h1>だまされた？</h1>
    <p>嘘ついてごめんね。やっぱりもうちょっとゆっくりしていかない？休息も大事だよ</p>
    <a href="/">本当にトップページに戻る</a>
    <a href="/hello/<name>">やっぱりもうちょっとゆっくりしていく</a>
    """