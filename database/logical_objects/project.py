from database.logical_objects.object import ObjectGeneral

#------------------------------------------------------------------------------------------------------------------------
## @class Project project.py
#  @brief Class of the object Project.
#  @sa ProjectType, Users, Location
#
class Project(ObjectGeneral):
    ## @fn __init__(self, index, name, applicationDate, rewardDate, closeDate, edit, modifying, projectTyp, customer, center = None, listWBSElement = [])
    #  @brief Constructor of the class Project.
    #  @param index Permission index.
    #  @param name Name of this Project.
    #  @param applicationDate The date the production of the project starts.
    #  @param rewardDate The date the project is won.
    #  @param closeDate The date the project closes.
    #  @param edit Boolean which indicates if the projet can be edited.
    #  @param modifying Boolean which indicates if the projet is being modified.
    #  @param projectTyp The ProjectType of the project.
    #  @param customer The Customer who asked for the project.
    #  @param center The center where the benefits of this project will go.
    #  @param listWBSElement The list of WBS Elements linked to this project.
    #
    def __init__(self, index, name, applicationDate, rewardDate, closeDate, edit, modifying, projectTyp, customer, center = None, listWBSElement = []):
        self.a_index = int(index)
        self.a_name = str(name)
        self.a_applicationDate = applicationDate
        self.a_rewardDate = rewardDate
        self.a_closeDate = closeDate
        self.a_edit = edit
        self.a_modifying = modifying
        self.a_projectTyp = projectTyp
        self.a_customer = customer
        self.a_center = center
        self.a_listWBSElement = listWBSElement
