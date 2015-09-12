#Python Libs imports
from kivy.uix.button import Button
#Personnal Libs imports
from gui.hoverclasses.hoverclass import HoverBehavior

#Button with a "mouse_on" effect
class HoverButton1(Button, HoverBehavior):
    def on_enter(self):
        self.background_normal= 'gui/hoverclasses/rectbut2.png'

    def on_leave(self):
        self.background_normal= 'gui/hoverclasses/rectbut1.png'
