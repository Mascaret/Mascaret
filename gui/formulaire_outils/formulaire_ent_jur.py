#Python Libs imports
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.listview import ListItemButton
import pymysql
from kivy.properties import ObjectProperty, StringProperty

#Personnal Libs imports
from database.db import MyDB
from database.logical_objects.entjur import LegalEntity, ListLegalEntity

#Class of the Legal Entity Form.
class Formulaire_Ent_Jur(FloatLayout):
    new_legal_entity_box = ObjectProperty()
    list_ent_jur_box = ObjectProperty()

    #Add
    def send_new_legal_entity(self):
        print(self.new_legal_entity_box.text)

        data_ent_jur = self.list_ent_jur_box.get_ent_jur_list()

        self.check_existence_of_new_ent_jur_and_add_it(data_ent_jur)

    def check_existence_of_new_ent_jur_and_add_it(self, data_ent_jur):

        #DB CONNECTION
        db = MyDB()

        entity_exist = False
        for row in data_ent_jur:
            if row.intitule == self.new_legal_entity_box.text:
                print("This Legal Entity already exists")
                entity_exist = True
        if entity_exist == False:
            add_legal_entity_query = "INSERT INTO `entitejuridique` (`intitule`) VALUES (%s) ;"

            parameters_query = [str(self.new_legal_entity_box.text)]

            try:
                db.query(add_legal_entity_query,parameters_query)
                db.commit()
            except:
                db.rollback()

            self.new_legal_entity_box.text = ""
            self.list_ent_jur_box.ent_jur_listview.adapter.data = self.list_ent_jur_box.get_ent_jur_list()

#Class of the Ent Jur List Items
class Jur_Ent_List_Item(BoxLayout, ListItemButton):
    id_jur_ent = StringProperty()
    name_jur_ent = StringProperty()

#Class of the Ent Jur List
class Jur_Ent_List(BoxLayout):
    ent_jur_listview = ObjectProperty()

    def ent_jur_converter(self, index, ent_jur):
        result = {
            "id_jur_ent": str(ent_jur.a_index),
            "name_jur_ent": str(ent_jur.a_name)
        }
        return result

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
        data_ent_jur = ListLegalEntity(legal_entities_data)

        return data_ent_jur
