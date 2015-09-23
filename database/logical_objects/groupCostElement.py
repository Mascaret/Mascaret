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
