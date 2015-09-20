#Python Libs imports
import pymysql
from database.logical_objects.entjur import EntJur,ListEntJur

#Class of the dtb
class MyDB(object):
    _db_connection = None
    _db_cur = None

    def __init__(self):
        self._db_connection = pymysql.connect('localhost', 'root', '', 'mascaret7')
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

    def check_existence_of_new_ent_jur_and_add_it_db(self,data_ent_jur,entity_text):
        entity_exist = False
        for row in data_ent_jur:
            if (row.intitule == entity_text):
                print("This Legal Entity already exists")
                entity_exist = True
        if entity_exist == False:
            add_legal_entity_query = "INSERT INTO `entitejuridique` (`intitule`) VALUES (%s) ;"

            parameters_query = [str(entity_text)]

            try:
                self.query(add_legal_entity_query,parameters_query)
                self.commit()
            except:
                self.rollback()
        return entity_exist
