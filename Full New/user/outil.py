from gui.hoverclasses import HoverButton
from kivy.properties import ObjectProperty
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

            return Formulaire_database_1()


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

class Formulaire_database_1(RelativeLayout):
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



class Formulaire_Location(RelativeLayout):
    new_location_box = ObjectProperty()
    ent_jur_listbox = ObjectProperty()
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

        # Liste d'entite Juridique
        data_location = ListEntJur(location_data)
        ######################################################################################################
        location_exist = False
        for row in data_location:
            if row.loc_intitule == self.new_location_box.text:
                print("This Legal Entity already exists")
                location_exist = True
        if location_exist == False:
            ent_jur_listbox.adapter.selection
            add_location_query = "INSERT INTO `location` (`intitule`) VALUES (%s) ;"

            parameters_query = [str(self.new_legal_entity_box.text)]

            try:
                db.query(add_legal_entity_query,parameters_query)
                db.commit()
            except:
                db.rollback()




class TestListItem(ListItemButton):
    pass

class TestList(BoxLayout):

    def __init__(self, *args, **kwargs):
        super(TestList, self).__init__()


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
        listtest = []
        for line in data_ent_jur:
            listtest.append(line.ent_name)

        self.list_ent_jur = listtest


        list_adapter = ListAdapter(data=listtest,
                                   cls=TestListItem,
                                   selection_mode='single',
                                   allow_empty_selection=False)

        list_view = ListView(adapter=list_adapter)
        self.add_widget(list_view)

class LocationList(BoxLayout):

    def __init__(self, *args, **kwargs):
        super(LocationList, self).__init__()

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
        listlocation = []
        for line in data_location:
            listlocation.append(line.loc_intitule)


        list_adapter = ListAdapter(data=listlocation,
                                   cls=TestListItem,
                                   selection_mode='single',
                                   allow_empty_selection=False)

        list_view = ListView(adapter=list_adapter)
        self.add_widget(list_view)
