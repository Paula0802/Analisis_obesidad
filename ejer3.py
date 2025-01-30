import pandas as pd
datos= pd.read_csv('Obesity.csv', encoding='latin-1')
print (datos.head())
datos.set_index('Gender', inplace=True)
print(datos.loc[datos['CAEC']=='Sometimes',['MTRANS']])
