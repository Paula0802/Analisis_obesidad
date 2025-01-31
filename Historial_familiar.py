import pandas as pd
datos=pd.read_csv('Obesity.csv')

import matplotlib.pyplot as plt

conteo_historial_genero = datos.groupby(['family_history_with_overweight', 'Gender']).size().unstack()
conteo_historial_genero.plot(kind='bar', color=['pink', 'skyblue'], figsize=(8,6), edgecolor='black')

plt.title('Historial Familiar de Sobrepeso según el Género')
plt.xlabel('¿Tiene historial familiar de sobrepeso?')
plt.ylabel('Cantidad de personas')
plt.xticks(rotation=0)
plt.legend(title='Género')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()
