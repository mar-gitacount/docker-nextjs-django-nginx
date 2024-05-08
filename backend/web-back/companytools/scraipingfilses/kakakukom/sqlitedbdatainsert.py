import sqlite3

def connect_db():
    return sqlite3.connect('kakakukomo.db')

def insert_watch_item(kakakukom_watch_id, model_name, ref, bracelet, dial, url):
    conn = connect_db()
    c = conn.cursor()
    try:
        print(f"価格コムのID：{type(kakakukom_watch_id)} モデル名:{type(model_name)} リファレンス:{type(ref)} ブレスレット:{type(bracelet)} ダイアル:{type(dial)} URL:{type(url)}")
        c.execute('''
        INSERT INTO watch_item (kakakukom_watch_id, model_name, ref, bracelet, dial, url)
        VALUES (?, ?, ?, ?, ?, ?)
        ''', (kakakukom_watch_id, model_name, ref, bracelet, dial, url))
        conn.commit()
    except sqlite3.IntegrityError as e:
        print(f"データ挿入に失敗しました。制約違反が発生しました: {e}")
    except Exception as e:
        print(f"予期せぬエラーが発生しました: {e}")
    finally:
        conn.close()

def insert_weekly_report(week_start_date, ranking, summary, price, kakakukom_watch_id):
    conn = connect_db()
    c = conn.cursor()
    c.execute('''
    INSERT INTO weekly_reports (week_start_date, ranking, summary, price, kakakukom_watch_id)
    VALUES (?, ?, ?, ?, ?)
    ''', (week_start_date, ranking, summary, price, kakakukom_watch_id))
    conn.commit()
    conn.close()
