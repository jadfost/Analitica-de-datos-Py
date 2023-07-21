import pandas as pd
import matplotlib.pyplot as plt

# Leer el archivo CSV
df = pd.read_csv('Datos/DIEG/DIEG PIONEROS.csv')

# Crear una lista con los nombres de los programas académicos
programas_academicos = ['PIME', 'PIAM', 'MSIG', 'MIAM']

# Inicializar un diccionario para almacenar la cantidad de estudiantes pioneros por programa
estudiantes_pioneros_por_programa = {}

# Calcular la cantidad de estudiantes pioneros por programa académico y almacenar en el diccionario
for programa in programas_academicos:
    df_programa = df[df['PROGRAMA ACADÉMICO'] == programa]
    estudiantes_pioneros_por_programa[programa] = df_programa.iloc[:, 3:].sum().sum()

# Configurar el gráfico de barras
plt.bar(estudiantes_pioneros_por_programa.keys(), estudiantes_pioneros_por_programa.values(), color='skyblue')
plt.xlabel('Programa Académico')
plt.ylabel('Cantidad de Estudiantes Pioneros')
plt.title('Cantidad de Estudiantes Pioneros por Programa Académico')
plt.grid(axis='y')

# Agregar leyenda
plt.legend(['Estudiantes Pioneros'])

# Mostrar el gráfico
plt.show()
