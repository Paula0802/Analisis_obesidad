import pandas as pd

# Cargar los datos del archivo CSV
df = pd.read_csv('Obesity.csv')

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