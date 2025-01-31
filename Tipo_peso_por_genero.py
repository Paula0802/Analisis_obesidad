import pandas as pd
import matplotlib.pyplot as plt

# Cargar el dataset
datos = pd.read_csv('Obesity.csv')

# Agrupar por 'NObeyesdad' y 'Gender', y contar la cantidad de personas
tipo_peso = datos.groupby(['NObeyesdad', 'Gender']).size().unstack()

# Definir el orden de las categorías de peso
orden = [
    'Insufficient_Weight', 'Normal_Weight', 'Overweight_Level_I',
    'Overweight_Level_II', 'Obesity_Type_I', 'Obesity_Type_II', 'Obesity_Type_III'
]

# Reindexar el DataFrame según el orden definido
tipo_peso = tipo_peso.reindex(orden)

# Mostrar el DataFrame