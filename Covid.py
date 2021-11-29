# -*- coding: utf-8 -*-
"""
Created on Mon Nov 29 10:09:07 2021

@author: Usuario
"""
import pandas as pd

url = 'covid_22_noviembre.csv'
data = pd.read_csv(url)

"""
1. Número de casos de Contagiados en el País.
"""
n_casos = data.shape[0]
print(f'El numero de casos de contagios en el pais es de: {n_casos}')

"""
2. Número de Municipios Afectados
"""
municipios = len(data.groupby('Nombre municipio').size())
print(f'El numero de municipios afectados son: {municipios}')
