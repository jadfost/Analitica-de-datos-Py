import pandas as pd
import matplotlib.pyplot as plt

# Cargar los datos
df_estudiantes = pd.read_csv('Datos/DIRI/DIRI Mov.estudiantil.csv')

# Calcular la cantidad de estudiantes nacionales e internacionales por convenio
nacionalidad_counts = df_estudiantes.groupby('POBLACION ENTRANTE - NOMBRE DEL CONVENIO')['PE - Estudiantes Nacional'].value_counts().unstack().fillna(0)

# Crear un gráfico circular por cada convenio
for convenio, row in nacionalidad_counts.iterrows():
    fig, ax = plt.subplots()
    wedges, texts, autotexts = ax.pie(row, autopct='%1.1f%%', startangle=90, textprops=dict(color="w"))
    ax.legend(wedges, row.index, title="Nacionalidad", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))
    ax.set_title(f'Distribución de Nacionalidad de Estudiantes en {convenio}')
    
    # Ajustar la etiqueta de cada porción para evitar superposición
    for text in texts:
        text.set_rotation(30)
    
    plt.show()
