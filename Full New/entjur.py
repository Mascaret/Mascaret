class EntJur:

    def __init__(self,ent_id,ent_name):
        self.ent_id = ent_id
        self.ent_name = ent_name

class ListEntJur(list):

    def __init__(self,ent_jur_fetched):
        for row in ent_jur_fetched:
            self.append(EntJur(int(row[0]),str(row[1])))
