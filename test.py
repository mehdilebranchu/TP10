from multinational import *
from directeur import *
from admin import *
from ingeJunior import *
from ingeSenior import *

ENT = multinational("RCAT", "France")
F1 = filiale("RCTA-Belgique", "Belgique", 2000)
F2 = filiale("RCTA-Maroc", "Maroc", 2010)
F3 = filiale("RCTA-Tunisie", "Tunisie", 1950)
F4 = filiale("RCTA-Angleterre", "Angleterre", 2005)
ENT.addFiliale(F1)
ENT.addFiliale(F2)
ENT.addFiliale(F3)
ENT.addFiliale(F4)
D1 = directeur(1960,"Jambon", "Beur", 8, 210)
F3.addSalarie(D1)
A1 = admin("RH",2003,562,"Jean", "Michel", 2, 300)
IJ1 = ingeJunior(4,50,64,2005,809,"Will", "Fred", 7, 230)
F1.addSalarie(A1)
F1.addSalarie(IJ1)
IS1 = ingeSenior("responsable prod",800,6050,2000,9004,"Jean", "Hugue", 9, 126)
F2.addSalarie(IS1)

ENT.afficher()

