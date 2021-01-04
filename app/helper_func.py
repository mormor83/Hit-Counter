import sqlite3

def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)
    return conn

def create_table(conn, create_table_sql):
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)

def insert_initial_value(conn, value):
    try:
        sql = ''' INSERT INTO hits_counter(hits)
              VALUES(?) '''
        cur = conn.cursor()
        cur.execute(sql, value)
        conn.commit()
    except Error as e:
        print(e)
    #return cur.lastrowid

def update_value(conn, value):
    try:
        sql = ''' UPDATE hits_counter
              SET hits = hits + ?
        '''
        cur = conn.cursor()
        cur.execute(sql, value)
        conn.commit()
    except Error as e:
        print(e)

def select_hits_count(conn):
    try:
        cur = conn.cursor()
        cur.execute("SELECT hits FROM hits_counter")
        rows = cur.fetchall()
    except Error as e:
        print(e)
    return rows[0]

def reset_hit_count(conn):
    try:
        sql = ''' UPDATE hits_counter
              SET hits = 0
        '''
        cur = conn.cursor()
        cur.execute(sql)
        conn.commit()
    except Error as e:
        print(e)