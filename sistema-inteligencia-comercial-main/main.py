from utils import cargar_datos
from analisis import (
    filtrar_por_fecha,
    productos_mas_vendidos,
    calcular_ingresos_totales,
)

def mostrar_menu():
    print("\n📋 MENÚ PRINCIPAL")
    print("1. Ver primeras filas")
    print("2. Ver estadísticas generales")
    print("3. Ver información del DataFrame")
    print("4. Filtrar por fecha")
    print("5. Productos más vendidos")
    print("6. Calcular ingresos totales")
    print("7. Salir")

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
        elif opcion == "6":
            calcular_ingresos_totales(datos)
        elif opcion == "7":
            print("👋 Saliendo del programa. ¡Hasta luego!")
            break
        else:
            print("❌ Opción no válida. Intenta de nuevo.")

if __name__ == "__main__":
    main()
