from database.logical_objects.object import ObjectGeneral

#------------------------------------------------------------------------------------------------------------------------
## @class Tool tool.py
#  @brief Class of the object Tool.
#  @sa Service, Center
#
class Tool(ObjectGeneral):
    ## @fn  __init__(self, index, name, module, toolType, listUsers = [])
    #  @brief Constructor of the class Tool.
    #  @param index Local index.
    #  @param name Name of this tool.
    #  @param module The module this tool is linked to.
    #  @param toolType The type of this tool.
    #  @param listUsers The Users of this Tool.
    #
    def __init__(self, index, name, module, toolType, listUsers = []):
        self.a_index = int(index)
        self.a_name = str(name)
        self.a_module = str(module)
        self.a_toolType = toolType
        self.a_listUsers = listUsers
        db.addTool(self)

    ## @fn Destructor of the class Tool
    #
    def __del__(self):
        db.removeTool(self)

    def addUser(self, i_user):
        if i_user in self.a_listUsers:
            return
        self.a_listUsers.append(i_user)
        i_user.addTool(self)
