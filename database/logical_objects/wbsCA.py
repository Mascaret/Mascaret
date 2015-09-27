from database.logical_objects.object import ObjectGeneral

#------------------------------------------------------------------------------------------------------------------------
## @class WBSActivityCenter wbsCA.py
#  @brief Class of the object WBS Activity Center.
#  @sa WBSElement, CodeType
#
class WBSActivityCenter(ObjectGeneral):
    ## @fn __init__(self, index, name, description, listCodeTyp = [], listGroupCostElement = [])
    #  @brief Constructor of the class WBSActivityCenter.
    #  @param index Permission index.
    #  @param name Name of the WBS Activity Center.
    #  @param description Description of the WBS Activity Center.
    #  @param listCodeTyp The list of code type this AC can get.
    #  @param listGroupCostElement Thelist of Cost Element this Activity Center is linked to.
    #
    def __init__(self, index, name, description, listCodeTyp = [], listGroupCostElement = []):
        self.a_index = int(index)
        self.a_name = str(name)
        self.a_description = str(description)
        self.a_listCodeTyp = listCodeTyp # peut etre NUL
        self.a_listGroupCostElement = listGroupCostElement # peut etre NUL
        db.addWBSCa(self)

    ## @fn Destructor of the class Service
    #
    def __del__(self):
        db.removeWBSCa(self)

    def addCodeType(self, i_type):
        if i_type in self.a_listCodeTyp:
            return
        self.a_listCodeTyp.append(i_type)
        i_type.addWbsCA(self)

    def addGroupCostElement(self, i_group):
        if i_group in self.a_listGroupCostElement:
            return
        self.a_listGroupCostElement.append(i_group)
        i_group.addWbsCA(self)
