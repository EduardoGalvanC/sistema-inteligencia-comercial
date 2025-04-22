# analisis.py

import pandas as pd

def mostrar_info_basica(datos):
    print("\n📌 Primeras filas:")
    print(datos.head())

def mostrar_estadisticas(datos):
    print("\n📊 Estadísticas generales:")
    print(datos.describe())

def mostrar_info_detallada(datos):
    print("\n🧠 Información del DataFrame:")
    print(datos.info())

def filtrar_por_fecha(datos, fecha):
    filtrado = datos[datos["Fecha"] == fecha]
    if filtrado.empty:
        print("⚠️ No se encontraron datos para esa fecha.")
    else:
        print(f"\n📅 Datos para la fecha {fecha}:")
        print(filtrado)
    return filtrado

def productos_mas_vendidos(datos, top_n=5):
    ventas = datos.groupby("Producto")["Cantidad"].sum().sort_values(ascending=False)
    print(f"\n🏆 Productos más vendidos (Top {top_n}):")
    print(ventas.head(top_n))

def calcular_ingresos_totales(datos):
    datos["Ingresos"] = datos["Cantidad"] * datos["Precio Unitario"]
    ingresos_totales = datos["Ingresos"].sum()
    print(f"\n💰 Ingresos totales: {ingresos_totales:.2f} €")
    return ingresos_totales