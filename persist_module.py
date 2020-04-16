import sqlite3

DATABASE = 'search.db'


def get_db():
    db = sqlite3.connect(DATABASE)
    return db


def persist_to_db(table_name='search_table',
                  field_name='search_keyword',
                  value='keyword'):
    try:
        create_table()
        print('Saving data to database : ', value)
        conn = get_db()
        cur = conn.cursor()
        sql = 'INSERT INTO ' + table_name + ' (' + field_name + ') values(?)'
        cur.execute(sql, (value,))
        conn.commit()
    except Exception as e:
        print('Persiting to db failed due to :', str(e))

def get_all_row(table_name='search_table'):
    conn = get_db()
    cur = conn.cursor()
    sql = 'SELECT * FROM ' + table_name
    cur.execute(sql)
    query_result = cur.fetchall()
    conn.commit()
    print('DB Entries : ', query_result)
    return query_result


def create_table(table_name='search_table',
                 field_name='search_keyword'):  # This can be made generic by making allowing multiple field name arg
    print('Application initialized, creating databases tables')
    try:
        conn = get_db()
        cur = conn.cursor()
        create_table_search = 'CREATE TABLE IF NOT EXISTS ' + table_name + ' (' + field_name + ' TEXT)'
        cur.execute(create_table_search)
        conn.close()
    except Exception as e:
        print('Exception occured while creating table', str(e))
        conn.close()


# Fist time create table
#create_table()
#persist_to_db(value='end game')
#get_all_row()
