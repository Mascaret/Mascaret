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
