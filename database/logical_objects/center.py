from database.logical_objects.object import ObjectGeneral
from database.db import MyDB
from database.logical_objects.service import Service
from database.logical_objects.location import Location
from database.logical_objects.entjur import LegalEntity

#------------------------------------------------------------------------------------------------------------------------
## @class Center center.py
#  @brief Class of the object Center
#  @sa Employee, Service, WBSEElement, TypeCenterExpense
#
class Center(ObjectGeneral):
    ## @fn __init__(self, index, num, description, service, wbsElementList = [])
    #  @brief Constructor of the class Center.
    #  @param index Permission index.
    #  @param num Name of the Center.
    #  @param description Detailed description of the center.
    #  @param service Name of the service this center is related to.
    #  @param wbsElementList list of the wbsElement the center is related to.
    #
    def __init__(self, index, num, description, service, wbsElementList = [], groupCostElement = [], employees = []):
        self.a_index = int(index)
        self.a_num = num
        self.a_description = str(description)
        self.a_service = service
        self.a_location = service.a_location
        self.a_listWBSElement = wbsElementList
        self.a_listGroupCostElement = groupCostElement
        self.a_listEmployee = employees
        db.addCenter(self)

    def addWBSElement(self, i_element):
        if i_element.a_center != self:
            return
        self.a_listWBSElement.append(i_element)

    def addGroupCostElement(self, i_group):
        if i_group in self.a_listGroupCostElement:
            return
        self.a_listGroupCostElement.append(i_group)
        i_group.addCenter(self)

    def addEmployee(self, i_employee):
        if i_employee in self.a_listEmployee:
            return
        self.a_listEmployee.append(i_employee)
        i_employee.addCenter(self)

    ## @fn Destructor of the class Center
    #
    def __del__(self):
        db.removeCenter(self)
#------------------------------------------------------------------------------------------------------------------------
## @class ListCenterFromFetch center.py
#  @brief Class of the list of all the objects Location
#  @sa Customer
#
class ListCenterFromFetch(list):

    ## @fn __init__(self,fetch_result)
    #  @brief Constructor of the class ListCenterFromFetch
    #  @param fetch_result Results table from the query
    #
    def __init__(self,fetch_result):
        for row in fetch_result:
            center = db.getCenter(row[0])
            if center:
                self.append(center)
            else:
                service = db.getService(row[2])
                self.append(Center(row[0],row[1],row[3],service))
