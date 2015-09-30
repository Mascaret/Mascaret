#Python Libs imports
from kivy.uix.dropdown import DropDown
#application imports
from database.logical_objects.buttonobject import *

#------------------------------------------------------------------------------------------------------------------------
## @class MascDropDown MascDropDown.py
#  @brief Class of the object MascDropDown.
#  @sa ButtonObject
#
class MascDropDownButton(ButtonObjectGeneral):
    ## @fn __init__(self, index, num, description, service, wbsElementList = [])
    #  @brief Constructor of the class Center.
    #  @param index Index for the ButtonFactory needed.
    #
    def __init__(self, i_buttonList):
        self.dropdown = DropDown()
        for button in i_buttonList:
            button.bind(on_release = lambda button: self.dropdown.select(button.text))
            self.dropdown.add_Widget(button)
        self.dropdown.bind(on_select = lambda instance, x: setattr(self, "text", x))

    def on_release(self):
        self.dropdown.open()
