import pandas as pd
df = pd.read_csv('Obesity.csv', encoding='latin-')
print(df.info())
'''
hacer la seleccion de acuerdo a una palabra
'''
df.set_index('Gender',inplace=True)
print("LOS DATOS DE MALE")
print(df.loc['Male'])
'''
si quiero mostrar solo dos datos
'''
print(df.loc['Male','Age'])
'''
Si quiero reproducir filas y 2 columnas
específicas
'''
print("\n*4")
print(df.loc[['Female','Male'],['Age','Weight']])
'''
Ahora si quiero mostrar las filas y columnas por rangos
'''
print("\n*4")
print(df.loc[['Female','Male'], 'Age':'Weight'])

'''
Cuando quiero que solo se muestren los datos por una palabra
'''
print("\n*4")

print(df.loc[df['MTRANS'].str.endswith('Automobile')])