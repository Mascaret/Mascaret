#Python Libs imports
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty

#Class of the modules screens
class ModuleGUI(Screen, ScreenManager):
    tools_box = ObjectProperty()
    screen1_box = ObjectProperty()
    right_Button= ObjectProperty()
    right_panel= ObjectProperty()
