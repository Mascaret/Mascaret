#Class of the object Location
class Location:

    def __init__(self,Id,intitule,id_cor1):
        self.Id = Id
        self.intitule = intitule
        self.id_cor1 = id_cor1

    def delete():
        pass 

#Class of the list of all the objects Location
class ListLocationFromFetch(list):

    def __init__(self,fetch_result):
        for row in fetch_result:
            self.append(Location(row[0],row[1],row[2]))
