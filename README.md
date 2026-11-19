
# team9 写真管理Webアプリ

FlaskとSQLiteを使用した、写真を共有・管理するWebアプリです。

## 開発担当

- 濵川：Read・Delete・List・SQLite・GitHub統合
- 川﨑：Create・Update

## 開発環境

- Python 3.10
- Flask 3.1.3
- SQLite

## 起動方法

```bash
cd team9
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python page_sql/app.py
```

ブラウザで http://127.0.0.1:3000 にアクセスしてください。

## データベース

DBファイル：`page_sql/photos.sqlite`

テーブル名：`photos`

| カラム | 型 | 説明 |
|---|---|---|
| id | INTEGER | 写真ID（自動採番） |
| filename | TEXT | 保存された画像のファイル名（必須） |
| taken_date | TEXT | 撮影日（YYYY-MM-DD） |
| location | TEXT | 撮影場所 |
| description | TEXT | 思い出・説明 |
| deleted | BOOLEAN | 0：通常、1：削除済み |

## 画像の保存場所

`page_sql/static/uploads/`

データベースには画像本体ではなく、保存したファイル名を記録します。

画像表示にはFlaskの `url_for('static', filename='uploads/' + filename)` を使用します。

画像ファイルとSQLiteデータベースはGitHubに登録しません。

## URL一覧

| URL | 機能 | 担当 |
|---|---|---|
| / | トップページ | 共通 |
| /create | 写真登録 | 川﨑 |
| /read | 写真詳細 | 濵川 |
| /update | 写真編集 | 川﨑 |
| /delete | 写真削除 | 濵川 |
| /list | 写真一覧 | 濵川 |

## 開発ルール

- `main`：完成版
- `dev`：統合用
- `kawa`：川﨑の作業用
- `feature-hama`：濵川の作業用（作成予定）

各自のブランチで開発し、Pull Requestを通して`dev`に統合します。

共通の `schema.sql` を変更する場合は、事前に相談してください。

## 現在の状態

Flaskの基本設定、データベース定義、各機能のURLを準備済みです。

Create・Read・Update・Delete・Listの機能本体は今後実装します。
# team9