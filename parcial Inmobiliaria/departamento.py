from inmueble import Inmueble

class Departamento(Inmueble):
    def __init__(self, codigo, propietario, alquiler_base, superficie, expensas, piso):
        super().__init__(codigo, propietario, alquiler_base, superficie)
        self.expensas = float(expensas)
        self.piso = int(piso)

    def calcular_alquiler(self):
        alquiler_final = self.alquiler_base
        if self.piso < 3:
            alquiler_final += 20000
        alquiler_final += self.expensas
        return alquiler_final
