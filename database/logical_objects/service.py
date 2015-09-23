from database.logical_objects.object import ObjectGeneral

#------------------------------------------------------------------------------------------------------------------------
## @class Service Service.py
#  @brief Class of the object Service.
#  @sa Service, Center
#
class Service(ObjectGeneral):
    ## @fn __init__(self, index, intitule, listUsers = [])
    #  @brief Constructor of the class Service.
    #  @param index Permission index.
    #  @param name Name of this ProjectType.
    #  @param location The location this service is linked to.
    #  @param listCenters The Centers this service contains
    #
    def __init__(self, index, name, location, listCenters = []):
        self.a_index = int(index)
        self.a_name = str(name)
        self.a_location = location
        self.a_listCenters = listCenters

    ## @fn delete()
    #  @brief Destructor of the class ProjectType.
    #
    def delete():
        pass


#------------------------------------------------------------------------------------------------------------------------
## @class ListServiceFromFetch Service.py
#  @brief Class of all the objects Service.
#  @sa Service
#
class ListServiceFromFetch(list):

    ## @fn __init__(self, index, intitule, listUsers = [])
    #  @brief Constructor of the class ListServiceFromFetch.
    #  @param fetch_result Results table from the query.
    #
    def __init__(self,fetch_result):
        for row in fetch_result:
            self.append(Service(row[0],row[2],row[1]))
