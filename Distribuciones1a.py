import pandas as pd
import matplotlib.pyplot as plt

# Carga del dataset:
file_path = 'heart_failure_data_ETL.csv'
data = pd.read_csv(file_path)

# Extraer la columna de edades
edades = data['age']

# Crear el histograma 
plt.figure(figsize=(10, 6))
plt.hist(edades, bins=20, edgecolor='darkblue')

# Añadir título y etiquetas
plt.title('Distribución de Edades')
plt.xlabel('Edades')
plt.ylabel('Frecuencia')

# Mostrar la gráfica
plt.show()