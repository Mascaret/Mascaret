from database.logical_objects.object import ObjectGeneral

#------------------------------------------------------------------------------------------------------------------------
## @class Customer customer.py
#  @brief Class of the object Customer.
#  @sa Project, Address
#
class Customer(ObjectGeneral):
    ## @fn __init__(self, index, name, address, listProjects = [])
    #  @brief Constructor of the class customer.
    #  @param index Permission index.
    #  @param name Name of the customer.
    #  @param address this customer's address.
    #  @param listProjects  List of Project done for this customer.
    #
    def __init__(self, index, name, address, listProjects = []):
        self.a_index = int(index)
        self.a_name = str(name)
        self.a_address = address
        self.a_listProjects = listProjects