from database.logical_objects.object import ObjectGeneral

#------------------------------------------------------------------------------------------------------------------------
## @class Center center.py
#  @brief Class of the object Center
#  @sa Employee, Service, WBSEElement, TypeCenterExpense
#
class Center(ObjectGeneral):
    ## @fn __init__(self, index, name, description, service, wbsElementList = [])
    #  @brief Constructor of the class Center.
    #  @param index Permission index.
    #  @param name Name of the Center.
    #  @param description Detailed description of the center.
    #  @param service Name of the service this center is related to.
    #  @param wbsElementList list of the wbsElement the center is related to.
    #
    def __init__(self, index, name, description, service, wbsElementList = []):
        self.a_index = int(index)
        self.a_num = num
        self.a_description = str(description)
        self.a_service = service
        self.a_location = service.location
        self.a_wbsElementList = wbsElementList

    ## @fn Destructor of the class Center
    #
    def delete():
        pass

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
            self.append(Center(row[0],row[1],row[3],row[2]))
