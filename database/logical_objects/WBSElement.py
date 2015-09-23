from database.logical_objects.object import ObjectGeneral

#------------------------------------------------------------------------------------------------------------------------
## @class WBSElement WBSElement.py
#  @brief Class of the object WBS Element.
#  @sa WBSActivityCenter
#
class WBSElement(ObjectGeneral):
    ## @fn __init__(self, index, code, description, applicationDate, closeDate, codeType, wbsCA, legalEntity, listExpenses = [])
    #  @brief Constructor of the class WBSElement.
    #  @param index Permission index.
    #  @param code Code of the WBSElement.
    #  @param description Description of the WBSElement.
    #  @param applicationDate When this WBSElement starts.
    #  @param closeDate When this WBSElement ends.
    #  @param codeType The type of this WBSElement's code.
    #  @param wbsCA The WBSActivityCenter this WBSElement is linked to.
    #  @param legalEntity The LegalEntity this WBSElement is linked to.
    #  @param listExpenses The list of Expenses this WBSElement is linked to.
    #
    def __init__(self, index, code, description, applicationDate, closeDate, codeType, wbsCA, legalEntity, listExpenses = []):
        self.a_index = int(index)
        self.a_code = str(code)
        self.a_description = str(description)
        self.a_applicationDate = applicationDate
        self.a_closeDate = closeDate
        self.a_codeType = codeType
        self.a_wbsCA = wbsCA
        self.a_legalEntity = legalEntity
        self.a_listExpenses = listExpenses #peut etre une list nul = []
