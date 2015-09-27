from database.logical_objects.object import ObjectGeneral

#------------------------------------------------------------------------------------------------------------------------
## @class ToolType tooltype.py
#  @brief Class of the object ToolType.
#  @sa Tool
#
class ToolType(ObjectGeneral):
    ## @fn __init__(self, index, name, listTools = [])
    #  @brief Constructor of the class ToolType.
    #  @param index Local index.
    #  @param typ Name of this type.
    #  @param listTools The tools of this type.
    #
    def __init__(self, index, name, listTools = []):
        self.a_index = int(index)
        self.a_name = str(name)
        self.a_listTools = listTools
        db.addToolType(self)

    ## @fn Destructor of the class ToolType
    #
    def __del__(self):
        db.removeToolType(self)

    def addTool(self, i_tool):
        if self != i_tool.a_toolType:
            return
        self.a_listTools.append(i_tool)
