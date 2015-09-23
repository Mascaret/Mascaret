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
