from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty, StringProperty
from kivy.uix.listview import ListItemButton
from kivy.uix.modalview import ModalView
from kivy.uix.button import Button

class Bouton_Deroulant(Button):
    id_object= StringProperty()
    name_object= StringProperty()
    
    def MenuDeroulant(self):
        liste = self.get_ent_jur_list()
        self.modal = Liste_Deroulante()
        self.modal.width = self.width
        self.modal.pos_hint = {'x': 0.5 + 0.5 * self.pos_hint['x'], 'top': self.pos_hint['y']}
        self.modal.ent_jur_listview.adapter.data=liste
        self.modal.height= str(min(400,len(liste) * 30)) + "dp"
        self.modal.ent_jur_listview.adapter.bind(on_selection_change=self.select_change)
        self.modal.open()

    def select_change(self,la):
        self.text= la.selection[0].name_jur_ent
        self.modal.dismiss()

    def get_ent_jur_list(self):
        return []

class Liste_Deroulante(ModalView):
    ent_jur_listview = ObjectProperty()

    def ent_jur_converter(self, index, ent_jur):
        result = {
            "name_jur_ent": str(ent_jur)
        }
        return result

    def select_change(self):
        print("a")




class Liste_Deroulante_Item(BoxLayout, ListItemButton):
    name_jur_ent = StringProperty()

