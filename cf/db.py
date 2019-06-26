import sqlite3

USER_TABLE = """
    CREATE TABLE IF NOT EXISTS User(
        username text PRIMARY KEY,
        password text NOT NULL,
        logged_in integer
    )
"""

def connection():
    conn = sqlite3.connect('cfcliDB.sqlite3')
    conn.execute(USER_TABLE)
    return conn

def logged_in():
    flag = True
    error = None
    try:
        conn = connection()
        cursor = conn.cursor()
        sql = 'SELECT * FROM User WHERE logged_in = 1'
        result = cursor.execute(sql)
        row = result.fetchone()
        if not row is None:
            error = row[0]
        else:
            flag = False
            error = 'No one is logged in'
    except sqlite3.IntegrityError as error:
        flag = False
    else:
        conn.close()
        return flag, error

def login(username, password):
    flag = True
    error = None
    try:
        conn = connection()
        cursor = conn.cursor()
        credentials = (username, password)
        sql = 'SELECT * FROM User WHERE username = ? AND password = ?'
        result = cursor.execute(sql, credentials) # query returns None if no row is selected
        row = result.fetchone()
        if not row is None:
            cursor.execute('UPDATE User SET logged_in = 1 WHERE username = ? ',(username,))
            conn.commit()
            return flag, ''
        else:
            sql = 'SELECT * FROM User WHERE username = ?'
            result = cursor.execute(sql, (username,))
            row = result.fetchone()
            if not row is None:
                return flag, 'Try on CodeForces'
            flag = False
            error = 'Invalid username or password'
    except sqlite3.IntegrityError as error:
        flag = False
    else:
        conn.close()
        return flag, error     

def logout():
    flag = True
    error = None
    try:
        conn = connection()
        cursor = conn.cursor()
        flag, username = logged_in()
        if flag:
            sql = 'UPDATE User SET logged_in = 0 WHERE username = ?'
            cursor.execute(sql, (username,))
            error = '{} is successfully logged out'.format(username)
        else:
            flag = False
            error = 'No user is logged in'
        conn.commit()    
    except sqlite3.IntegrityError as error:
        flag = False
    else:
        conn.close()
        return flag, error        

def update(username, password):
    flag = True
    error = None
    try:
        conn = connection()
        cursor = conn.cursor()
        sql = 'UPDATE User SET password = ? WHERE username = ?'
        ip = (password, username)
        cursor.execute(sql, ip)
        return flag, ''
    except sqlite3.IntegrityError as error:
        flag = False
    except:
        error = 'unknown error'
        flag = False
    else:
        conn.close()
        return flag, error

def write(username, password):
    flag = True
    error = None
    try:
        conn = connection()
        cursor = conn.cursor()
        sql = 'INSERT INTO User VALUES (?, ?, ?)'
        cursor.execute(sql, (username, password, 1))
        conn.commit()
    except sqlite3.IntegrityError as error:
        flag = False
    else:
        conn.close()
        return flag, error

if __name__ == "__main__":
    print(logged_in())