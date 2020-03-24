from employe import *
class inge(employe):
    def __init__(self, nbHProj, nbHGestion, anneeEmbauche, nbJTrav, nom, prenom, salaire, id):
        employe.__init__(self, anneeEmbauche, nbJTrav, nom, prenom, salaire, id)
        self._nbHProj = nbHProj
        self._nbHGestion = nbHGestion

    def afficher(self,site):
        pass
