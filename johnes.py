# -*- coding: utf-8 -*-
"""
Created on Wed Jan  4 18:36:54 2023

@author: congopromotion.store
"""


from abc import ABCMeta,abstractmethod
from math import pi,sqrt
class Figuregeo(metaclass = ABCMeta):
    @abstractmethod
    def calculperimetre():
        pass
    @abstractmethod

    def calculsurface():
        pass
    
class Recta(Figuregeo):
    
    def __init__(self , longeur , largeur):
        
        self.x=longeur()
        
        self.y=largeur()
        
    def calculperimetre(self):
        
        return 2*self.x + 2*self.y
    
    def calculsurface(self):
        
        return self.x * self.y
    
class Cercle(Figuregeo):
    
    def __init__(self , radius):
        
        self.radius=radius
        
    def calculperimetre(self):
        
        return 2*pi* self.radius
    def calculsurface(self):
        return pi*(self.radius)**2
class Triangle(Figuregeo):
    def __init__(self, side1,side2 ,side3):
        self.a=side1
        self.b=side2
        self.c=side3
    def calculperimetre(self):
        return self.a + self.b +self.c
    def calculsurface(self):
        dp=(self.a+self.b+self.c)/2
        return sqrt(dp*(dp-self.a)*(dp-self.b)*(dp- self.c))
class Carree(Recta):
    def __init__(self, side):
        Recta.__init__(self,side , side)
class Trianglerectange(Triangle):
    def __init__(self, hauteur, base):
        hypothense= (hauteur)**2+(base)**2
        Triangle.__init__(self ,hauteur, base, hypothense)
        
def calculperimetre(p):
    return p.calculperimetre()
def calculsurface(v):
    return v.calculsurface()





