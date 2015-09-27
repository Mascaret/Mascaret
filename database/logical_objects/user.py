from database.logical_objects.employee import Employee
from database.logical_objects.object import ObjectGeneral

#------------------------------------------------------------------------------------------------------------------------
## @class User user.py
#  @brief Class of the object User.
#  @sa Tool, Employee
#  @todo CLASSE EMPLOYEE A INTEGRER : héritage
#
class UserDb(ObjectGeneral, Employee):
    ## @fn __init__(self, index, login, password, list_tools = [], list_roles = [] )
    #  @brief Constructor of the class User.
    #  @param index Permission index.
    #  @param login Login of the account.
    #  @param password Password of the account.
    #  @param listTools The tools the user has access to.
    #  @param listRoles The roles the user has.
    #
    def __init__(self, index, login, password, listTools = [], listRoles = [], listExpenses = []):
        self.a_index = int(index)
        self.a_login = str(login)
        self.a_password = str(password)
        self.a_listTools = listTools
        self.a_listRoles = listRoles
        self.a_listExpenses = listExpenses

    def addTool(self, i_tool):
        if i_tool in self.a_listTools:
            return
        self.a_listTools.append(i_tool)
        i_tool.addUser(self)

    def addRole(self, i_role):
        if i_role in self.a_listRoles:
            return
        self.a_listRoles.append(i_role)
        i_role.addUser(self)

    def addExpense(self, i_expense):
        if i_expense in self.a_listExpenses:
            return
        self.a_listExpenses.append(i_expense)
        i_expense.addUser(self)
