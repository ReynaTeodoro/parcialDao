# Clase base Inmueble
class Inmueble:
    def __init__(self, codigo, propietario, alquiler_base, superficie):
        self.codigo = codigo
        self.propietario = propietario
        self.alquiler_base = float(alquiler_base)
        self.superficie = int(superficie)
    
    def calcular_alquiler(self):
        # Método que será implementado en las clases derivadas
        pass
