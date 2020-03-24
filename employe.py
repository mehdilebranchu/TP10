from salarie import *
class employe(salarie):
    def __init__(self, anneeEmbauche, nbJTrav, nom, prenom, salaire, id):
        salarie.__init__(self, nom, prenom, salaire, id)
        self._anneeEmbauche = anneeEmbauche
        self._nbJTrav = nbJTrav

    def afficher(self,site):
        pass
