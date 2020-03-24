from salarie import *

class filiale:
    def __init__(self, nom, pays, datecrea):
        self.__nom = nom
        self.__pays = pays
        self.__datecrea = datecrea
        self._salarie = []

    def addSalarie(self, salarie):
        self._salarie.append(salarie)

    def delSalarie(self, salarie):
        self._salarie.remove(salarie)


    def getPays(self):
        a = self.__pays
        return a
    def getDate(self):
        b = self.__datecrea
        return b
    def getNom(self):
        no = self.__nom
        return no
    def getSalarie(self):
        nb = len(self._salarie)
        return nb

    def Afficher(self,site):
        for i in self._salarie:
            i.afficher(site)
