from database.logical_objects.object import ObjectGeneral

#------------------------------------------------------------------------------------------------------------------------
## @class Expense expense.py
#  @brief Class of the object Expense.
#  @sa User, costElement, Status, WBSElement
#
class Expense(ObjectGeneral):
    ## @fn __init__(self, index, price, quantity, comment, status, costElement, typeCE = None, wbsElement = None, listUsers = [])
    #  @brief Constructor of the class Expense.
    #  @param index Local index.
    #  @param price Price of this expense.
    #  @param quantity Quantity of product for this expense (ex: hours).
    #  @param comment Detailed comment for this expense.
    #  @param status Real, or forecast.
    #  @param costElement CostElement this Legal Entity has.
    #  @param typeCE Type of Cost Center (Profit Center, Cost Center, Partner Cost Center).
    #  @param wbsElement WBSElement this Legal Entity is linked to.
    #  @param listUsers Users that can modify this Legal Entity .
    #
    def __init__(self, index, price, quantity, comment, status, costElement, typeCE = None, wbsElement = None, listUsers = []):
        self.a_index = int(index)
        self.a_price = price
        self.a_quantity = int(quantity)
        self.a_comment = str(comment)
        self.a_status = status
        self.a_costElement = costElement
        self.a_typeCE = typeCE
        self.a_wbsElement = wbsElement
        self.a_listUsers = listUsers # peut etre NUL
        db.addExpense(self)

    def addUser(self, i_user):
        if i_user in self.a_listUsers:
            return
        self.a_listUsers.append(i_user)
        i_user.addExpense(self)

    ## @fn Destructor of the class Expense
    #
    def __del__(self):
        db.removeExpense(self)
