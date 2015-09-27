from database.logical_objects.object import ObjectGeneral

#------------------------------------------------------------------------------------------------------------------------
## @class groupCostElement groupCostElement.py
#  @brief Class of the object groupCostElement.
#  @sa Classification, costElement, WbsCenterActivity
#
class groupCostElement(ObjectGeneral):
    ## @fn __init__(self, index, name, classification, listGroupCostElement = [], listCostElement = [], listCenter = [], listWBSca = []
    #  @brief Constructor of the class groupCostElement.
    #  @param index Local index.
    #  @param name Name of this groupCostElement.
    #  @param classification How this groupCostElement is ordered.
    #  @param listGroupCostElement List of subGroupCostElement this Group directly contains.
    #  @param listCostElement List of CostElement this Group directly contains.
    #  @param listCenter List of centers this GroupCostElementis linked to.
    #  @param listWBSca List of WbsCenterActivity this GroupCostElementis linked to.
    #
    def __init__(self, index, name, classification, listGroupCostElement = [], listCostElement = [], listCenter = [], listWBSca = []):
        self.a_index = int(index)
        self.a_name = str(name)
        self.a_classification = classification # On lui passe un object classification prealablement cree
        self.a_listGroupCostElement = listGroupCostElement # Si pas de list de gce alors on passe une liste vide #CLementine c'est bien ?
        self.a_listCostElement = listCostElement # peut etre NUL = []
        self.a_listCenter = listCenter # peut etre NUL = []
        self.a_listWBSca = listWBSca
        db.addGroupCostElement(self)

    ## @fn Destructor of the class GroupCostElement
    #
    def __del__(self):
        db.removeGroupCostElement(self)

    def addCostElement(self, i_element):
        if i_element in self.a_listCostElement:
            return
        self.a_listCostElement.append(i_element)
        i_ca.addGroupCostElement(self)

    def addCenter(self, i_center):
        if i_center in self.a_listWbsCA:
            return
        self.a_listWbsCA.append(i_center)
        i_ca.addGroupCostElement(self)

    def addWbsCA(self, i_ca):
        if i_ca in self.a_listWbsCA:
            return
        self.a_listWbsCA.append(i_ca)
        i_ca.addGroupCostElement(self)
