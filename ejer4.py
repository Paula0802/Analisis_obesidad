import pandas as pd
df = pd.read_csv('Obesity.csv', encoding='latin-')
print(df.dtypes)
print(df.sort_values(by=['Weight'], ascending=[True]))