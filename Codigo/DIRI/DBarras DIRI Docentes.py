import pandas as pd
import matplotlib.pyplot as plt

# Cargamos los datos desde el archivo CSV en un DataFrame
df_docentes = pd.read_csv('Datos/DIRI/DIRI Mov. Docente.csv')

# Filtrar el DataFrame para obtener solo los datos con movilidades en "PE" y "PS"
df_movilidad_pe_ps = df_docentes[(df_docentes['PE - Docente Nacional'].notnull()) & (df_docentes['PS - Docente Nacional'].notnull())]

# Ordenar los datos por la columna 'PE - Docente Nacional' de manera descendente para PE
df_pe_nacional = df_movilidad_pe_ps.sort_values(by='PE - Docente Nacional', ascending=False)

# Tomar los tres docentes con más movimientos en PE
top_docentes_pe_nacional = df_pe_nacional.head(3)

# Ordenar los datos por la columna 'PS - Docente Nacional' de manera descendente para PS
df_ps_nacional = df_movilidad_pe_ps.sort_values(by='PS - Docente Nacional', ascending=False)

# Tomar los tres docentes con más movimientos en PS
top_docentes_ps_nacional = df_ps_nacional.head(3)

# Lista de nombres de los docentes con más movimientos en PE - Docente Nacional
nombres_docentes_pe = top_docentes_pe_nacional['PE - Docente Nacional'].tolist()
# Lista de valores de movilidades para los docentes con más movimientos en PE - Docente Nacional
movilidades_docentes_pe = top_docentes_pe_nacional['PE  Periodo movilidad'].tolist()

# Lista de nombres de los docentes con más movimientos en PS - Docente Nacional
nombres_docentes_ps = top_docentes_ps_nacional['PS - Docente Nacional'].tolist()
# Lista de valores de movilidades para los docentes con más movimientos en PS - Docente Nacional
movilidades_docentes_ps = top_docentes_ps_nacional['PS Periodo movilidad'].tolist()

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
