from kivy.uix.button import Button
from database.logical_objects.object import ObjectGeneral

#------------------------------------------------------------------------------------------------------------------------
## @class ButtonObjectGeneral ButtonObjectGeneral.py
#  @brief Class of the object ButtonObjectGeneral.
#  @sa ObjectGeneral
#
class ButtonFactory:
    factories = {}
    def addFactory(id, newFactory):
        ButtonFactory.factories.put[id] = newFactory
    addFactory = staticmethod(addFactory)
    # A Template Method:
    def createButton(id):
        if not ButtonFactory.factories.has_key(id):
            ButtonFactory.factories[id] = eval(id + '.Factory()')
        return ShapeFactory.factories[id].create()
    createButton = staticmethod(createButton)

#------------------------------------------------------------------------------------------------------------------------
## @class ButtonObjectGeneral ButtonObjectGeneral.py
#  @brief Class of the object ButtonObjectGeneral.
#  @sa ObjectGeneral
#
class ButtonObjectGeneral(Button):
    ## @fn  __init__(self, GenObject)
    #  @brief Constructor of the class ButtonObjectGeneral.
    #  @param GenObject The General Object.
    #
    def __init__(self, genObject):
        self.a_object = genObject

#------------------------------------------------------------------------------------------------------------------------
## @class ButtonObjectGeneral ButtonObjectGeneral.py
#  @brief Class of the object ButtonObjectGeneral.
#  @sa ObjectGeneral
#
class ButtonObjectClassic(Button):
    ## @fn  __init__(self, GenObject)
    #  @brief Constructor of the class ButtonObjectGeneral.
    #  @param GenObject The General Object.
    #
    def __init__(self, classicObject):
        super(ButtonObjectGeneral, self).__init__(classicObject.a_name)
        ButtonClassic.__init__(self, classicObject)

    class Factory:
        def create(self, objct)): return self.__init__(self, objct)

#------------------------------------------------------------------------------------------------------------------------
## @class ButtonObjectCenter ButtonObject.py
#  @brief Class of the object ButtonObjectCenter.
#
class ButtonObjectCenter(ButtonObjectGeneral):
    ## @fn  __init__(self, center)
    #  @brief Constructor of the class ButtonObjectCenter.
    #  A button which contains a object from the class center.
    #  @param center The center object.
    #
    def __init__(self, center):
        super(ButtonObjectCenter, self).__init__(center.a_location.a_name+ +center.a_service.a_name+ +center.a_description)
        ButtonClassic.__init__(self, center)

    class Factory:
        def create(self, objct)): return self.__init__(self, objct)

#------------------------------------------------------------------------------------------------------------------------
## @class ButtonObjectService ButtonObject.py
#  @brief Class of the object ButtonObjectService.
#
class ButtonObjectService(ButtonObjectGeneral):
    ## @fn  __init__(self, service)
    #  @brief Constructor of the class ButtonObjectService.
    #  A button which contains a object from the class Service.
    #  @param service The service object.
    #
    def __init__(self, service):
        super(ButtonObjectCenter, self).__init__(service.a_location.a_name+ +service.a_description)
        ButtonClassic.__init__(self, service)

    class Factory:
        def create(self, objct)): return self.__init__(self, objct)

#------------------------------------------------------------------------------------------------------------------------
## @class ButtonObjectService ButtonObject.py
#  @brief Class of the object ButtonObjectService.
#
class ButtonObjectEmployee(ButtonObjectGeneral):
    ## @fn  __init__(self, employee)
    #  @brief Constructor of the class ButtonObjectEmployee.
    #  A button which contains a object from the class Employee.
    #  @param employee The service employee.
    #
    def __init__(self, employee):
        super(ButtonObjectCenter, self).__init__(employee.a_name+ +employee.a_surname)
        ButtonClassic.__init__(self, employee)

    class Factory:
        def create(self, objct)): return self.__init__(self, objct)

#------------------------------------------------------------------------------------------------------------------------
## @class ButtonObjectService ButtonObject.py
#  @brief Class of the object ButtonObjectService.
#
class ButtonObjectExpense(ButtonObjectGeneral):
    ## @fn  __init__(self, expense)
    #  @brief Constructor of the class ButtonObjectExpense.
    #  A button which contains a object from the class Expense.
    #  @param expense The service expense.
    #
    def __init__(self, expense):
        super(ButtonObjectCenter, self).__init__(expense.a_price+ +expense.a_comment)
        ButtonClassic.__init__(self, expense)

    class Factory:
        def create(self, objct)): return self.__init__(self, objct)
