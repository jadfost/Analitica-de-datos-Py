import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Cargamos los datos desde el archivo CSV en un DataFrame
df = pd.read_csv('Datos/DIEG/DIEG Distinguidos.csv')

# Reemplazamos los valores "-" por NaN (Not a Number) de NumPy
df.replace('-', np.nan, inplace=True)

# Creamos una lista con los años para utilizar en las visualizaciones
years = ['2014', '2015', '2016-10', '2016-20', '2018', '2019', '2020-10', '2020-20', '2021-10', '2021-20']

# Eliminamos filas que contengan valores NaN en las columnas de años
df.dropna(subset=years, inplace=True)

# Graficamos la evolución de cada programa distinguido en DIEG
programas_distinguidos = df['PROGRAMA'].unique()
plt.figure(figsize=(10, 6))

for programa in programas_distinguidos:
    programa_data = df[df['PROGRAMA'] == programa]
    distinciones = programa_data.iloc[:, 3:].values.astype(float).tolist()[0]
    plt.pie(distinciones, labels=years, autopct='%1.1f%%', startangle=90)
    plt.title(f'Evolución del programa distinguido {programa} en DIEG')
    plt.axis('equal')  # Proporciona un aspecto de círculo en lugar de una elipse
    plt.legend(years, title='Años', loc='upper left', bbox_to_anchor=(1, 0, 0.5, 1))  # Muestra la leyenda fuera del gráfico
    plt.show()
