import pandas as pd
import matplotlib.pyplot as plt

# Cargar los datos del archivo CSV
datos = pd.read_csv('Obesity.csv')

# Contar la frecuencia de fumadores
conteo_fumadores = datos['SMOKE'].value_counts()
print(conteo_fumadores)

# Crear el gráfico de barras
plt.figure(figsize=(8, 6))  # Tamaño del gráfico
conteo_fumadores.plot(kind='bar', color=['skyblue', 'red'])

# Características del gráfico
plt.title('Fumas?')
plt.xlabel('')
plt.xticks(rotation=0)
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Guardar la gráfica como archivo de imagen
plt.savefig('grafica_fumadores.png')

# Mostrar la gráfica
plt.show()