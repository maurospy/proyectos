# -*- coding: utf-8 -*-
"""
Editor de Spyder
@author: Ivan Carrascal
"""
 
import numpy as np
import scipy as stats
import pandas as pd
from matplotlib import pyplot as plt

info=pd.read_csv('PE.csv',header=0)
#Definiendo columna Applications
apl=info.ix[:,1]
#DEFINICION DE LOS EJES
x=info.ix[:,0]
y=info.ix[:,2]
#INSTRUCCIÓN PARA GENERAR GRÁFICO
plt.plot(x,y)
plt.xlabel('Usuarios')
plt.ylabel('Aplicaciones')
#Hallando la media 
print ('La media es:')
print (apl.mean())
#Hallando la moda
print ('La moda es:')
print (apl.mode())
#Hallando la mediana
print ('La mediana es:')
print (apl.median())
#Hallando la desviación estandar
print ('La desviación estandar es:')
print (apl.std())
