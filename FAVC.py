import pandas as pd
import matplotlib.pyplot as plt

# Cargar los datos del archivo CSV
df = pd.read_csv('Obesity.csv')

# Contar la frecuencia de valores en la columna FAVC
favc_counts = df['FAVC'].value_counts()

# Crear la gráfica de barras
plt.figure(figsize=(10, 6))
favc_counts.plot(kind='bar', color=['green', 'red'])

# Añadir título y etiquetas
plt.title('Frecuencia de Consumo de Alimentos Altos en Calorías')
plt.xlabel('Frecuencia')
plt.ylabel('Cantidad de Personas')
plt.grid(True)

# Guardar la gráfica como archivo de imagen
plt.savefig('grafica_favc.png')

# Mostrar la gráfica
plt.show()