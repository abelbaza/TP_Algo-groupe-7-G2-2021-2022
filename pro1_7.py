# -*- coding: utf-8 -*-
"""
Created on Tue Jan  3 15:16:32 2023 TP ALGO PROJET 1
@author: 
    Gr7 :
        BAZAYAMA MBOTI Abel
        METENA M'NTEBA Yves
        YEKWA WAYANDIRI John
"""
"""REPONSE 1"""

from abc import ABCMeta, abstractmethod #importation du module abc qui gère les classes abstraites
from math import pi, sqrt #importation des fonctions pi et sqrt depuis math

class Geo_Form(metaclass = ABCMeta): #definition de la classe mère
    @abstractmethod     #mention d'appel pour rendre la methode abstraite
    def perimetre(): #methode abstraite pour perimetre sans retour
        pass

    @abstractmethod
    def surface():
        pass
    
    def decris_toi(self): #methode de la description complete d'une figure
        print("Pour la figure {}\nPerimetre : {}\nSurface : {}".format(self.nomF, self.perimetre(), self.surface()))

"""REPONSE 2"""

#classe Retangle qui herite de la classe mère Geo_Form      
class Rectangle(Geo_Form): 
    try: #gestion des exceptions
        def __init__(self,nomF, longueur, largeur): #initialisation de la classe Rectangle avec nom, long, largueur
            #initialistation des variables internes de la classe
            self.nomF = nomF 
            self.longueur = longueur
            self.largeur = largeur
        #methode de calcul du perimetre
        def perimetre(self): 
            return 2*self.longueur + 2*self.largeur
        #methode de calcul de la surface
        def surface(self):
            return self.longueur*self.largeur
    except: #gestion des exceptions
        print("Parametres non pris en charge")

#classe Cercle qui herite de la classe mère Geo_Form
class Cercle(Geo_Form):  
    try:
        def __init__(self, nomF, rayon):
            self.nomF = nomF
            self.rayon = rayon
        def perimetre(self):
            return 2*pi*self.rayon
        def surface(self):
            return  pi*(self.rayon**2)
    except:
        print("Parametres non pris en charge")

#classe Triangle qui herite de la classe mère Geo_Form 
class Triangle(Geo_Form):
    try:
        def __init__(self,nomF, coteA,coteB,coteC):
            self.nomF = nomF
            self.coteB = coteB
            self.coteA = coteA
            self.coteC = coteC
        def perimetre(self):
            return self.coteB + self.coteA + self.coteC

        def surface(self):
            p = self.perimetre()/2
            aire = sqrt(p*(p - self.coteA)*(p - self.coteB)*(p - self.coteC))
            aire = aire.real
            return aire
    except:
        print("Parametres non pris en charge")

"""REPONSE 4"""

#classe Carre qui herite de la classe Retangle 
class Carre(Rectangle):
    try:
        def __init__(self,nomF, cote):
            Rectangle.__init__(self, nomF, cote, cote)
    except:
        print("Parametres non pris en charge ")

#classe TriangleRectangle qui herite de la classe Triangle 
class TriangleRectangle(Triangle):
    try:
        def __init__(self,nomF, base, hauteur):
            hyp = sqrt(base**2+hauteur**2)
            Triangle.__init__(self, nomF, base, hauteur, hyp)
    except:
        print("Parametres non pris en charge ")

"""REPONSE 5"""

#classe GeoFig exploite toutes les autres classes de la Geo_Form
class GeoFig():  
    try:
        def __init__(self):
            self.gGeo_rep = []
        def add(self, fig):
            self.gGeo_rep.append(fig)
        def decris_toi(self):
            for g in self.gGeo_rep:
                print("Pour la figure {}\nPerimetre : {}\nSurface : {}".format(g.nomF, g.perimetre(), g.surface()))
    except:
        print("Parametres non pris en charge")
