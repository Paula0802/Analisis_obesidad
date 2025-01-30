import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv('Obesity.csv')


plt.figure(figsize=(10, 6))
plt.hist([df[df['Gender'] == 'Male']['Age'], df[df['Gender'] == 'Female']['Age']], 
         bins=20, color=['blue', 'pink'], label=['Male', 'Female'])


plt.title('Histograma de Edad por Género')
plt.xlabel('Edad')
plt.ylabel('Frecuencia')
plt.grid(True)
plt.legend()

plt.savefig('histograma_edad_genero.png')
plt.show()