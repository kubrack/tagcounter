
import pickle
import sqlite3
import sys
import datetime
import sys

class DB:
    # non-instantiable singleton
    db = 'tagcounter.db'
    dbh = None

    def init():
        try:
            DB.dbh = sqlite3.connect(DB.db)
            c = DB.dbh.cursor()
            c.execute('''CREATE TABLE urls (url text primary key, date text, tags blob)''')
            DB.dbh.commit()
        except Exception as err:
            if not type(err) == sqlite3.OperationalError:
                # sqlite3.OperationalError 'table urls already exists' is expected, ignoring
                sys.stderr.write('AliasDB issue: ' + str(err) +', type: '+ str(type(err)) +'. Proceed without DB.' +'\n')

    def get(key):
        if not DB.dbh: return
        c = DB.dbh.cursor()
        c.execute('''SELECT * FROM urls WHERE url = ?''', (key,))
        fetched = c.fetchone()
        if fetched: return pickle.loads(fetched[2])
        
    def set(key, value):
        if not DB.dbh: return
        c = DB.dbh.cursor()
        now =  str(datetime.datetime.now())
        tags = pickle.dumps(value)
        c.execute('''insert INTO urls VALUES(?,?,?) ON CONFLICT(url) DO UPDATE SET date = ?, tags = ?;''', (key, now, tags, now, tags,))
        DB.dbh.commit()
