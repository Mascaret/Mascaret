#Python Libs imports
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.modalview import ModalView
from kivy.uix.button import Button
from kivy.uix.listview import ListItemButton
from kivy.properties import ObjectProperty, StringProperty
#Personnal Libs imports
import config.settings

#Class creating a list menu triggered when clicking on a button
class Menu_Deroulant(Button):
    id_object= StringProperty()
    name_object= StringProperty()
    
    def MenuDeroulant(self):
        print(settings.Mode)
        liste = self.get_ent_jur_list()
        self.modal = Liste_Deroulante()
        self.modal.width = self.width
        self.modal.pos_hint = {'x': 0.5 + 0.5 * self.pos_hint['x'], 'top': self.pos_hint['y']}
        self.modal.ent_jur_listview.adapter.data=liste
        self.modal.height= str(min(400,len(liste) * 30)) + "dp"
        self.modal.ent_jur_listview.adapter.bind(on_selection_change=self.select_change)
        self.modal.open()

    def select_change(self,la):
        self.name_object = la.selection[0].name_object
        print(self.name_object)
        self.text= self.name_object
        self.id_object = la.selection[0].id_object
        print(self.id_object)
        self.modal.dismiss()

    def get_ent_jur_list(self):
        return ["GRE", "FRE"]

#Class of a list menu inside a modal view
class Liste_Deroulante(ModalView):
    ent_jur_listview = ObjectProperty()

    def ent_jur_converter(self, index, objet):
        result = {
            "id_object": str(objet.ent_id),
            "name_object": str(objet.ent_name)
        }
        return result

    def select_change(self):
        print("a")

#Class of the items contained by the list menu
class Liste_Deroulante_Item(BoxLayout, ListItemButton):
    id_object = StringProperty()
    name_object = StringProperty()
    id_cor1_object = StringProperty()
    id_cor2_object = StringProperty()
