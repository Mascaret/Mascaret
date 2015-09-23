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
        self.a_listServices = listServices
        self.a_listProjects = listProjects

    ## @fn delete()
    #  @brief Destructor of the class Location.
    #
    def delete():
        pass

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
            self.append(Location(row[0],row[1],row[2]))
