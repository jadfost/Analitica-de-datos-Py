import pandas as pd
import matplotlib.pyplot as plt

# Cargamos los datos desde los archivos CSV en DataFrames
df_estudiantes = pd.read_csv('Datos/DIRI/DIRI Consolidado mov. estud.csv')
df_docentes = pd.read_csv('Datos/DIRI/DIRI Mov. Docente.csv')
df_mov_estudiantil = pd.read_csv('Datos/DIRI/DIRI Mov.estudiantil.csv')

# Calculamos el total de movimientos (estudiantes y docentes) por ciudad
total_movimientos_tunja = df_estudiantes['MOVILIDAD ESTUDIANTES SALIENTE TUNJA'].sum() + df_estudiantes['MOVILIDAD ESTUDIANTES ENTRATE TUNJA'].sum()
total_movimientos_chiquinquira = df_estudiantes['MES - CHIQUINQUIRÁ'].sum()
total_movimientos_sogamoso = df_estudiantes['MES - SOGAMOSO'].sum() + df_docentes['PS - Docente Nacional'].count()

# Creamos el gráfico de barras
ciudades = ['Tunja', 'Chiquinquirá', 'Sogamoso']
total_movimientos = [total_movimientos_tunja, total_movimientos_chiquinquira, total_movimientos_sogamoso]

plt.bar(ciudades, total_movimientos, color=plt.cm.Paired.colors)
plt.xlabel('Ciudad')
plt.ylabel('Total de Movimientos')
plt.title('Distribución de Movimientos Estudiantiles y Docentes por Ciudad')
plt.show()
