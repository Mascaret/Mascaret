#Python Libs imports
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.listview import ListItemButton
import pymysql
from kivy.properties import ObjectProperty, StringProperty

#Personnal Libs imports
from database.db import MyDB
from database.logical_objects.entjur import LegalEntity,ListLegalEntity
from database.logical_objects.location import Location,ListLocationFromFetch
from gui.widgets.menu_deroulant import Menu_Deroulant

#Class of the Location Form.
class Formulaire_Location(RelativeLayout):
    new_location_box = ObjectProperty()
    location_listbox = ObjectProperty()
    ent_jur_button = ObjectProperty()

    #Add
    def send_new_location(self):
        print(self.new_location_box.text)
        print(self.ent_jur_button.id_object)
        data_location = self.location_listbox.get_location_list()

        self.check_existence_of_new_location_and_add_it(data_location)


    def check_existence_of_new_location_and_add_it(self, data_location):

        #DB CONNECTION
        db = MyDB()
        
        location_exist = False
        for row in data_location:
            if row.intitule == self.new_location_box.text:
                print("This Location already exists")
                location_exist = True

        if location_exist == False:

##            try:
            idEntJur= self.ent_jur_button.id_object

            add_permission_query = "INSERT INTO `permission` (`idPermission`) VALUES (NULL) ;"
            db.query(add_permission_query,[])

            get_idpermission_query = "SELECT P.idPermission AS Id FROM permission P ORDER BY P.idPermission DESC LIMIT 1;"
            db.query(get_idpermission_query,[])
            get_permission_id_data = db.db_fetchall()

            add_location_query = """INSERT INTO `location` (idLoc, intitule, idEntJur)
                                    VALUES (%s,%s,%s);"""

            parameters_query = [get_permission_id_data,self.new_location_box.text,idEntJur]
            db.query(add_location_query,parameters_query)
            db.commit()
##            except:
##                db.rollback()

            self.new_location_box.text = ""
            self.location_listbox.location_listview.adapter.data = self.location_listbox.get_location_list()

#Class of the Location List Items
class Location_List_Item(BoxLayout, ListItemButton):
    id_location = StringProperty()
    name_location = StringProperty()
    id_ent_jur_cor = StringProperty()

#Class of the Location List
class Location_List(BoxLayout):
    location_listview= ObjectProperty()

    def location_converter(self, index, location):
        result = {
            "id_location": str(location.Id),
            "name_location": str(location.intitule),
            "id_ent_jur_cor": str(location.id_cor1)
        }
        return result

    def get_location_list(self):

        #DB CONNECTION
        db = MyDB()
        #Execute la requete SQL
        get_all_location_query = "SELECT * FROM Location;"

        try:
            db.query(get_all_location_query,[])

            db.commit()
        except:
            db.rollback()
        #On obtient une matrice
        location_data = db.db_fetchall()

        # Liste d'entite Juridique
        data_location = ListLocationFromFetch(location_data)
        
        return data_location

#Class of a list of Ent Jur trigered by clickiing on a button
class Menu_Deroulant_Ent_Jur(Menu_Deroulant):

    def get_object_list(self):
        
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

