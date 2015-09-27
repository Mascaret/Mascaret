#Python Libs imports
from kivy.config import Config
Config.set('graphics', 'window_state', 'maximized')
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.app import App
import pymysql
#Personnal Libs imports
from gui.login_screen.loginscreen import MascaretLoginScreen
from gui.home_screen.mascaret_screen_manager import MascaretHomeScreen
from database.db import MyDB

#root
class MascaretRoot(FloatLayout):

    def __init__(self):
        super(MascaretRoot, self).__init__()
        self.mascaretloginscreen = MascaretLogScreen()
        self.add_widget(self.mascaretloginscreen)
        db = MyDB()

    def show_bigscreen(self):
        self.clear_widgets()
        self.mascarethomescreen = MascaretHomeScreen()
        self.add_widget(self.mascarethomescreen)



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
