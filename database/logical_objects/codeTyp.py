from database.logical_objects.object import ObjectGeneral

#------------------------------------------------------------------------------------------------------------------------
## @class CodeType codeType.py
#  @brief Class of the object CodeType.
#  @sa Type
#
class CodeType(ObjectGeneral):
    ## @fn __init__(self, index, name, listWbsCA = [], listWbsElement = [])
    #  @brief Constructor of the class CodeType.
    #  @param index Permission index.
    #  @param name Name of the CodeType.
    #  @param listWbsCA List of WbsCenterActivity the CodeType is linked to.
    #  @param listWbsElement  List of WbsElement of this type.
    #
    def __init__(self, index, name, listWbsCA = [], listWbsElement = []):
        self.a_index = int(index)
        self.a_name=str(name)
        self.a_listWbsCA = listWbsCA
        self.a_listWbsElement = listWbsElement
