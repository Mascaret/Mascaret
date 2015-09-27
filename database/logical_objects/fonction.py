from database.logical_objects.object import ObjectGeneral

#------------------------------------------------------------------------------------------------------------------------
## @class Function function.py
#  @brief Class of the object Function.
#  Deprecated, use directly Users and Project
#
class Function(ObjectGeneral):

    def __init__(self,index,intitule,employee,project):
        self.a_index = int(index)
        self.a_intitule = str(intitule)
        self.a_employee = employee
        self.a_project = project
        db.addFunction(self)

    ## @fn Destructor of the class Function
    #
    def __del__(self):
        db.removeFunction(self)
