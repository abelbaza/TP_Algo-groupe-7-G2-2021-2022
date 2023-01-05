# -*- coding: utf-8 -*-
"""
Created on Tue Jan  3 16:06:32 2023 TP ALGO PROJET 1
@author: 
    Gr7 :
        BAZAYAMA MBOTI Abel
        METENA M'NTEBA Yves
        YEKWA WAYANDIRI John
"""
"""REPONSE 7"""
from pro1_7 import Rectangle, Cercle, Triangle, Carre, TriangleRectangle, GeoFig

if __name__ == '__main__':
    print("Depuis les classes seules :")
    print()
    try:
        for i in range (1,501):
            rectangle = Rectangle("Rectangle A1", 12+i, 7)
            cercle = Cercle("Cercle A2", 14)
            triangle = Triangle("Triangle A3", 9, 6, 7)
            carre = Carre("Carré A4", 6)
            t_rectangle = TriangleRectangle("Triangle Rectangle A5", 5, 7)
        
            rectangle.decris_toi()
            print()
            cercle.decris_toi()
            print()
            triangle.decris_toi()
            print()
            carre.decris_toi()
            print()
            t_rectangle.decris_toi()
            print()
    except Exception:
        print("Parametres non pris en charge.")
    
    print()
    print()
    print("Depuis la classe Globale : ")
    print()
    for i in range (1,501):
        figA = GeoFig() 
        figB = GeoFig() 
        figC = GeoFig()
        figD = GeoFig()
        figE = GeoFig()
        
        figA.add(Rectangle("Rectangle B1", 12, 5))
        figB.add(Cercle("Cercle B2", 5))
        figC.add(Triangle("Triangle B3", 9, 6, 7))
        figD.add(Carre("Carré B4", 10))
        figE.add(TriangleRectangle("Triangle Rectangle", 5, 7))
        
        figA.decris_toi()
        figB.decris_toi()
        figC.decris_toi()
        figD.decris_toi()
        figE.decris_toi()
        
        try:
            figA.add(Rectangle("Rectangle B1", 12, 5))
            figB.add(Cercle("Cercle B2", 5))
            figC.add(Triangle("Triangle B3", 9, 6, 7))
            figD.add(Carre("Carré B4", 10))
            figE.add(TriangleRectangle("Triangle Rectangle", 5, 7))
            
            figA.decris_toi()
            figB.decris_toi()
            figC.decris_toi()
            figD.decris_toi()
            figE.decris_toi()
        except Exception:
            print("Parametres non pris en charge.")

print("le temps d'exe est : ",elaps)