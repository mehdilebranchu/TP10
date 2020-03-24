from Inge import *
class ingeSenior(inge):
    def __init__(self, resp, nbHProj, nbHGestion, anneeEmbauche, nbJTrav, nom, prenom, salaire, id):
        inge.__init__(self, nbHProj, nbHGestion, anneeEmbauche, nbJTrav, nom, prenom, salaire, id)
        self.__resp = resp

    def afficher(self,site):
        print("[id=", self._id,"] Nom et prenom : ", self._nom," ",self._prenom, ", salaire : ",self._salaire,", statut : ingenieur senior, annee d'embauche : ", self._anneeEmbauche ,", site : ",site, "nombre de jours de travail : ", self._nbJTrav,"nombre d'heures de projet : ", self._nbHProj,"nombre d'heures de gestion : ",self._nbHGestion ,"Responsabilité : ", self.__resp)
