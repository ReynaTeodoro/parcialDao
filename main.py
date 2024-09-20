from inmobiliaria import Inmobiliaria
import csv
def main():
    inmobiliaria = Inmobiliaria()
    inmobiliaria.cargar_inmuebles('inmuebles.csv')  # Cargar el archivo CSV
    
    # Ejecutar los métodos requeridos
    print(f"Suma de alquileres: {inmobiliaria.suma_de_alquileres()}")
    print(f"Cantidad de casas premium: {inmobiliaria.cantidad_de_casas_premium()}")
    print(f"Propietario del alquiler más bajo: {inmobiliaria.propietario_alquiler_mas_bajo()}")


if __name__ == "__main__":
    main()
