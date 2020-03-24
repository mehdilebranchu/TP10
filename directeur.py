from salarie import *
class directeur(salarie):
    def __init__(self, anneeNom, nom, prenom, salaire, id):
        salarie.__init__(self, nom, prenom, salaire, id)
        self.__anneeNom = anneeNom

    def afficher(self,site):
        print("[id=", self._id,"] Nom et prenom : ", self._nom," ",self._prenom, ", salaire : ",self._salaire,", statut : directeur, annee de nomination : ", self.__anneeNom,", site : ",site)


