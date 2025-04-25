# analisis.py

import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime


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

def mostrar_grafico_pastel_ingresos(datos):
    ingresos_por_producto = datos.groupby('Producto')['Cantidad'].sum() * datos.groupby('Producto')['Precio Unitario'].mean()
    
    plt.figure(figsize=(8, 8))
    plt.pie(ingresos_por_producto, labels=ingresos_por_producto.index, autopct='%1.1f%%', startangle=90)
    plt.title('Distribución de Ingresos por Producto 🥧')
    plt.axis('equal')  # Hace que el pastel sea circular
    plt.tight_layout()
    plt.show()

def resumen_inteligente(datos):
    print("\n🧠 Análisis inteligente del negocio:")

    # Convertimos fechas si no lo están ya
    datos["Fecha"] = pd.to_datetime(datos["Fecha"])

    # Añadir columna de semana
    datos["Semana"] = datos["Fecha"].dt.isocalendar().week

    # Calcular semana actual y anterior
    semana_actual = datos["Semana"].max()
    semana_anterior = semana_actual - 1

    # Filtrar datos por semana
    datos_actual = datos[datos["Semana"] == semana_actual]
    datos_anterior = datos[datos["Semana"] == semana_anterior]

    # ✅ Producto estrella de la semana actual
    if not datos_actual.empty:
        producto_top = datos_actual.groupby("Producto")["Cantidad"].sum().sort_values(ascending=False)
        producto_estrella = producto_top.idxmax()
        cantidad_estrella = producto_top.max()
        print(f"\n🌟 Tu producto estrella esta semana fue: **{producto_estrella}** con {cantidad_estrella} unidades vendidas.")
    else:
        print("\n🌟 No hay datos disponibles para esta semana.")

    # ✅ Comparar ventas totales semana actual vs anterior
    total_actual = datos_actual["Cantidad"].sum()
    total_anterior = datos_anterior["Cantidad"].sum()

    if total_actual < total_anterior:
        print(f"\n⚠️ Alerta: Las ventas bajaron respecto a la semana anterior.")
    elif total_actual > total_anterior:
        print(f"\n✅ ¡Buen trabajo! Las ventas subieron respecto a la semana anterior.")
    else:
        print(f"\nℹ️ Las ventas se mantuvieron estables respecto a la semana anterior.")

    print(f"📉 Semana actual: {total_actual} unidades, Semana anterior: {total_anterior} unidades.")

def predecir_demanda_proxima_semana(datos, top_n=3):
    datos["Fecha"] = pd.to_datetime(datos["Fecha"])
    datos["Semana"] = datos["Fecha"].dt.isocalendar().week

    # Agrupar por semana y producto
    resumen = datos.groupby(["Semana", "Producto"])["Cantidad"].sum().reset_index()

    # Calcular media de ventas semanales por producto
    predicciones = resumen.groupby("Producto")["Cantidad"].mean().sort_values(ascending=False)

    print("\n🔮 Predicción de demanda para la próxima semana (basado en medias):")
    for producto, media in predicciones.head(top_n).items():
        print(f"➡️ Se espera vender aproximadamente {media:.0f} unidades de {producto}")

def detectar_productos_en_caida(datos, umbral_caida=0.3):
    datos["Fecha"] = pd.to_datetime(datos["Fecha"])
    datos["Semana"] = datos["Fecha"].dt.isocalendar().week

    semana_actual = datos["Semana"].max()
    semana_anterior = semana_actual - 1

    ventas_actual = datos[datos["Semana"] == semana_actual].groupby("Producto")["Cantidad"].sum()
    ventas_anterior = datos[datos["Semana"] == semana_anterior].groupby("Producto")["Cantidad"].sum()

    # Solo compararemos productos que estén en ambas semanas
    productos_comunes = ventas_actual.index.intersection(ventas_anterior.index)

    print("\n📉 Productos en caída (disminución > {:.0f}% respecto a la semana anterior):".format(umbral_caida * 100))
    caidas_detectadas = False

    for producto in productos_comunes:
        v_actual = ventas_actual[producto]
        v_anterior = ventas_anterior[producto]

        if v_actual < v_anterior:
            caida_relativa = (v_anterior - v_actual) / v_anterior
            if caida_relativa >= umbral_caida:
                caidas_detectadas = True
                print(f"🔻 {producto}: de {v_anterior} a {v_actual} unidades (-{caida_relativa:.0%})")

    if not caidas_detectadas:
        print("✅ No se detectaron caídas significativas esta semana.")

def panel_resumen_negocio(datos):
    print("\n📋 PANEL RESUMEN DEL NEGOCIO\n" + "-"*35)

    # Ingresos totales
    datos["Ingresos"] = datos["Cantidad"] * datos["Precio Unitario"]
    ingresos_totales = datos["Ingresos"].sum()
    print(f"💰 Ingresos totales: {ingresos_totales:.2f} €")

    # Producto más vendido
    mas_vendido = datos.groupby("Producto")["Cantidad"].sum().idxmax()
    cantidad_vendida = datos.groupby("Producto")["Cantidad"].sum().max()
    print(f"🏆 Producto más vendido: {mas_vendido} ({cantidad_vendida} unidades)")

    # Producto con más ingresos
    producto_top_ingresos = datos.groupby("Producto")["Ingresos"].sum().idxmax()
    ingresos_producto = datos.groupby("Producto")["Ingresos"].sum().max()
    print(f"💸 Producto con más ingresos: {producto_top_ingresos} ({ingresos_producto:.2f} €)")

    # Análisis por semana
    datos["Fecha"] = pd.to_datetime(datos["Fecha"])
    datos["Semana"] = datos["Fecha"].dt.isocalendar().week
    semana_actual = datos["Semana"].max()
    semana_anterior = semana_actual - 1

    ventas_actual = datos[datos["Semana"] == semana_actual]["Cantidad"].sum()
    ventas_anterior = datos[datos["Semana"] == semana_anterior]["Cantidad"].sum()

    print(f"\n📈 Comparativa semanal:")
    print(f"Semana actual (semana {semana_actual}): {ventas_actual} unidades")
    print(f"Semana anterior (semana {semana_anterior}): {ventas_anterior} unidades")

    # Producto estrella semana actual
    ventas_esta_semana = datos[datos["Semana"] == semana_actual]
    producto_estrella = ventas_esta_semana.groupby("Producto")["Cantidad"].sum().idxmax()
    unidades_estrella = ventas_esta_semana.groupby("Producto")["Cantidad"].sum().max()
    print(f"\n🌟 Producto estrella esta semana: {producto_estrella} ({unidades_estrella} unidades)")

    # Alerta si hay bajada
    if ventas_actual < ventas_anterior:
        print(f"⚠️ Alerta: Las ventas bajaron respecto a la semana anterior.")
    else:
        print("✅ Las ventas se mantuvieron o subieron respecto a la semana anterior.")

    # Productos en caída
    print("\n📉 Productos en caída:")
    detectar_productos_en_caida(datos)  # Usamos la función ya creada
