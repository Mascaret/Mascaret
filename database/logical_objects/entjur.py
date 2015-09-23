from database.logical_objects.object import ObjectGeneral

#------------------------------------------------------------------------------------------------------------------------
## @class LegalEntity entjur.py
#  @brief Class of the object LegalEntity.
#  @sa Location
#
class LegalEntity(ObjectGeneral):
    ## @fn __init__(self, index, name, listLocations = [], listWbsElements = [])
    #  @brief Constructor of the class LegalEntity.
    #  @param index Permission index.
    #  @param name Name of this Employee.
    #  @param listLocations  List of Locations this Legal Entity is linked to.
    #  @param listWbsElements  List of wbsElements this Legal Entity has.
    #
    def __init__(self, index, name, listLocations = [], listWbsElements = []):
        self.a_index = int(index)
        self.a_name = str(name)
        self.a_listLocations = list_locations
        self.a_listWbsElements = list_wbsElements

#------------------------------------------------------------------------------------------------------------------------
## @class ListLegalEntity entjur.py
#  @brief Class of the object ListLegalEntity.
#  @sa LegalEntity
#
class ListLegalEntity(list):
    ## @fn __init__(self, legalEntityFetched)
    #  @brief Constructor of the class ListLegalEntity.
    #  @param legalEntityFetched List of legal Entities.
    #
    def __init__(self, legalEntityFetched):
        for row in legalEntityFetched:
            self.append(LegalEntity(int(row[0]),str(row[1])))
