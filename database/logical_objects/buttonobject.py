from kivy.uix.button import Button
from user.singleton import Singleton
from database.logical_objects.object import ObjectGeneral
from database.logical_objects.center import Center
from database.logical_objects.service import Service
from database.logical_objects.employee import Employee
from database.logical_objects.expense import Expense


#------------------------------------------------------------------------------------------------------------------------
## @class ButtonObjectGeneral ButtonObjectGeneral.py
#  @brief Class of the object ButtonObjectGeneral.
#  @sa ObjectGeneral
#
class ButtonFactory (metaclass=Singleton):

    def __init__(self):
        self.factories.addFactory(0, ButtonObjectClassic.Factory)
        self.factories.addFactory(1, ButtonObjectCenter.Factory)
        self.factories.addFactory(2, ButtonObjectService.Factory)
        self.factories.addFactory(3, ButtonObjectEmployee.Factory)
        self.factories.addFactory(4, ButtonObjectExpense.Factory)
        print("initialisation de la Factory")

    def addFactory(index, newFactory):
        ButtonFactory.factories.put[index] = newFactory

    addFactory = staticmethod(addFactory)

    # A Template Method:
    #* 0: ButtonObjectClassic.Factory
    #* 1: ButtonObjectCenter.Factory
    #* 2: ButtonObjectService.Factory
    #* 3: ButtonObjectEmployee.Factory
    #* 4: ButtonObjectExpense.Factory
    def createButton(index):
        if not ButtonFactory.factories.has_key(index):
            ButtonFactory.factories[index] = eval(index + '.Factory()')
        return ShapeFactory.factories[index].create()

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
    def __init__(self, text, genObject):
        super(ButtonObjectGeneral, self).__init__(text)
        self.a_object = genObject

#------------------------------------------------------------------------------------------------------------------------
## @class ButtonObjectGeneral ButtonObjectGeneral.py
#  @brief Class of the object ButtonObjectGeneral.
#  @sa ObjectGeneral
#
class ButtonObjectClassic(ButtonObjectGeneral):
    ## @fn  __init__(self, GenObject)
    #  @brief Constructor of the class ButtonObjectGeneral.
    #  @param GenObject The General Object.
    #
    def __init__(self, classicObject):
        super(ButtonObjectClassic, self).__init__(classicObject.a_name, classicObject)

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
        super(ButtonObjectCenter, self).__init__(center.a_location.a_name+ +center.a_service.a_name+ +center.a_description, center)

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
        super(ButtonObjectCenter, self).__init__(service.a_location.a_name+ +service.a_description, service)

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
        super(ButtonObjectCenter, self).__init__(employee.a_name+ +employee.a_surname, employee)

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
        super(ButtonObjectCenter, self).__init__(expense.a_price+ +expense.a_comment, expense)

    class Factory:
        def create(self, objct)): return self.__init__(self, objct)
