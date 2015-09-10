from gui.hoverclasses import HoverButton
from kivy.properties import ObjectProperty, StringProperty
from kivy.uix.relativelayout import RelativeLayout
from kivy.adapters.listadapter import ListAdapter
from kivy.uix.listview import ListItemButton, ListView, ListItemLabel
from kivy.uix.boxlayout import BoxLayout
from entjur import EntJur,ListEntJur
from location import Location,ListLocationFromFetch
import pymysql
import db_Requests
from db import MyDB

class HPOutilsButton(HoverButton):

    def __init__(self, strLinkedOutils):
        super(HPOutilsButton, self).__init__()
        self.linkedoutils_name = strLinkedOutils
        self.text= self.linkedoutils_name
        self.background_normal= 'gui/rectbut1.png'
        self.background_color= (100/255, 100/255, 230/255, 1)
        self.linkedoutils = self.define_linked_tool()


    def on_release(self):
        print(self.linkedoutils_name)

        self.parent.parent.parent.parent.parent.right_panel.clear_widgets()
        self.parent.parent.parent.parent.parent.right_panel.add_widget(self.linkedoutils)

        if self.parent.parent.parent.parent.parent.parent.mode == "narrow":
            print("rrrr")
            self.parent.parent.parent.parent.manager.transition.direction = 'left'
            self.parent.parent.parent.parent.manager.current = "2"


    def define_linked_tool(self):

        if self.linkedoutils_name == "Forecast tool":

            return Forecast_Tool()

        elif self.linkedoutils_name == "Liste employes":

            return Liste_Employes()

        elif self.linkedoutils_name == "CJSL01":

            return CJSL01()

        elif self.linkedoutils_name == "Creation facture":

            return Creation_Facture()

        elif self.linkedoutils_name == "Liste commandes":

            return Liste_Commandes()

        elif self.linkedoutils_name == "Formulaire dtb 1":

            return Formulaire_Ent_Jur()

        elif self.linkedoutils_name == "Formulaire location":

            return Formulaire_Location()







class Outil:

    def __init__(self,outil_name):
        self.outil_name = outil_name



class Forecast_Tool(RelativeLayout):
    pass

class Liste_Employes(RelativeLayout):
    pass

class CJSL01(RelativeLayout):
    pass

class Creation_Facture(RelativeLayout):
    pass

class Liste_Commandes(RelativeLayout):
    pass




class Formulaire_Ent_Jur(RelativeLayout):
    new_legal_entity_box = ObjectProperty()
    list_ent_jur_box = ObjectProperty()

    #Add
    def send_new_legal_entity(self):
        print(self.new_legal_entity_box.text)

        #Check directement la DB pour plus de surete

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

        entity_exist = False
        for row in data_ent_jur:
            if row.ent_name == self.new_legal_entity_box.text:
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


class Jur_Ent_List_Item(BoxLayout, ListItemButton):
    id_jur_ent = StringProperty()
    name_jur_ent = StringProperty()


class Jur_Ent_List(BoxLayout):
    ent_jur_listview= ObjectProperty()

    def __init__(self, *args, **kwargs):
        super(Jur_Ent_List, self).__init__()
        self.ent_jur_listview.adapter.data = self.get_ent_jur_list()

    def ent_jur_converter(self, index, ent_jur_id):
        result = {
            "id_jur_ent": ent_jur_id,
            "name_jur_ent": ""
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
        data_ent_jur = ListEntJur(legal_entities_data)


        #Liste d'intitule des entites juridiques
        list_ent_jur = []
        for line in data_ent_jur:
            list_ent_jur.append(line.ent_name)

        return list_ent_jur


class Formulaire_Location(RelativeLayout):
    new_location_box = ObjectProperty()
    location_listbox = ObjectProperty()
    #Add
    def send_new_location(self):
        print(self.new_location_box.text)

        #Check directement la DB pour plus de surete
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

        location_exist = False
        for row in data_location:
            if row.loc_intitule == self.new_location_box.text:
                print("This Location already exists")
                location_exist = True

        if location_exist == False:
            idEntJur=ent_jur_listbox.adapter.selection.id

            add_permission_query = "INSERT INTO `Permission`;"

            get_permission_id_query = """SELECT P.idPermission AS idP
                                    FROM Permission P
                                    ORDER BY P.idPermission DESC
                                    LIMIT 1;"""

            add_location_query = """INSERT INTO `Location` (idLocation, intitule, idEntJur)
                                    VALUES (%d,%s,%d);"""

            parameters_query = [id_permission_data,self.new_location_box.text,idEntJur]

            try:
                db.query(add_permission_query,[])

                db.query(get_permission_id_query,[])
                id_permission_data = db.db_fetchone()

                db.query(add_location_query,parameters_query)
                db.commit()
            except:
                db.rollback()



class Location_List_Item(BoxLayout, ListItemButton):
    id_location = StringProperty()
    name_location = StringProperty()


class Location_List(BoxLayout):
    location_listview= ObjectProperty()

    def __init__(self, *args, **kwargs):
        super(Location_List, self).__init__()
        self.location_listview.adapter.data = self.get_location_list()

    def location_converter(self, index, location_id):
        result = {
            "id_jur_ent": ent_jur_id,
            "name_jur_ent": ""
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
        data_location = ListEntJur(location_data)

        #Liste d'intitule des entites juridiques
        list_location = []
        for line in data_location:
            list_location.append(line.loc_intitule)

        return list_location
