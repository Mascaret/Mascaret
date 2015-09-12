#Personnal Libs imports
from gui.hoverclasses.hoverbutton import HoverButton1

#Class of the module buttons on HP
class HPModuleButton(HoverButton1):

    def __init__(self, strLinkedModule):
        super(HPModuleButton, self).__init__()
        self.linkedmodule = strLinkedModule
        self.text= self.linkedmodule
        self.background_normal= 'gui/hoverclasses/rectbut1.png'
        self.background_color= (100/255, 100/255, 230/255, 1)

    def on_release(self):
        self.parent.parent.parent.parent.parent.manager.current = self.linkedmodule


