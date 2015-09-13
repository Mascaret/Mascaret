#Python Libs imports
import pymysql

#Personnal Libs imports
from gui.widgets.menu_deroulant import Menu_Deroulant
from database.db import MyDB
from database.logical_objects.entjur import EntJur,ListEntJur

#Class of a list of Ent Jur trigered by clickiing on a button
class Menu_Deroulant_Ent_Jur(Menu_Deroulant):

    def get_ent_jur_list(self):
        
        #DB CONNECTION
        db = MyDB()
        #Execute la requete SQL
        get_all_legal_entities_query = "SELECT *FROM EntiteJuridique;"

        try:
            db.query(get_all_legal_entities_query,[])
            db.commit()
        except:
            db.rollback()
        #On obtient une matrice
        legal_entities_data = db.db_fetchall()

        # Liste d'entite Juridique
        data_ent_jur = ListEntJur(legal_entities_data)
        
        return data_ent_jur
