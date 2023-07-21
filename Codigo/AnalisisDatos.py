import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('Codigo/EstudiantesRendimiento.csv')
df1 = pd.read_csv('Codigo/Paises.csv')




with_edc = len(df[df['parental level of education']!='some college'])

print('Número de solicitantes con educación superior:',with_edc)

female = len(df[df['gender']=='female'])
print('Número de Mujeres:',female)
male = len(df[df['gender']=='male'])
print('Número de Hombres:',male)

print('Número de alumnos pertenecientes al grupo A:',len(df[df['race/ethnicity']=='group A']))
print('Número de alumnos pertenecientes al grupo B:',len(df[df['race/ethnicity']=='group B']))
print('Número de alumnos pertenecientes al grupo C:',len(df[df['race/ethnicity']=='group C']))
print('Número de alumnos pertenecientes al grupo D:',len(df[df['race/ethnicity']=='group D']))
print('Número de alumnos pertenecientes al grupo E:',len(df[df['race/ethnicity']=='group E']))

#--------------------------------------------------------------------------------------




print('\n \nNúmero total de países:',len(df1['Country']))
print('PIB promedio de todos los países:', int(df1['GDP ($ per capita)'].mean()) )

