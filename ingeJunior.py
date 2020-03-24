from Inge import *
class ingeJunior(inge) :
    def __init__(self, nbAnneeExp, nbHProj, nbHGestion, anneeEmbauche, nbJTrav, nom, prenom, salaire, id):
        inge.__init__(self, nbHProj, nbHGestion, anneeEmbauche, nbJTrav, nom, prenom, salaire, id)
        self.__nbAnneeExp = nbAnneeExp

    def afficher(self,site):
                print("[id=", self._id,"] Nom et prenom : ", self._nom," ",self._prenom, ", salaire : ",self._salaire,", statut : ingenieur junior, annee d'embauche : ", self._anneeEmbauche ,", site : ",site, "nombre de jours de travail : ", self._nbJTrav,"nombre d'heures de projet : ", self._nbHProj,"nombre d'heures de gestion : ",self._nbHGestion ," Nombre d'année d'expérience : ", self.__nbAnneeExp)
