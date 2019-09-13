# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 17:17:39 2019

@author: estudiantes
"""

class Grafo:
    
    def __init__(self, mAdyacencia):
        self.mAdyacencia = mAdyacencia
        self.marcados=list
        self.costos=list
        self.vActual=0
        for i in range(len(mAdyacencia)):
            self.marcados.append(0)
            self.costos.append(99)
    
    def Prim (self):
        menorCosto=99
        for i in range(len(self.mAdyacencia)):
            if self.mAdyacencia[self.vActual][i]>0 and self.mAdyacencia[self.vActual][i]<menorCosto:
                self.vActual=i
                menorCosto=self.mAdyacencia[self.vActual][i]
        self.costos[self.vActual]=menorCosto