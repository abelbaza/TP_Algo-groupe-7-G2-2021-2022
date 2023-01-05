# -*- coding: utf-8 -*-
"""
Created on Tue Jan  3 16:06:32 2023 TP ALGO PROJET 1
@author: 
    Gr7 :
        BAZAYAMA MBOTI Abel
        METENA M'NTEBA Yves
        YEKWA WAYANDIRI John
"""
"""REPONSE 8"""
from pro1_8 import Rectangle, Cercle, Triangle, Carre, TriangleRectangle, tout_perimetre, tout_superficie
if __name__ == '__main__':
    try:
        for i in range (1,501):
            rectangle = Rectangle("Rectangle A1", 14, 7)
            cercle = Cercle("Cercle A2", 14)
            triangle = Triangle("Triangle A3", 9, 6, 7)
            carre = Carre("Carré A4", 6)
            t_rectangle = TriangleRectangle("Triangle Rectangle A5", 5, 7)
            
            print("Pour le polymorphisme\n")
            print("{} :\nPerimetre : {}\nSurface : {}".format(rectangle.nomF, tout_perimetre(rectangle), tout_superficie(rectangle)))
            print("{} :\nPerimetre : {}\nSurface : {}".format(cercle.nomF, tout_perimetre(cercle), tout_superficie(cercle)))
            print("{} :\nPerimetre : {}\nSurface : {}".format(triangle.nomF, tout_perimetre(triangle), tout_superficie(triangle)))
            print("{} :\nPerimetre : {}\nSurface : {}".format(carre.nomF, tout_perimetre(carre), tout_superficie(carre)))
            print("{} :\nPerimetre : {}\nSurface : {}".format(t_rectangle.nomF, tout_perimetre(t_rectangle), tout_superficie(t_rectangle)))     
    except Exception:
        print("Parametres non pris en charge.")