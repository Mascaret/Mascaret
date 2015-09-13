#Python Libs imports

#Personnal Libs imports
from gui.hoverclasses.hoverbutton import HoverButton1
from gui.formulaire_outils.formulaire_ent_jur import Formulaire_Ent_Jur
from gui.formulaire_outils.formulaire_location import Formulaire_Location
from gui.formulaire_outils.forecast_tool import Forecast_Tool
from gui.formulaire_outils.liste_employes import Liste_Employes
from gui.formulaire_outils.cjsl01 import CJSL01
from gui.formulaire_outils.creation_facture import Creation_Facture
from gui.formulaire_outils.liste_commandes import Liste_Commandes
from gui.formulaire_outils.formulaire_center import Formulaire_Center
from gui.formulaire_outils.formulaire_service import Formulaire_Service

#Class of the tools buttons inside the modules
class HPOutilsButton(HoverButton1):

    def __init__(self, strLinkedOutils):
        super(HPOutilsButton, self).__init__()
        self.linkedoutils_name = strLinkedOutils
        self.text= self.linkedoutils_name
        self.background_normal= 'gui/hoverclasses/rectbut1.png'
        self.background_color= (100/255, 100/255, 230/255, 1)
        self.linkedoutils = self.define_linked_tool()

    def on_release(self):

        self.parent.parent.parent.parent.parent.right_panel.clear_widgets()
        self.parent.parent.parent.parent.parent.right_panel.add_widget(self.linkedoutils)

        if self.parent.parent.parent.parent.parent.parent.mode == "narrow":
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

        elif self.linkedoutils_name == "Formulaire Ent_Jur":

            return Formulaire_Ent_Jur()

        elif self.linkedoutils_name == "Formulaire location":

            return Formulaire_Location()

        elif self.linkedoutils_name == "Formulaire center":

            return Formulaire_Center()

        elif self.linkedoutils_name == "Formulaire service":

            return Formulaire_Service()
