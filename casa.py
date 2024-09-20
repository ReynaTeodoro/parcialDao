from inmueble import Inmueble

# Clase Casa que hereda de Inmueble
class Casa(Inmueble):
    def __init__(self, codigo, propietario, alquiler_base, superficie, dormitorios, tiene_pileta):
        super().__init__(codigo, propietario, alquiler_base, superficie)
        self.dormitorios = int(dormitorios)
        self.tiene_pileta = bool(int(tiene_pileta))  # 1 o 0

    def calcular_alquiler(self):
        alquiler_final = self.alquiler_base + (30000 * self.dormitorios)
        if self.tiene_pileta:
            alquiler_final += 100000
        return alquiler_final
