class groupCostElement:
    def __init__(self,id_gce,intitule,classification,list_gce,list_costElement,list_center,list_wbaca):
        self.Id = int(id_gce)
        self.intitule = str(intitule)
        self.classification = classification # On lui passe un object classification prealablement cree
        self.list_gce = list_gce # Si pas de list de gce alors on passe une liste vide #CLementine c'est bien ?
        self.list_costElement = list_ce # peut etre NUL = []
        self.list_center = list_center # peut etre NUL = []
        self.list_wbaca = list_wbaca
