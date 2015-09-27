from database.logical_objects.object import ObjectGeneral

#------------------------------------------------------------------------------------------------------------------------
## @class Status statut.py
#  @brief Class of the object Status.
#  @sa Service, Center
#
class Status(ObjectGeneral):
        ## @fn __init__(self, index, description, listExpenses = [])
        #  @brief Constructor of the class Status.
        #  @param index Local index.
        #  @param name Name of this Status.
        #  @param listExpenses The Expenses of this status.
        #
    def __init__(self, index, name, listExpenses = []):
        self.a_index = index
        self.a_name = name
        self.a_listExpenses = listExpenses #pourras etre une list nul = []
        db.addStatus(self)

    ## @fn Destructor of the class Status
    #
    def __del__(self):
        db.removeStatus(self)

    def addExpense(self, i_expense):
        if self != i_expense.a_status:
            return
        self.a_listExpenses.append(i_expense)
