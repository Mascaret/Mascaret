#Python Libs imports
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.listview import ListItemButton
import pymysql
from kivy.properties import ObjectProperty, StringProperty

#Personnal Libs imports
from database.db import MyDB
from database.logical_objects.entjur import EntJur,ListEntJur
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
        location_text = str(self.new_location_box.text)
        location_id = int(self.ent_jur_button.id_object)
        location_exist = check_existence_of_new_location_and_add_it_db(data_location,location_text,location_id)

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
        data_location = db.get_location_list_db()
        return data_location

#Class of a list of Ent Jur trigered by clickiing on a button
class Menu_Deroulant_Ent_Jur(Menu_Deroulant):

    def get_object_list(self):
        db = MyDB()
        data_ent_jur = db.get_all_ent_jur()
        return data_ent_jur
