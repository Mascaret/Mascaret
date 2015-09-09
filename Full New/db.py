import pymysql

class MyDB(object):
    _db_connection = None
    _db_cur = None

    def __init__(self):
        self._db_connection = pymysql.connect('localhost', 'root', '', 'mascaretdb6')
        self._db_cur = self._db_connection.cursor()

    def query(self, query, params):
        self._db_cur.execute(query, params)

    def db_fetchall(self):
        return self._db_cur.fetchall()

    def __del__(self):
        self._db_connection.close()
