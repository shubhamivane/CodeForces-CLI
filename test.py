import sqlite3
conn = sqlite3.connect('cfcliDB.sqlite3')
cursor = conn.cursor()
result = cursor.execute('SELECT * FROM User WHERE username = ?', ('shubhamivane',))
print(result.fetchone())
