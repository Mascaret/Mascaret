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
from database.logical_objects.service import Service,ListServiceFromFetch

#Class of the Service Form.
class Formulaire_Service(RelativeLayout):
    new_service_box = ObjectProperty()
    service_listbox = ObjectProperty()
    location_button = ObjectProperty()

    #Add
    def send_new_service(self):
        print(self.new_service_box.text)
        print(self.location_button.id_object)
        data_service = self.service_listbox.get_service_list()

        self.check_existence_of_new_service_and_add_it(data_service)


    def check_existence_of_new_service_and_add_it(self, data_service):

        #DB CONNECTION
        db = MyDB()
        
        service_exist = False
        for row in data_service:
            if row.intitule == self.new_service_box.text:
                print("This service already exists")
                service_exist = True

        if service_exist == False:

##            try:
            idLocation= self.location_button.id_object

            add_permission_query = "INSERT INTO `permission` (`idPermission`) VALUES (NULL) ;"
            db.query(add_permission_query,[])

            get_idpermission_query = "SELECT P.idPermission AS Id FROM permission P ORDER BY P.idPermission DESC LIMIT 1;"
            db.query(get_idpermission_query,[])
            get_permission_id_data = db.db_fetchall()

            add_service_query = """INSERT INTO `service` (idservice, intitule, idLocation)
                                    VALUES (%s,%s,%s);"""

            parameters_query = [get_permission_id_data,self.new_service_box.text,idLocation]
            db.query(add_service_query,parameters_query)
            db.commit()
##            except:
##                db.rollback()

            self.new_service_box.text = ""
            self.service_listbox.service_listview.adapter.data = self.service_listbox.get_service_list()

#Class of the Location List Items
class Service_List_Item(BoxLayout, ListItemButton):
    id_service = StringProperty()
    name_service = StringProperty()
    id_location_cor = StringProperty()

#Class of the Location List
class Service_List(BoxLayout):
    service_listview= ObjectProperty()

    def service_converter(self, index, service):
        result = {
            "id_service": str(service.Id),
            "name_service": str(service.intitule),
            "id_location_cor": str(service.id_cor1)
        }
        return result

    def get_service_list(self):

        #DB CONNECTION
        db = MyDB()
        #Execute la requete SQL
        get_all_service_query = "SELECT * FROM Service;"

        try:
            db.query(get_all_service_query,[])

            db.commit()
        except:
            db.rollback()
        #On obtient une matrice
        service_data = db.db_fetchall()

        # Liste de service
        data_service = ListServiceFromFetch(service_data)
        
        return data_service

#Class of a list of Ent Jur trigered by clickiing on a button
class Menu_Deroulant_Location(Menu_Deroulant):

    def get_object_list(self):
        
        #DB CONNECTION
        db = MyDB()
        #Execute la requete SQL
        get_all_location_query = "SELECT *FROM Location;"

        try:
            db.query(get_all_location_query,[])
            db.commit()
        except:
            db.rollback()
        #On obtient une matrice
        location_data = db.db_fetchall()

        # Liste de location
        data_location = ListLocationFromFetch(location_data)
        
        return data_location

