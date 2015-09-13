#Python Libs imports
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty

#Class of the principal screen of the HP
class HomePage(Screen, ScreenManager):
    screen1_box= ObjectProperty()
    right_Button= ObjectProperty()
    module_box= ObjectProperty()
    right_panel= ObjectProperty()
