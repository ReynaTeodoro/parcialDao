from departamento import Departamento
from casa import Casa
import csv
class Inmobiliaria:
    def __init__(self):
        self.inmuebles = []

    def cargar_inmuebles(self, archivo_csv):
        with open(archivo_csv, newline='') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                tipo = int(row[0])
                codigo = int(row[1])
                propietario = row[2]
                alquiler_base = float(row[3])
                superficie = int(row[4])

                if tipo == 1:  # Casa
                    dormitorios = int(row[5])
                    tiene_pileta = int(row[6])
                    inmueble = Casa(codigo, propietario, alquiler_base, superficie, dormitorios, tiene_pileta)
                elif tipo == 2:  # Departamento
                    expensas = float(row[5])
                    piso = int(row[6])
                    inmueble = Departamento(codigo, propietario, alquiler_base, superficie, expensas, piso)

                self.inmuebles.append(inmueble)

    def suma_de_alquileres(self):
        total = sum(inmueble.calcular_alquiler() for inmueble in self.inmuebles)
        return total

    def cantidad_de_casas_premium(self):
        premium_casas = [casa for casa in self.inmuebles if isinstance(casa, Casa) and 
                         casa.superficie > 150 and casa.dormitorios > 2 and casa.tiene_pileta]
        return len(premium_casas)

    def propietario_alquiler_mas_bajo(self):
        alquiler_minimo = min(self.inmuebles, key=lambda inmueble: inmueble.calcular_alquiler())
        return alquiler_minimo.propietario
