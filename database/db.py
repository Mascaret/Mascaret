#Python Libs imports
import pymysql
from database.logical_objects.entjur import EntJur,ListEntJur

#Class of the dtb
class MyDB(object):
    _db_connection = None
    _db_cur = None

    def __init__(self):
        try:
            self._db_connection = pymysql.connect('localhost', 'root', '', 'mascaretdb7')
        except:

        self._db_cur = self._db_connection.cursor()
        self._db_connection.autocommit(False)

    def query(self, query, params):
        self._db_cur.execute(query, params)

    def db_fetchall(self):
        return self._db_cur.fetchall()

    def __del__(self):
        self._db_connection.close()

    def commit(self):
        self._db_connection.commit()

    def rollback(self):
        self._db_connection.rollback()

    def get_all_ent_jur(self):
        get_all_legal_entities_query = "SELECT *FROM EntiteJuridique;"
        try:
            self.query(get_all_legal_entities_query,[])
            self.commit()
        except:
            self.rollback()
        #On obtient une matrice
        legal_entities_data = self.db_fetchall()
        # Liste d'entite Juridique
        data_ent_jur = ListEntJur(legal_entities_data)

        return data_ent_jur
