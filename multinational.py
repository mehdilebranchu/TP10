from filiale import *

class multinational:
    def __init__(self, nom, paysdor):
        self.__nom = nom
        self.__paysdor = paysdor
        self.__listefiliale = []

    def addFiliale(self,filiale):
        self.__listefiliale.append(filiale)

    def paysChange(self,nomSalarie):
        for i in self.__listefiliale:
            for j in self.__listefiliale[i]:
                if j.getNom() == nomSalarie :

                    i.delsalarie(j)

    def afficher(self):
        print("la multinational RCAT est composé de ", len(self.__listefiliale)," filiales. Son pays d'origine est : ", self.__paysdor)
        for i in range(0, len(self.__listefiliale)-1):
            d = self.__listefiliale[0]
            date = d.getDate()
            c = self.__listefiliale[i]
            date1 = self.__listefiliale[i].getDate()
            if date1 < date:
                self.__listefiliale[0] = c
                self.__listefiliale[i] = d

        print("la filiale la plus ancienne de cette multinational ",self.__paysdor," est ", self.__listefiliale[0].getNom()," elle est composée de ",self.__listefiliale[0].getSalarie(), " salarié " )
        nbSalar = 0
        for nbs in self.__listefiliale :
            a = nbs.getSalarie()
            nbSalar += a
        print(self.__nom," est composé de ",nbSalar," salaries : ")
        for fil in self.__listefiliale :
                site = fil.getPays()
                fil.Afficher(site)
