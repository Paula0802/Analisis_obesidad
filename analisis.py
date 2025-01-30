import pandas as pd
df = pd.read_csv('Obesity.csv', encoding='latin-')
print(df.info())
print(df.head())
print("\n"*4)
#Se muestran los 5 primeros, desde cero hasta el dato 5
print(df.iloc[0:5])
#Renglones salteados
'''
Muestra las filas 0,3,6 y 24
'''
print(df.iloc[[0,3,6,24],])
#COLUMNAS
'''
solo se muestran desde la columna 0 hasta la 2
'''
print(df.iloc[:,0:2])
'''
Encontrar renglones y columnas específicas
'''
print(df.iloc[[0,3,6,24],[0,5,6]])