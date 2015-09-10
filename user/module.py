from gui.hoverclasses import HoverButton
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty
from user.outil import Outil

class HPModuleButton(HoverButton):

    def __init__(self, strLinkedModule):
        super(HPModuleButton, self).__init__()
        self.linkedmodule = strLinkedModule
        self.text= self.linkedmodule
        self.background_normal= 'gui/rectbut1.png'
        self.background_color= (100/255, 100/255, 230/255, 1)

    def on_release(self):
        self.parent.parent.parent.parent.parent.manager.current = self.linkedmodule


class HomePage(Screen, ScreenManager):
    screen1_box= ObjectProperty()
    right_Button= ObjectProperty()
    module_box= ObjectProperty()
    right_panel= ObjectProperty()


class Module:

    def __init__(self, module_name, listoutils):
        self.module_name = module_name
        self.list_outils = listoutils

# class ListModuleFromFetch: Ceci est une classe avec une liste en attribut
#
#     def __init__(self, fetch_result):
#         self.list_modules = []
#         for row in fetch_result:
#             module_appearance = False
#             for mod in self.list_modules:
#                 #Si le module existe deja dans la liste
#                 if mod.module_name == str(row[0]):
#                     module_appearance = True
#                     index_mod = self.list_modules.index(mod)
#                     break
#
#             if module_appearance:
#                 self.list_modules[index_mod].list_outils.append(Outil(str(row[1])))
#             else:
#                 temp_module = Module(str(row[0]),[])
#                 temp_module.list_outils.append(Outil(str(row[1])))
#                 self.list_modules.append(temp_module)

#Cette classe EST une liste
class ListModuleFromFetch(list):

    def __init__(self, fetch_result):
        for row in fetch_result:
            module_appearance = False
            for mod in self:
                #Si le module existe deja dans la liste
                if mod.module_name == str(row[0]):
                    module_appearance = True
                    index_mod = self.index(mod)
                    break

            if module_appearance:
                self[index_mod].list_outils.append(Outil(str(row[1])))
            else:
                temp_module = Module(str(row[0]),[])
                temp_module.list_outils.append(Outil(str(row[1])))
                self.append(temp_module)


class ModuleGUI(Screen, ScreenManager):
    tools_box = ObjectProperty()
    screen1_box = ObjectProperty()
    right_Button= ObjectProperty()
    right_panel= ObjectProperty()
