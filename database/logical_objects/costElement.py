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
        db.addCostElement(self)

    def addExpense(self, i_expense):
        if i_group.a_costElement != self:
            return
        self.a_listGroupCostElement.append(i_expense)

    def addGroupCostElement(self, i_group):
        if i_group in self.a_listGroupCostElement:
            return
        self.a_listGroupCostElement.append(i_group)
        i_group.addCostElement(self)

    ## @fn Destructor of the class CostElement
    #
    def __del__(self):
        db.removeCostElement(self)
