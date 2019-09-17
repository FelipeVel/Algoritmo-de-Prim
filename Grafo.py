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
        self.padres=list
        self.vActual=0
        for i in range(len(mAdyacencia)):
            self.marcados.append(0)
            self.costos.append(99)
            self.padres.append(0)
    
    def Prim (self):
        self.marcados[self.vActual]=1
        self.costos[self.menorCosto(self.vActual)]=self.mAdyacencia[self.vActual][self.menorCosto(self.vActual)]
        
        return 0
        
    #Buscar el menor costo de un vertice con sus adyacentes
    def menorCosto(self, vertice):
        menor=99
        for i in range(len(self.mAdyacencia)):
            if self.mAdyacencia[vertice][i]>0 and self.mAdyacencia[vertice][i]<menor:
                menor=i
        return menor
    
    