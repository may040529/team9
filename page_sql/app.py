import os
import sqlite3
from flask import Flask, render_template, request, g, redirect, url_for

app = Flask(__name__)

# アプリのフォルダ
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# データベースの保存場所
DBFILE = os.path.join(BASE_DIR, 'photos.sqlite')

# 写真の保存場所
UPLOAD_FOLDER = os.path.join(BASE_DIR, 'static', 'uploads')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# 写真保存用フォルダを作成
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

def init_db():
    with app.app_context():
        db = connect_db()
        with app.open_resource('schema.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()
        db.close()

# データベースに接続する関数
def connect_db():
    # SQLiteデータベースに接続
    conn = sqlite3.connect(DBFILE)
    return conn

# before_requestフックでリクエストごとに接続を確立
@app.before_request
def before_request():
    # データベース接続を作成し、gオブジェクトに保存
    g.db = connect_db()

# teardown_requestフックでリクエスト終了時に接続を切断
@app.teardown_request
def teardown_request(exception):
    # 接続がある場合は切断
    db = getattr(g, 'db', None)
    if db is not None:
        db.close()


# 写真管理用データベースを初期化
with app.app_context():
    init_db()
    
#     cur=g.db.cursor()
#     cur.execute(query_create_table)        
#     g.db.commit()
#     teardown_request(exception=None)

with app.app_context():
#    before_request()
    init_db()
#    teardown_request(exception=None)


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


# Create：川﨑担当
@app.route('/create', methods=['GET', 'POST'])
def create():
    return "Create機能は開発中です"


# Read：濵川担当
@app.route('/read', methods=['GET'])
def read():
    return "Read機能は開発中です"


# Update：川﨑担当
@app.route('/update', methods=['GET', 'POST'])
def update():
    return "Update機能は開発中です"


# Delete：濵川担当
@app.route('/delete', methods=['GET', 'POST'])
def delete():
    return "Delete機能は開発中です"


# List：濵川担当
@app.route('/list', methods=['GET'])
def list_photos():
    return "List機能は開発中です"


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=3000, debug=True)
