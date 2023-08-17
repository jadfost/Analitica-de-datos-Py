import pandas as pd
import matplotlib.pyplot as plt

# Leer el archivo CSV con los datos de OCME
df = pd.read_csv('Datos/OCME/OCME 10-18.csv')  # Reemplaza 'ruta_del_archivo.csv' con la ubicación real del archivo

# Agrupar categorías menos relevantes bajo una categoría "Otros"
top_categories = 5  # Número de categorías más importantes a mostrar
top_propositos = df['PROPÓSITO DEL MEDIO UTILIZADO'].value_counts().head(top_categories)
other_propositos = df['PROPÓSITO DEL MEDIO UTILIZADO'].value_counts().tail(len(df) - top_categories).sum()

# Crear un DataFrame para la visualización
propositos_counts = pd.DataFrame({'Propósito': top_propositos.index, 'Cantidad': top_propositos.values})
propositos_counts.loc[len(propositos_counts)] = ['Otros', other_propositos]  # Agregar la categoría "Otros"

# Configurar el gráfico circular
plt.figure(figsize=(8, 8))
colors = plt.cm.Set3.colors
plt.pie(propositos_counts['Cantidad'], labels=propositos_counts['Propósito'], colors=colors, autopct='%1.1f%%', startangle=140, pctdistance=0.85)
plt.title('Distribución de Propósitos del Medio Utilizado')
plt.gca().add_artist(plt.Circle((0,0),0.70,fc='white'))
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.tight_layout()
plt.show()
