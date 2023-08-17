import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Archivos CSV
df = pd.read_csv('Datos/DIRS/DIRS 1.csv')
df1 = pd.read_csv('Datos/DIRS/DIRS 2.csv')
df2 = pd.read_csv('Datos/DIRS/DIRS 3.csv')
df3 = pd.read_csv('Datos/DIRS/DIRS 4.csv')

# Concatenar los datos en un solo DataFrame
df = pd.concat([df, df1, df2, df3])

# Calcular la distribución porcentual de los estados de proyecto
estado_counts = df['ESTADO DEL PROYECTO'].value_counts()
total_projects = estado_counts.sum()
porcentajes = (estado_counts / total_projects) * 100

# Configuración del gráfico
labels = estado_counts.index
colors = ['blue', 'green', 'orange', 'red']
explode = (0.1, 0, 0, 0)  # Resaltar el primer segmento

# Crear el gráfico circular
plt.figure(figsize=(8, 6))
plt.pie(porcentajes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.title('Distribución porcentual de Estados de Proyectos de Proyección Social')
plt.show()