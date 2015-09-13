#Personnal Libs imports
from user.outil import Outil

#Class of a module
class Module:

    def __init__(self, module_name, listoutils):
        self.module_name = module_name
        self.list_outils = listoutils


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



