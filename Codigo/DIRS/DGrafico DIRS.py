import pandas as pd
import matplotlib.pyplot as plt

# Cargar los datos desde los archivos CSV
df1 = pd.read_csv('Datos/DIRS/DIRS 1.csv')
df2 = pd.read_csv('Datos/DIRS/DIRS 2.csv')
df3 = pd.read_csv('Datos/DIRS/DIRS 3.csv')
df4 = pd.read_csv('Datos/DIRS/DIRS 4.csv')

# Concatenar los datos en un solo DataFrame
df = pd.concat([df1, df2, df3, df4])

# Filtrar las actividades relacionadas con la atención primaria en salud y promoción de la salud
df_salud = df[(df['PROGRAMA O DEPENDENCIA'] == 'PMED') | (df['PROGRAMA O DEPENDENCIA'] == 'PMED')]

# Agrupar por año y contar la cantidad de actividades
actividades_por_año = df_salud.groupby('AÑO DE RELACIÓN')['NOMBRE DE LA ACTIVIDAD'].count()

# Configuración del gráfico
plt.figure(figsize=(10, 6))
actividades_por_año.plot(kind='bar', color='blue')
plt.xlabel('Año')
plt.ylabel('Cantidad de Actividades')
plt.title('Cantidad de Actividades de Atención Primaria en Salud y Promoción de la Salud por Año')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()