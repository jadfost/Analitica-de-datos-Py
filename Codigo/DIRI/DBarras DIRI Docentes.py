import pandas as pd
import matplotlib.pyplot as plt

# Cargamos los datos desde el archivo CSV en un DataFrame
df_docentes = pd.read_csv('Datos/DIRI/DIRI Mov. Docente.csv', dtype={'PE  Periodo movilidad': float, 'PS Periodo movilidad': float})

# Contar la frecuencia de aparición de cada docente en PE
frecuencia_pe = df_docentes['PE - Docente Nacional'].value_counts()

# Tomar los tres docentes con más movimientos en PE
top_docentes_pe_nacional = frecuencia_pe.head(3)

# Contar la frecuencia de aparición de cada docente en PS
frecuencia_ps = df_docentes['PS - Docente Nacional'].value_counts()

# Tomar los tres docentes con más movimientos en PS
top_docentes_ps_nacional = frecuencia_ps.head(3)

# Lista de nombres de los docentes con más movimientos en PE - Docente Nacional
nombres_docentes_pe = top_docentes_pe_nacional.index.tolist()
# Lista de valores de movimientos para los docentes con más movimientos en PE - Docente Nacional
movilidades_docentes_pe = top_docentes_pe_nacional.tolist()

# Lista de nombres de los docentes con más movimientos en PS - Docente Nacional
nombres_docentes_ps = top_docentes_ps_nacional.index.tolist()
# Lista de valores de movimientos para los docentes con más movimientos en PS - Docente Nacional
movilidades_docentes_ps = top_docentes_ps_nacional.tolist()

# Crear el gráfico de barras para PE
plt.figure(figsize=(15, 6))

plt.subplot(1, 2, 1)
plt.barh(nombres_docentes_pe, movilidades_docentes_pe, color='#F78F1E')

for i, v in enumerate(movilidades_docentes_pe):
    plt.text(v + 0.2, i, str(v), ha='left', va='center', fontsize=10)

plt.xlabel("Número de Movimientos")
plt.title("Tres Docentes con más Movimientos en PE - Docente Nacional")

# Crear el gráfico de barras para PS
plt.subplot(1, 2, 2)
plt.barh(nombres_docentes_ps, movilidades_docentes_ps, color='#F78F1E')

for i, v in enumerate(movilidades_docentes_ps):
    plt.text(v + 0.2, i, str(v), ha='left', va='center', fontsize=10)

plt.xlabel("Número de Movimientos")
plt.title("Tres Docentes con más Movimientos en PS - Docente Nacional")

plt.tight_layout()
plt.show()
