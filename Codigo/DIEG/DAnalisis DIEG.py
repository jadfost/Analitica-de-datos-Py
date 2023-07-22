import pandas as pd

# Cargar datos de DIEG PIONEROS desde el archivo CSV
df_pioneros = pd.read_csv('Datos/DIEG/DIEG PIONEROS.csv')

# Cargar datos de DIEGO Distinguidos desde el archivo CSV
df_distinguidos = pd.read_csv('Datos/DIEG/DIEG Distinguidos.csv')

# Remplazar los guiones '-' por 0 en ambos DataFrames
df_pioneros.replace('-', 0, inplace=True)
df_distinguidos.replace('-', 0, inplace=True)

# Convertir las columnas numéricas a valores numéricos
df_pioneros.iloc[:, 3:] = df_pioneros.iloc[:, 3:].apply(pd.to_numeric)
df_distinguidos.iloc[:, 3:] = df_distinguidos.iloc[:, 3:].apply(pd.to_numeric)

# Calcular la media y la suma de estudiantes para programas pioneros
df_pioneros['Media'] = df_pioneros.iloc[:, 3:].mean(axis=1)
df_pioneros['Total Estudiantes'] = df_pioneros.iloc[:, 3:].sum(axis=1)

# Calcular la media y la suma de estudiantes para programas distinguidos
df_distinguidos['Media'] = df_distinguidos.iloc[:, 3:].mean(axis=1)
df_distinguidos['Total Estudiantes'] = df_distinguidos.iloc[:, 3:].sum(axis=1)

# Crear un DataFrame para almacenar las sedes de pioneros y distinguidos
df_sedes = pd.DataFrame()
df_sedes['Sedes Pioneros'] = df_pioneros['SEDE']
df_sedes['Sedes Distinguidos'] = df_distinguidos['SEDE']

# Mostrar el DataFrame con las sedes de pioneros y distinguidos
print("Sedes de Programas Pioneros y Distinguidos en DIEG:")
print(df_sedes)
