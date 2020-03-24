from employe import *
class admin(employe):
    def __init__(self, service, anneeEmbauche, nbJTrav, nom, prenom, salaire, id):
        employe.__init__(self, anneeEmbauche, nbJTrav, nom, prenom, salaire, id)
        self._service = service
    def afficher(self,site):
        print("[id=", self._id,"] Nom et prenom : ", self._nom," ",self._prenom, ", salaire : ",self._salaire,", statut : Administratif, annee d'embauche : ", self._anneeEmbauche ,", site : ",site, "nombre de jours de travail : ", self._nbJTrav, "Service : ", self._service)
