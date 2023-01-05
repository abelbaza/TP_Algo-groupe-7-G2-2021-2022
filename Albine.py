# -*- coding: utf-8 -*-
"""
Created on Wed Jan  4 18:41:27 2023

@author: congopromotion.store
"""
from johnes import Recta,Triangle,Cercle,Carree,Trianglerectange,calculperimetre,calculsurface
if __name__ =='main':
    valor=Recta(9, 7)
    
    valeur=Cercle(10)
    
    number=Trianglerectange(8, 6)
    tri=Triangle(5, 7, 8)
    
    cote=Carree(5)
    
    print("for this figure our perim is :",calculperimetre(valor))
    print("for this figure our surface is: ",calculsurface(valor))
    
    print("for this figure our perim is :",calculperimetre(valeur))
    print("for this figure our surface is: ", calculsurface(valeur))
    
    print("for this figure our perim is :",calculperimetre(number))
    print("for this figure our surface is: ",calculsurface(number))
    
    print("for this figure our perim is :",calculperimetre(tri))
    print("for this figure our surface is: ",calculsurface(tri))
    
    print("for this sqrt our perim is :",calculperimetre(cote))
    print("for this sqrt our surface is: ", calculsurface(cote))
    
   