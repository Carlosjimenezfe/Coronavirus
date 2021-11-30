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

"""
8. Número de departamentos afectados
"""
Departamentos = len(data.groupby('Nombre departamento').size())
print(f'EL numero de municipios afectado es de: {Departamentos}')

"""
9.Liste los departamentos afectados(sin repetirlos)
"""
data['Nombre departamento'].replace('Caldas', 'CALDAS', inplace=True)
data['Nombre departamento'].replace('Tolima', 'TOLIMA', inplace=True)
l_departamentos = data.groupby('Nombre departamento').size().sort_values(ascending=False)
print(f'Lista de Departamentos afectados: {l_departamentos}')
 
"""
10. Ordene de mayor a menor por tipo de atención
"""
tipo_atencion = data.groupby('Ubicación del caso').size().sort_values(ascending=False)
print(f'{tipo_atencion}') 

"""
11. Liste de mayor a menor los 10 departamentos con mas casos de
contagiados
"""
orden_dpto= data.groupby('Nombre departamento').size().sort_values(ascending=False).head(10)
print(f'Los 10 departamentos con mas casos de contagiados son: {orden_dpto}')

"""
12. Liste de mayor a menor los 10 departamentos con mas casos de
fallecidos
"""
dpto_fallecidos = data[data['Recuperado'] == 'fallecido'].groupby('Nombre departamento').size().sort_values(ascending=False).head(10)
print(f'{dpto_fallecidos}') 

"""
13. Liste de mayor a menor los 10 departamentos con mas casos de
recuperados
"""
dpto_recuperados = data[data['Recuperado'] == 'Recuperado'].groupby('Nombre departamento').size().sort_values(ascending=False).head(10)
print(f' {dpto_recuperados}')     

"""
14. Liste de mayor a menor los 10 municipios con mas casos de
contagiados
"""
mas_contagiados = data.groupby('Nombre municipio').size().sort_values(ascending=False).head(10)
print(f' {mas_contagiados}') 

"""
15. Liste de mayor a menor los 10 municipios con mas casos de
fallecidos
"""
casos_municipios = data[data['Recuperado'] == 'fallecido'].groupby('Nombre municipio').size().sort_values(ascending=False).head(10)
print(f'{casos_municipios}') 

"""
16. Liste de mayor a menor los 10 municipios con mas casos de
recuperados
"""
recuperado_municipio = data[data['Recuperado'] == 'Recuperado'].groupby('Nombre municipio').size().sort_values(ascending=False).head(10)
print(f'{recuperado_municipio}')  

"""
17. Liste agrupado por departamento y en orden de Mayor a menor las
ciudades con mas casos de contagiados
"""
dpto_ciudades = data.groupby(['Nombre departamento', 'Nombre municipio']).size().sort_values(ascending=False)
print(f'{dpto_ciudades}')  

"""
18. Número de Mujeres y hombres contagiados por ciudad por
departamento
"""
numero_personas = data.groupby(['Nombre departamento', 'Nombre municipio','Sexo']).size().sort_values(ascending=False)
print( f' {numero_personas}') 

"""
19. Liste el promedio de edad de contagiados por hombre y mujeres por
ciudad por departamento
"""
promedio = data.groupby( ['Nombre departamento', 'Nombre municipio', 'Sexo']).Edad.mean()
print(f'{promedio}')

"""
20. Liste de mayor a menor el número de contagiados por país de
procedencia
"""
procedencia = data['Nombre del país'].value_counts()
print(f'{procedencia}')     

"""
21. Liste de mayor a menor las fechas donde se presentaron mas
contagios
"""
fecha_contagios = data.groupby('Fecha de diagnóstico').size().sort_values(ascending=False)
print(f' {fecha_contagios}')

"""
23. Liste la tasa de mortalidad y recuperación que tiene cada
departamento
"""
tasa_mortalidad = (data[data['Recuperado'] == 'fallecido'].groupby('Nombre departamento').size() / len(data)) * 100
print(f' tasa de mortalidad por Departamento: {tasa_mortalidad}')
tasa_recuperacion = (data[data['Recuperado'] == 'Recuperado'].groupby('Nombre departamento').size() / len(data)) * 100
print(f'r tasa de recuperación por departamento: {tasa_recuperacion}')








tasa_recuperacion_dep = (data[data['Recuperado'] == 'Recuperado'].groupby('Nombre departamento').size() / len(data)) * 100
print(f'La lista por tasa de recuperación por departamento es: {tasa_recuperacion_dep}')