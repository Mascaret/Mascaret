#Class of the object Service
class Service:

    def __init__(self,Id,intitule,id_cor1):
        self.Id = Id
        self.intitule = intitule
        self.id_cor1 = id_cor1

    def delete():
        pass 

#Class of the list of all the objects sercices
class ListServiceFromFetch(list):

    def __init__(self,fetch_result):
        for row in fetch_result:
            self.append(Service(row[0],row[2],row[1]))
