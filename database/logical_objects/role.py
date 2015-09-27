from database.logical_objects.object import ObjectGeneral

#------------------------------------------------------------------------------------------------------------------------
## @class Role role.py
#  @brief Class of the object Role.
#  @sa Project
#  @todo CLASSES OPERATION ET PERMISSION A INTEGRER
#
class Role(ObjectGeneral):
    ## @fn __init__(self, index, intitule, listUsers = [])
    #  @brief Constructor of the class Role.
    #  @param index Permission index.
    #  @param name Name of this Role.
    #  @param listUsers The Users linked to this role.
    #
    def __init__(self, index, name, listUsers = []):
        self.a_index = int(index)
        self.a_name = str(name)
        self.a_listUsers = listUsers
        db.addRole(self)

    ## @fn Destructor of the class Role
    #
    def __del__(self):
        db.removeRole(self)

    def addUser(self, i_user):
        if i_user in self.a_listUsers:
            return
        self.a_listUsers.append(i_user)
        i_user.addRole(self)
