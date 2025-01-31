import pandas as pd
import matplotlib.pyplot as plt

# Cargar los datos del archivo CSV
df = pd.read_csv('Obesity.csv')

# Crear el histograma de Edad por Género
plt.figure(figsize=(10, 6))
plt.hist([df[df['Gender'] == 'Male']['Age'], df[df['Gender'] == 'Female']['Age']],
         bins=20, color=['blue', 'pink'], label=['Male', 'Female'])

# Añadir título y etiquetas
plt.title('Histograma de Edad por Género')
plt.xlabel('Edad')
plt.ylabel('Frecuencia')
plt.grid(True)
plt.legend()

# Guardar la gráfica como archivo de imagen
plt.savefig('histograma_edad_genero.png')
plt.show()

