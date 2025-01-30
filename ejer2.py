'''
Exportar los archivos csv para 
exportar los datos
'''
import pandas as pd
datos = pd.read_csv('Obesity.csv', encoding='latin-')
df= pd.DataFrame(datos)
print(df.info())
df.reset_index().to_csv('DatosExportadosObesity.csv', header=True, index=False)
datos.set_index('Gender',inplace=True)
df=datos.loc['Male']
df.reset_index().to_csv('MaleDatosObesity.csv', header=True, index=False)
