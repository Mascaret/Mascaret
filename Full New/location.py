class Location:

    def __init__(self,loc_id,loc_intitule,loc_ent_jur):
        self.loc_id = loc_id
        self.loc_intitule = loc_intitule
        self.loc_ent_jur = loc_ent_jur

    def delete():
        pass 
class ListLocationFromFetch(list):

    def __init__(self,fetch_result):
        for row in fetch_result:
            self.append(Location(row[0],row[1],row[2]))
