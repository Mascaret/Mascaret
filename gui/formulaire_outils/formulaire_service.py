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
        service_text = self.new_service_box.text
        location_id = self.location_button.id_object
        service_exist = db.check_existence_of_new_service_and_add_it_db(data_service,service_text,location_id)

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
        data_service = db.get_service_list_db()
        return data_service

#Class of a list of Ent Jur trigered by clickiing on a button
class Menu_Deroulant_Location(Menu_Deroulant):

    def get_object_list(self):

        #DB CONNECTION
        db = MyDB()
        data_location = db.get_location_list_db()
        return data_location
