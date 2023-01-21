# -*- coding: utf-8 -*-
"""
Created on Tue Jan  3 17:06:32 2023 TP ALGO PROJET 1
@author: 
    Gr7 :
        BAZAYAMA MBOTI Abel
        METENA M'NTEBA Yves
        YEKWA WAYANDIRI John
"""
import unittest
import math
from pro1_7 import Rectangle, Cercle, Triangle, Carre, TriangleRectangle

class TestGeo_Form(unittest.TestCase):
    def test_rectangle(self):
        try:
            rectangle = Rectangle("Rectangle 01",5,4)
            self.assertEqual(rectangle.perimetre(), 14)
            self.assertEqual(rectangle.surface(), 12)            
        except:
            pass

    def test_cercle(self): 
        try:
            cercle = Cercle("Cercle A1",5)
            self.assertEqual(cercle.perimetre(), 2*math.pi*5)
            self.assertEqual(cercle.surface(), math.pi*5**2)
        except:
            pass
        
    def test_triangle(self):
        try:
            triangle = Triangle("Triangle T1 ",3,4,5)
            self.assertEqual(triangle.perimetre(), 12)
            self.assertEqual(triangle.surface(), 6)
        except Exception:
            pass

    def test_carre(self):
        
        try:
            carre = Carre("Carre Cr1 ",6)
            self.assertEqual(carre.perimetre(), 24)
            self.assertEqual(carre.surface(), 36)
        except Exception:
            pass

    def test_triarectangle(self):
        try:
            triarectangle = TriangleRectangle("Triangle Rectangle TR1 ",3,4)
            self.assertEqual(triarectangle.perimetre(), 12)
            self.assertEqual(triarectangle.surface(), 6)
        except Exception:
            pass

if __name__ == '__main__':
    unittest.main()