import pandas as pd
import matplotlib.pyplot as plt

# Cargamos los datos desde los archivos CSV en DataFrames
df_estudiantes = pd.read_csv('Datos/DIRI/DIRI Consolidado mov. estud.csv')
df_docentes = pd.read_csv('Datos/DIRI/DIRI Mov. Docente.csv')
df_mov_estudiantil = pd.read_csv('Datos/DIRI/DIRI Mov.estudiantil.csv')

# Calculamos el total de movimientos estudiantiles por año y período
total_estudiantes_por_periodo = df_estudiantes.groupby('Año y período')['TOTAL'].sum()

# Calculamos el total de movimientos docentes por año y período
total_docentes_por_periodo = df_docentes['PE  Periodo movilidad'].value_counts()

# Calculamos el total de movimientos estudiantiles y docentes por año y período
total_movimientos_por_periodo = total_estudiantes_por_periodo.add(total_docentes_por_periodo, fill_value=0)

# Creamos el gráfico circular
plt.figure(figsize=(8, 8))
plt.pie(total_movimientos_por_periodo, labels=total_movimientos_por_periodo.index, autopct='%1.1f%%', startangle=90, colors=plt.cm.Paired.colors)
plt.title('Distribución de Movimientos Estudiantiles y Docentes por Período')
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

# Mostramos el gráfico
plt.show()
