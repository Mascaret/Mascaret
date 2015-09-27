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
        self.a_location.addService(self)
        self.a_listCenters = listCenters
        db.addService(self)

    ## @fn Destructor of the class Service
    #
    def __del__(self):
        db.removeService(self)

    def addCenter(self, i_center):
        if i_center.a_service != self:
            return
        self.a_listCenters.append(i_center)



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
            service = db.getService(row[0])
            if service:
                self.append(service)
            else:
                location = db.getLocation(row[2])
                self.append(Service(row[0],row[1],location))
