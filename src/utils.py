# utils.py

import pandas as pd

def cargar_datos(ruta):
    try:
        datos = pd.read_csv(ruta)
        print("✅ Datos cargados correctamente.")
        return datos
    except Exception as e:
        print("❌ Error al cargar los datos:", e)
        return None
