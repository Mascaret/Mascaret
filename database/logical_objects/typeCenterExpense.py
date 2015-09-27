from database.logical_objects.object import ObjectGeneral

#------------------------------------------------------------------------------------------------------------------------
## @class TypeCenterExpense typeCenterExpense.py
#  @brief Class of the object TypeCenterExpense.
#  @sa Expense, Center
#  @todo A REVOIR ->la mettre plutot dans center
#
class TypeCenterExpense(ObjectGeneral):
    ## @fn __init__(self, index, description, listExpenses = [])
    #  @brief Constructor of the class TypeCenterExpense.
    #  @param index Permission index.
    #  @param typ Name of this type.
    #  @param expense The expense.
    #  @param center The center.
    #
    def __init__(self, index, typ, expense, center):
        self.a_index = int(index)
        self.a_typ = str(typ)
        self.a_expense = expense
        self.a_center = center
        db.addCenterExpensesType(self)

    ## @fn Destructor of the class CenterExpensesType
    #
    def __del__(self):
        db.removeCenterExpensesType(self)
