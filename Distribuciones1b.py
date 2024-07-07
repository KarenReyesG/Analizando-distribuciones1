import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Cargar el archivo en CSV donde están los datos fuentes
file_path = 'heart_failure_data_ETL.csv'
data = pd.read_csv(file_path)

# Procedemos a crear gráficos de barras lado a lado
def crear_barras_lado_a_lado(data, columnas, titulo, categorias):
    bar_width = 0.35
    indices = np.arange(len(columnas))
    
    fig, ax = plt.subplots()
    
    for i, columna in enumerate(columnas):
        hombres = data[data['sex'] == 1][columna].sum()
        mujeres = data[data['sex'] == 0][columna].sum()
        
        ax.bar(indices[i] - bar_width/2, hombres, bar_width, label=f'Hombres - {categorias[i]}', align='edge', color='blue')
        ax.bar(indices[i] + bar_width/2, mujeres, bar_width, label=f'Mujeres - {categorias[i]}', align='edge', color='red')
    
    ax.set_xlabel('Categorías')
    ax.set_ylabel('Cantidad')
    ax.set_title(titulo)
    ax.set_xticks(indices)
    ax.set_xticklabels(categorias)
    ax.legend(['Hombres', 'Mujeres'], loc='upper right')
    
    plt.show()

# Definir las columnas y categorías
columnas = ['anaemia', 'diabetes', 'smoking', 'DEATH_EVENT']
categorias = ['Anémicos', 'Diabéticos', 'Fumadores', 'Muertos']

# Gráfico de barras para las categorías
crear_barras_lado_a_lado(data, columnas, 'Histograma agrupado por sexo', categorias)