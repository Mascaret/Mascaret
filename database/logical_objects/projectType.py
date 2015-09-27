from database.logical_objects.object import ObjectGeneral

#------------------------------------------------------------------------------------------------------------------------
## @class ProjectType projectType.py
#  @brief Class of the object ProjectType.
#  @sa Project
#
class ProjectType(ObjectGeneral):
    ## @fn __init__(self, index, name, legalEntity)
    #  @brief Constructor of the class ProjectType.
    #  @param index Permission index.
    #  @param name Name of this ProjectType.
    #  @param listProjects The Peojects of this type.
    #
    def __init__(self, index, name, listProjects = []):
        self.a_index = int(index)
        self.a_name = str(name)
        self.a_listProjects = listProjects
        db.addProjectType(self)

    ## @fn Destructor of the class ProjectType
    #
    def __del__(self):
        db.removeProjectType(self)

    def addProject(self, i_project):
        if i_project.a_projectTyp != self:
            return
        self.a_listProjects.append(i_project)
