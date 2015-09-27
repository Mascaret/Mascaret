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
        db.addCodeType(self)

        def addWbsCA(self, i_ca):
            if i_ca in self.a_listWbsCA:
                return
            self.a_listWbsCA.append(i_ca)
            i_ca.addCodeType(self)

        def addWBSElement(self, i_element):
            if i_element.a_codeType != self:
                return
            self.a_listWBSElement.append(i_element)

        ## @fn Destructor of the class CodeType
        #
        def __del__(self):
            db.removeCodeType(self)
