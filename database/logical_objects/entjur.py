#Class of the object Legal Entity
class EntJur:

    def __init__(self,Id,intitule):
        self.Id = Id
        self.intitule = intitule
        
#Class of the list of all the objects Legal Entity
class ListEntJur(list):

    def __init__(self,ent_jur_fetched):
        for row in ent_jur_fetched:
            self.append(EntJur(int(row[0]),str(row[1])))
