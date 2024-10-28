import requests
import pandas as pd

# URL de la página web que contiene la tabla
url = 'https://www.transfermarkt.es/clube-atletico-mineiro/kader/verein/330/saison_id/2023'  # Reemplaza con la URL real

# Obtener el contenido HTML de la página
response = requests.get(url)
response.raise_for_status()  # Lanza un error si la solicitud no tiene éxito

# Leer la tabla de HTML usando pandas
tables = pd.read_html(response.text)  # Obtiene todas las tablas de la página
tabla = tables[0]  # Selecciona la primera tabla (ajusta si hay más de una)

# Guardar la tabla en un archivo Excel
nombre_archivo = 'tabla_web.xlsx'
tabla.to_excel(nombre_archivo, index=False)

print(f'Tabla guardada en {nombre_archivo}')
