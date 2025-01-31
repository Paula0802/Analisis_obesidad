import pandas as pd

# Cargar los datos del archivo CSV
df = pd.read_csv('Obesity.csv')

# Verificar si las columnas 'SCC' y 'smoke' existen en el DataFrame
if 'SCC' not in df.columns or 'SMOKE' not in df.columns:
    raise KeyError("Las columnas 'SCC' y/o 'smoke' no existen en el archivo CSV.")

# Contar la frecuencia de cada tipo de obesidad
obesity_counts = df['Obesity'].value_counts()

# Crear una tabla de datos
obesity_table = pd.DataFrame({
    'Tipo de Obesidad': obesity_counts.index,
    'Frecuencia': obesity_counts.values
})

# Mostrar la tabla de datos
print(obesity_table)

# Exportar la tabla de datos a un archivo CSV
obesity_table.to_csv('frecuencia_obesidad.csv', index=False)

# Filtrar los tipos de obesidad específicos
specific_obesity_types = ['Obesity_Type_I', 'Obesity_Type_III', 'Obesity_Type_II', 'Overweight_Level_I', 'Overweight_Level_II']
filtered_df = df[df['Obesity'].isin(specific_obesity_types)]

# Contar cuántos marcaron "yes" y "no" en la columna SCC
scc_counts = filtered_df['SCC'].value_counts()

# Contar cuántos marcaron "yes" y "no" en la columna smoke
smoke_counts = filtered_df['SMOKE'].value_counts()

# Mostrar los resultados
print("SCC counts:")
print(scc_counts)
print("\nSMOKE counts:")
print(smoke_counts)