#Python Libs imports
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.listview import ListItemButton
import pymysql
from kivy.properties import ObjectProperty, StringProperty
from kivy.uix.dropdown import DropDown

#Personnal Libs imports
from database.db import MyDB
from database.logical_objects.entjur import LegalEntity, ListLegalEntity
from database.logical_objects.service import Service,ListServiceFromFetch
from gui.widgets.menu_deroulant import Menu_Deroulant
from database.logical_objects.center import Center,ListCenterFromFetch

#Class of the Center Form.
class Formulaire_Center(RelativeLayout):
    new_center_int_box = ObjectProperty()
    new_center_desc_box = ObjectProperty()
    center_listbox = ObjectProperty()
    service_button = ObjectProperty()

    #Add
    def send_new_center(self):
        print(self.new_center_int_box.text)
        print(self.service_button.id_object)
        data_center = self.center_listbox.get_center_list()

        self.check_existence_of_new_center_and_add_it(data_center)


    def check_existence_of_new_center_and_add_it(self, data_center):

        #DB CONNECTION
        db = MyDB()

        center_exist = False
        for row in data_center:
            if row.intitule == self.new_center_int_box.text:
                print("This center already exists")
                center_exist = True

        if center_exist == False:

##            try:
            idService= self.service_button.id_object

            add_permission_query = "INSERT INTO `permission` (`idPermission`) VALUES (NULL) ;"
            db.query(add_permission_query,[])

            get_idpermission_query = "SELECT P.idPermission AS Id FROM permission P ORDER BY P.idPermission DESC LIMIT 1;"
            db.query(get_idpermission_query,[])
            get_permission_id_data = db.db_fetchall()

            add_center_query = """INSERT INTO `center` (`idCenter`, `intitule`, `desc`, `idService`)
                                    VALUES (%s,%s,%s,%s);"""

            parameters_query = [get_permission_id_data,self.new_center_int_box.text,self.new_center_desc_box.text,idService]
            db.query(add_center_query,parameters_query)
            db.commit()
##            except:
##                db.rollback()

            self.new_center_int_box.text = ""
            self.center_listbox.center_listview.adapter.data = self.center_listbox.get_center_list()

#Class of the Service List Items
class Center_List_Item(BoxLayout, ListItemButton):
    id_center = StringProperty()
    name_center = StringProperty()
    id_service_cor = StringProperty()
    desc_center = StringProperty()

#Class of the Service List
class Center_List(BoxLayout):
    center_listview= ObjectProperty()

    def center_converter(self, index, center):
        result = {
            "id_center": str(center.a_index),
            "name_center": str(center.a_name),
            "id_service_cor": str(center.a_service),
            "desc_center": str(center.a_description)
        }
        return result

    def get_center_list(self):

        #DB CONNECTION
        db = MyDB()
        #Execute la requete SQL
        get_all_center_query = "SELECT * FROM Center;"

        try:
            db.query(get_all_center_query,[])

            db.commit()
        except:
            db.rollback()
        #On obtient une matrice
        center_data = db.db_fetchall()

        # Liste de center
        data_center = ListCenterFromFetch(center_data)

        return data_center
