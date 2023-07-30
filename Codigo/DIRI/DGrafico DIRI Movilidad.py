import pandas as pd
import matplotlib.pyplot as plt

# Cargamos los datos desde el archivo CSV en un DataFrame
df_docentes = pd.read_csv('Datos/DIRI/DIRI Mov. Docente.csv')

# Calcular la cantidad de movilidades para cada periodo
movilidades_pe = df_docentes['PE  Periodo movilidad'].sum()
movilidades_ps = df_docentes['PS Periodo movilidad'].sum()

# Etiquetas y datos para el gráfico
periodos = ['PE', 'PS']
movilidades = [movilidades_pe, movilidades_ps]

# Colores para el gráfico
colores = ['#F78F1E', '#1E90FF']

# Crear el gráfico circular
plt.figure(figsize=(8, 8))
plt.pie(movilidades, labels=periodos, colors=colores, autopct='%1.1f%%', startangle=140)

# Agregar título y leyenda
plt.title('Distribución del Número de Movilidades en Periodos PE y PS')
plt.legend(periodos, title='Periodos', loc='upper left', bbox_to_anchor=(0.85, 0.95))

# Calcular y agregar el total de movilidades en el centro del gráfico
total_movilidades = sum(movilidades)
plt.text(0, 0, f'Total de Movilidades:\n{total_movilidades}', ha='center', va='center', fontsize=12)

# Mostrar el gráfico
plt.axis('equal')
plt.show()