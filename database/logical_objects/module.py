from database.logical_objects.object import ObjectGeneral

#------------------------------------------------------------------------------------------------------------------------
## @class CodeType codeType.py
#  @brief Class of the object CodeType.
#  @sa Type
#
class Module(ObjectGeneral):
    ## @fn __init__(self, index, name, listTools = [])
    #  @brief Constructor of the class Module.
    #  @param index Local index.
    #  @param name Name of the Module.
    #  @param listTools List of Tools the module has.
    #
    def __init__(self, index, name, listTools = []):
        self.a_index = int(index)
        self.a_name = str(name)
        self.a_listTools = listTools
        db.addModule(self)

    ## @fn Destructor of the class Module
    #
    def __del__(self):
        db.removeModule(self)

    def addTool(self, i_tool):
        if i_tool.a_module != self:
            return
        self.a_listTools.append(i_tool)
