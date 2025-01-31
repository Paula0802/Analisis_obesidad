import pandas as pd
datos=pd.read_csv('Obesity.csv')
peso_promedio=datos.groupby('Gender')['Weight'].mean()
print(peso_promedio)
