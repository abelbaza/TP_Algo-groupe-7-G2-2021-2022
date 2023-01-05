# -*- coding: utf-8 -*-
"""
Created on Wed Jan  4 17:42:46 2023

@author: congopromotion.store
"""

from bjk import Recta,Triangle,Cercle,Carree,Trianglerectange,Allgeo
if __name__ =='__main__':
    valor=Recta(9, 7)
    
    valeur=Cercle(10)
    
    number=Trianglerectange(8, 6)
    tri=Triangle(4,6,2 )
    
    cote=Carree(5)
    
    print("for this figure our perim is :",valor.calculperimetre())
    print("for this figure our surface is: ", valor.calculsurface())
    
    print("for this figure our perim is :",valeur.calculperimetre())
    print("for this figure our surface is: ", valeur.calculsurface())
    
    print("for this figure our perim is :",number.calculperimetre())
    print("for this figure our surface is: ", number.calculsurface())
    
    print("for this figure our perim is :",tri.calculperimetre())
    print("for this figure our surface is: ",tri.calculsurface())
    
    print("for this sqrt our perim is :",cote.calculperimetre())
    print("for this sqrt our surface is: ", cote.calculsurface())
    
    print("for this figure our perim is :",tri.calculperimetre())
    print("for this figure our surface is: ", tri.calculsurface())
    
    
        
    
    cool=Allgeo()
    
    cool.add(Recta(10,5))
    
    figA=Allgeo()
    
    figA.add(Cercle(7))
    
    figB=Allgeo()
    
    figB.add(Carree(25))
    
    figC=Allgeo()
    figD=Allgeo()
    
    figC.add(Trianglerectange(20, 25))
    figD.add(Triangle(5, 8,10))
    
    cool.showme()
    figA.showme()
    figB.showme()
    figC.showme()
    figD.showme()
    
    
    