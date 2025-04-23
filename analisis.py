# analisis.py

import pandas as pd
import matplotlib.pyplot as plt


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

def grafico_productos_mas_vendidos(datos, top_n=5):
    ventas = datos.groupby("Producto")["Cantidad"].sum().sort_values(ascending=False).head(top_n)
    
    plt.figure(figsize=(8, 6))
    ventas.plot(kind='bar', color='skyblue')
    plt.title(f"Top {top_n} productos más vendidos")
    plt.xlabel("Producto")
    plt.ylabel("Cantidad Vendida")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def ingresos_por_producto(datos):
    print("\n💰 Ingresos totales por producto:\n")
    datos['Ingresos'] = datos['Cantidad'] * datos['Precio Unitario']
    ingresos = datos.groupby('Producto')['Ingresos'].sum().sort_values(ascending=False)
    print(ingresos.round(2))

    # 📊 Mostrar gráfico
    ingresos.plot(kind='bar', figsize=(10, 6), color='orange')
    plt.title('Ingresos Totales por Producto')
    plt.xlabel('Producto')
    plt.ylabel('Ingresos (€)')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()
