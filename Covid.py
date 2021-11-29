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
print(f'EL numero de municipios afectado es de: {municipios}')

"""
3. Liste los municipios afectados (sin repetirlos)
"""

l_municipios = data.groupby('Nombre municipio').size().sort_values(ascending=False)
print(f'\nMunicipios afectados: {l_municipios}') 

"""
4. Número de personas que se encuentran en atención en casa
"""
data['Ubicación del caso'].replace('Casa', 'CASA', inplace=True)
data['Ubicación del caso'].replace('casa', 'CASA', inplace=True) 

atencion_casa = len(data[data['Ubicación del caso'] == 'CASA'])
print(f'El numeroo de personas que se encuentran en atención en casa: {atencion_casa}')

"""
5. Número de personas que se encuentran recuperados
"""
recuperados = data[data['Recuperado'] == 'Recuperado'].shape[0]
print(f'El total de  personas recuperada es de: {recuperados}') 

"""
6. Número de personas que ha fallecido
"""
fallecidos = data[data['Estado'] == 'Fallecido'].shape[0]
print(f'El total de personas fallecidas en Colombia es de: {fallecidos}')

"""
7. Ordenar de Mayor a menor por tipo de caso (Importado, en estudio,
Relacionado)
"""
importado = data.groupby('Tipo de contagio').size().sort_values(ascending=False)
print(f'{importado}')