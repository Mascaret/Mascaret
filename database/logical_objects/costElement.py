from database.logical_objects.object import ObjectGeneral

#------------------------------------------------------------------------------------------------------------------------
## @class CostElement costElement.py
#  @brief Class of the object CostElement.
#  @sa Expense, GroupCostElement
#
class CostElement(ObjectGeneral):
    ## @fn __init__(self, index, name, description, listExpenses = [], listGroupCostElement = [])
    #  @brief Constructor of the class CostElement.
    #  @param index Permission index.
    #  @param name Name of the CostElement.
    #  @param listExpenses List of WbsCenterActivity which are linked to this CostElement.
    #  @param listGroupCostElement  List of GroupCostElement this CostElement is linked to.
    #
    def __init__(self, index, name, description, listExpenses = [], listGroupCostElement = []):
        self.a_index = index
        self.a_name = name
        self.a_description = description
        self.a_listExpenses = listExpenses
        self.a_listGroupCostElement = listGroupCostElement
