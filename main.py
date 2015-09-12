#Python Libs imports
from kivy.config import Config
Config.set('graphics', 'window_state', 'maximized')
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, NoTransition
from kivy.app import App
from kivy.properties import ObjectProperty, StringProperty
import time
import pymysql
#Personnal Libs imports
import config.settings as setts
from database.db import MyDB
from user.user import User
from gui.home_screen.hp_outils_buttons import HPOutilsButton
from gui.login_screen.loginscreen import MascaretLoginScreen
from user.module import ListModuleFromFetch
from gui.home_screen.modules_screens import ModuleGUI
from gui.home_screen.home_screen import HomePage
from gui.home_screen.hp_modules_buttons import HPModuleButton

#root
class MascaretRoot(FloatLayout):

    def __init__(self):
        super(MascaretRoot, self).__init__()
        self.mascaretloginscreen = MascaretLogScreen()
        self.add_widget(self.mascaretloginscreen)

    def show_bigscreen(self):
        self.clear_widgets()
        self.mascarethomescreen = MascaretHomeScreen()
        self.add_widget(self.mascarethomescreen)

#Class of the homescreen
class MascaretHomeScreen(ScreenManager):
    mode = StringProperty(setts.Mode)

    def __init__(self,**kwargs):
        super(MascaretHomeScreen, self).__init__()
        self.transition=NoTransition()

        module_data = self.get_module_available()

        self.homepage = HomePage()
        self.add_widget(self.homepage)

        self.create_modules_and_tools(module_data)


##        self.right_panel= RightPanel()
##        self.current_screen.screen1_box.add_widget(self.right_panel)


    def get_module_available(self):

                ###################Looking into Module#####################

        #DB CONNECTION

        db = MyDB()

        modules_query = """SELECT m.intitule, o.intitule
                        FROM module AS m , outil AS o, utilisateur AS u, utilisateuroutil AS uo
                        WHERE u.login =%s AND uo.idUtilisateur = u.idUtilisateur
                        AND uo.idOutil = o.idOutil AND o.idModule = m.idModule"""

        user_logged = User()
        parameters_query =[user_logged.login]
        try:
            db.query(modules_query,parameters_query)
            db.commit()
        except:
            db.rollback()
            
        modules_data = db.db_fetchall()

        return modules_data

    def create_modules_and_tools(self, modules_data):

        list_modules = ListModuleFromFetch(modules_data)

        # #On va chercher les infos
        # for row in modules_data:
        #
        #     module_appearance = False
        #     for mod in list_modules:
        #         #Si le module existe deja dans la liste
        #         if mod.module_name == str(row[0]):
        #             module_appearance = True
        #             index_mod = list_modules.index(mod)
        #             break
        #
        #     if module_appearance:
        #         list_modules[index_mod].list_outils.append(Outil(str(row[1])))
        #     else:
        #         temp_module = Module(str(row[0]),[])
        #         temp_module.list_outils.append(Outil(str(row[1])))
        #         list_modules.append(temp_module)

        #On créer la GUI pour chaque Module
        for mod in list_modules:
            newmodule = ModuleGUI(name = mod.module_name)
            for tools in mod.list_outils:
                newmodule.tools_box.add_widget(HPOutilsButton(tools.outil_name))
            self.add_widget(newmodule)
            self.homepage.module_box.add_widget(HPModuleButton(strLinkedModule=mod.module_name))



    def on_mode(self, widget, mode):
        if mode == "wide" :
            print("wide")
            setts.Mode = "wide"
            print("setts: " + setts.Mode)
            for screen in self.screens:
                print(screen.name)
                screen.right_Button.pos_hint = {'x': 1}
                screen.right_Button.disabled= True
                try:
                    screen.get_screen('2').remove_widget(screen.right_panel)
                except:
                    pass
                try:
                    screen.screen1_box.add_widget(screen.right_panel)
                except:
                    pass


        else:
            print("narrow")
            setts.Mode = "narrow"
            print("setts: " + setts.Mode)
            for screen in self.screens:
                print(screen.name)
                screen.right_Button.pos_hint = {'x': 0.93}
                screen.right_Button.disabled= False
                try:
                    screen.screen1_box.remove_widget(screen.right_panel)
                except:
                    pass
                try:
                    screen.get_screen('2').add_widget(screen.right_panel)
                except:
                    pass

#Call of the login screen
class MascaretLogScreen(MascaretLoginScreen):
    def on_right_id(self):
        app = Mascaret.get_running_app()
        app.root.show_bigscreen()

#Panel containing tools on the right of the screen
class RightPanel(FloatLayout):
    pass

#button linking to the right panel
class RightPanelBtn(Button):
    pass

#App
class Mascaret(App):
    pass
    
Mascaret().run()
