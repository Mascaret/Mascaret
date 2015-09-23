from database.logical_objects.object import ObjectGeneral

#------------------------------------------------------------------------------------------------------------------------
## @class Classification classification.py
#  @brief Class of the object Classification.
#  Details how the costElement are ordered
#  @sa CostElement
#
class Classification(ObjectGeneral):
    ## @fn __init__(self, index, name, description)
    #  @brief Constructor of the class Classification.
    #  @param index Local index.
    #  @param name Name of the Classification.
    #  @param description Detailed description of the Classification.
    #
    def __init__(self, index, name, description):
        self.a_index = int(index)
        self.a_name = str(name)
        self.a_description = str(description)
