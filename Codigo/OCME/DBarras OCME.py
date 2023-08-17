import pandas as pd
import matplotlib.pyplot as plt

# Leer el archivo CSV con los datos de OCME
df = pd.read_csv('Datos/OCME/OCME 10-18.csv')  # Reemplaza 'ruta_del_archivo.csv' con la ubicación real del archivo

# Convertir la columna a números
df['NÚMERO APROX. DE PERSONAS INFORMADAS'] = pd.to_numeric(df['NÚMERO APROX. DE PERSONAS INFORMADAS'], errors='coerce')

# Filtrar las filas con valores numéricos en la columna
df = df.dropna(subset=['NÚMERO APROX. DE PERSONAS INFORMADAS'])

# Agrupar datos por año y sumar el número de personas informadas
informados_por_año = df.groupby('AÑO/PERIODO')['NÚMERO APROX. DE PERSONAS INFORMADAS'].sum()

# Configurar el gráfico
plt.figure(figsize=(10, 6))
informados_por_año.plot(kind='bar')
plt.xlabel('Año')
plt.ylabel('Número de Personas Informadas')
plt.title('Número de Personas Informadas por Año')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
