#Class of the object Center
class Center:

    def __init__(self,Id,intitule,id_cor1,desc):
        self.Id = Id
        self.intitule = intitule
        self.id_cor1 = id_cor1
        self.desc = desc

    def delete():
        pass 

#Class of the list of all the objects Location
class ListCenterFromFetch(list):

    def __init__(self,fetch_result):
        for row in fetch_result:
            self.append(Center(row[0],row[1],row[3],row[2]))
