import pandas as pd
import matplotlib.pyplot as plt

# Leer el archivo CSV con los datos de OCME
df = pd.read_csv('Datos/OCME/OCME 10-18.csv')  # Reemplaza 'ruta_del_archivo.csv' con la ubicación real del archivo

# Calcular la distribución de propósitos
proposito_counts = df['PROPÓSITO DEL MEDIO UTILIZADO'].value_counts()

# Configurar el gráfico
plt.figure(figsize=(8, 6))
plt.pie(proposito_counts, labels=proposito_counts.index, autopct='%1.1f%%', startangle=140)
plt.title('Distribución de Propósitos de Medios de Divulgación')
plt.show()
