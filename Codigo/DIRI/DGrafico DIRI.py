import pandas as pd
import matplotlib.pyplot as plt

# Cargamos los datos desde el archivo CSV en un DataFrame
df_docentes = pd.read_csv('Datos/DIRI/DIRI Mov. Docente.csv')

# Encontrar el docente con más movilidad en general
df_docentes['Total Movilidad'] = df_docentes['PE - Docente Nacional'].notnull().astype(int) + df_docentes['PE - Docente Internacional'].notnull().astype(int) + df_docentes['PS - Docente Nacional'].notnull().astype(int) + df_docentes['PS - Docente Internacional'].notnull().astype(int)
docente_mas_movilidad = df_docentes.loc[df_docentes['Total Movilidad'].idxmax()]

# Crear una lista con los nombres de los docentes y otra lista con los valores de movilidad
nombres_docentes = ['PE - Docente Nacional', 'PE - Docente Internacional', 'PS - Docente Nacional', 'PS - Docente Internacional']
movilidades = [str(docente_mas_movilidad[nombre]).count(',') + 1 for nombre in nombres_docentes]

# Etiquetas para mostrar las poblaciones o universidades
etiquetas = ['Docente Nacional PE', 'Docente Internacional PE', 'Docente Nacional PS', 'Docente Internacional PS']

# Colores para el gráfico
colores = ['#F78F1E', '#EA4335', '#4285F4', '#34A853']

# Crear el gráfico circular con estilo
plt.figure(figsize=(8, 8))
plt.pie(movilidades, labels=None, autopct='%1.1f%%', startangle=140, colors=colores, wedgeprops=dict(width=0.3))

# Agregar etiquetas a las porciones del gráfico y la leyenda
plt.gca().set_aspect("equal")
plt.gca().legend(etiquetas, title="Pertenece a:", bbox_to_anchor=(0.85, 0.9))
plt.title("Docente con más movilidad")

# Mostrar el nombre del docente con más movilidad en el centro del gráfico
docente_nombre = [docente_mas_movilidad[nombre] for nombre in nombres_docentes if pd.notna(docente_mas_movilidad[nombre])]
docente_nombre = ' '.join(docente_nombre)
plt.text(0, 0, docente_nombre, ha='center', va='center', fontsize=14, fontweight='bold')

plt.show()
