from database.logical_objects.object import ObjectGeneral

#------------------------------------------------------------------------------------------------------------------------
## @class Employee employee.py
#  @brief Class of the object Employee. Base class of Users.
#  @sa Center, Project
#
class Employee(ObjectGeneral):
    ## @fn __init__(self, index, name, surname, job, listCenters = [], mapProjectFunction = [])
    #  @brief Constructor of the class Employee.
    #  @param index Permission index.
    #  @param name Name of this Employee.
    #  @param surname Surname of this Employee.
    #  @param job  Job of this Employee.
    #  @param listCenters  List of Centers this employee is linked to.
    #  @param mapProjectFunction  Map that links projects and functions that the employee has on theproject
    #
    def __init__(self, index, name, surname, job, listCenters = [], mapProjectFunction = []):
        self.a_index = int(index)
        self.a_name = str(name)
        self.a_surname = str(surname)
        self.a_listCenters = listCenters
        self.a_mapProjectFunction = mapProjectFunction
