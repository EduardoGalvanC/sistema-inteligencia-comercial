from utils import cargar_datos
from analisis import (
    filtrar_por_fecha,
    productos_mas_vendidos,
    calcular_ingresos_totales,
    grafico_productos_mas_vendidos,
    ingresos_por_producto,
    mostrar_grafico_pastel_ingresos,
    resumen_inteligente,
    predecir_demanda_proxima_semana,
    detectar_productos_en_caida,
    panel_resumen_negocio
)

def mostrar_menu():
    print("\n📋 MENÚ PRINCIPAL")
    print("1. Ver primeras filas")
    print("2. Ver estadísticas generales")
    print("3. Ver información del DataFrame")
    print("4. Filtrar por fecha")
    print("5. Productos más vendidos")
    print("6. Calcular ingresos totales")
    print("7. Ver ingresos totales por producto")
    print("8. Recomendaciones y alertas inteligentes")
    print("9. Predecir demanda para la próxima semana")
    print("10. Ver productos en caída")
    print("11. Ver panel resumen del negocio")
    print("12. Salir")

def main():
    print("📂 Cargando archivo de datos...")
    datos = cargar_datos("data/ejemplo_ventas.csv")
    if datos is None:
        return

    while True:
        mostrar_menu()
        opcion = input("Elige una opción: ")

        if opcion == "1":
            print(datos.head())
        elif opcion == "2":
            print(datos.describe())
        elif opcion == "3":
            print(datos.info())
        elif opcion == "4":
            fecha = input("Introduce una fecha (YYYY-MM-DD): ")
            filtrar_por_fecha(datos, fecha)
        elif opcion == "5":
            productos_mas_vendidos(datos)
            grafico_productos_mas_vendidos(datos)
            mostrar_grafico_pastel_ingresos(datos)
        elif opcion == "6":
            calcular_ingresos_totales(datos)
        elif opcion == "7":
            ingresos_por_producto(datos)
        elif opcion == "8":
            resumen_inteligente(datos)
        elif opcion == "9":
            predecir_demanda_proxima_semana(datos)
        elif opcion == "10":
            detectar_productos_en_caida(datos)
        elif opcion == "11":
            panel_resumen_negocio(datos)
        elif opcion == "12":
            print("👋 Saliendo del programa. ¡Hasta luego!")
            break
        else:
            print("❌ Opción no válida. Intenta de nuevo.")

if __name__ == "__main__":
    main()
