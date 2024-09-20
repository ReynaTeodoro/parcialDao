from classes import * 
def main():
    empresa = Empresa()
    print(empresa)
    print(f'1)La suma de ganancia del punto 1 fue de ${empresa.sumaGananacias()}')
    print(f'2)La cantidad de locales no rentables fueron: {empresa.localesNoRentables()}')
    print('3) Sucursal mas rentable:')
    empresa.localMasRentable()
if __name__ == "__main__":
    main()
