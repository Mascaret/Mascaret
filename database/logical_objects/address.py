
#------------------------------------------------------------------------------------------------------------------------
## @class Address adress.h
#  @brief Class of the object Address
#  @sa Customer
#
class Address:
    ## @fn __init__(self, index, streetNumber = None, streetType = None, streetName = None, zipCode, city, country, customer)
    #  @brief Constructor of the class Address.
    #  @param index Local index.
    #  @param street Number the number in the street.
    #  @param streetType Type of the street (Place, street, ...).
    #  @param streetName Name of the street.
    #  @param zipCode Address ZipCode.
    #  @param city
    #  @param country
    #  @param customer The Customer to whom this address is related to.
    #
    def __init__(self, index, streetNumber = None, streetType = None, streetName = None, zipCode, city, country, customer):
        self.a_index = int(index)
        self.a_streetNumber = int(streetNumber)
        self.a_streetType = str(streetType)
        self.a_streetName = str(streetName)
        self.a_zipCode = str(zipCode)
        self.a_city = str(city)
        self.a_country = str(country)
        self.a_customer = customer
