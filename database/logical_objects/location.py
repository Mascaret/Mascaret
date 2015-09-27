from database.logical_objects.object import ObjectGeneral

#------------------------------------------------------------------------------------------------------------------------
## @class Location location.py
#  @brief Class of the object Location.
#  @sa Service, LegalEntity
#
class Location(ObjectGeneral):
    ## @fn __init__(self, index, name, legalEntity, listServices = [], listProjects = [])
    #  @brief Constructor of the class Location.
    #  @param index Permission index.
    #  @param name Name of this Location.
    #  @param legalEntity The legalEntity this Location is linked to.
    #  @param listServices The services this Location is composed of.
    #  @param listProjects The project linked to this Location.
    #
    def __init__(self, index, name, legalEntity, listServices = [], listProjects = []):
        self.a_index = index
        self.a_name = name
        self.a_legalEntity = legalEntity
        self.a_legalEntity.addLocation(self)
        self.a_listServices = listServices
        self.a_listProjects = listProjects
        db.addLocation(self)

    ## @fn delete()
    #  @brief Destructor of the class Location.
    #
    def delete():
        pass

    ## @fn Destructor of the class Location
    #
    def __del__(self):
        db.removeLocation(self)

    def addService(self, i_service):
        if i_service.a_location != self:
            return
        self.a_listServices.append(i_service)

    def addProject(self, i_project):
        if i_project.a_location != self:
            return
        self.a_listProjects.append(i_project)



## @class ListLocationFromFetch location.h
#  @brief Class of the list of all the objects Location
#  @sa Location
#
class ListLocationFromFetch(list):
    ## @fn __init__(self, fetchResult)
    #  @brief Constructor of the class ListLocationFromFetch.
    #  @param fetchResult Results table from the query
    #
    def __init__(self, fetchResult):
        for row in fetchResult:
            location = db.getLocation(row[0])
            if location:
                self.append(location)
            else:
                legalEntity = db.getLegalEntity(row[2])
                self.append(Location(row[0],row[1],legalEntity))
