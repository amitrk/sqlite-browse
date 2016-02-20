import sqlite3

db = sqlite3.connect('appdata.db')
#cur = db.execute("SELECT * FROM sqlite_master WHERE type='table'")
cur = db.execute("pragma table_info(team)")
result = cur.fetchall()

for item in result:
    print(item)
