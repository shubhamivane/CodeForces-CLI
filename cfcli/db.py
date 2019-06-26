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
        with conn:
            sql = 'SELECT * FROM User WHERE logged_in = 1'
            cursor = conn.execute(sql)
            if not cursor is None:
                result = cursor.fetchone()
                error = result[0]
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
        with conn:
            credentials = tuple(username, password)
            sql = 'SELECT * FROM User WHERE username = ? AND password = ?'
            cursor = conn.execute(sql, credentials) # query returns None if no row is selected
            if not cursor is None:
                conn.execute('UPDATE User SET logged_in = 1 WHERE username = ? ',(username))
                return flag, ''
            else:
                sql = 'SELECT * FROM User WHERE username = ?'
                cursor = conn.execute(sql, (username,))
                if not cursor is None:
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
        with conn:
            flag, username = logged_in()
            if flag:
                sql = 'UPDATE User SET logged_in = 0 WHERE username = ?'
                conn.execute(sql, (username))
                error = '{} is successfully logged out'.format(username)
            else:
                flag = False
                error = 'No user is logged in'
            
    except sqlite3.IntegrityError as error:
        flag = False
    else:
        conn.close()
        return flag, error        
            