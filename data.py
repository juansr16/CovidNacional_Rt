
"""

# -- script: data.py : python script for data collection                                                 -- #

"""

# Importar paqueterías
import pandas as pd

# Obtener datos de csv
data = pd.read_csv('files/datos_sinave_fconfirmacion.csv')

## Filtrar resultados positivos
df = data.loc[data['RESULTADO_LAB'] == 1]

## Acomodar por fechas
df = df.sort_values(by=['FECHA_CONFIRMACION'])
df = df.reset_index()

