class Empresa():
    def __init__(self):
        self.sucursales = []
        self.cargarCSV()
    def cargarCSV(self):
        file = open('sucursales.csv','rt')
        for linea in file:
            campos = linea[:-1].split(',')
            tipo = int(campos[0])
            numero = campos[1]
            superficie = int(campos[2])
            facturacion = float(campos[3])

            if(tipo == 1):
                alquileres = int(campos[4])
                sucursal = Hiper(numero,superficie,facturacion,alquileres)
            elif(tipo == 2):
                esmayorista = campos[4]
                sucursal = Super(numero,superficie,facturacion,esmayorista)
            elif(tipo == 3):
                alquiler = int(campos[4])
                sucursal = Mini(numero,superficie,facturacion,alquiler)
            self.sucursales.append(sucursal)
        file.close()
    def sumaGananacias(self):
        ganancia = 0
        for sucur in self.sucursales:
            ganancia += sucur.getResultado()
        return ganancia
    
    def localesNoRentables(self):
        noRentable = 0
        for sucur in self.sucursales:
            if not sucur.esRentable():
                noRentable += 1
        return noRentable
    
    def localMasRentable(self):
        maxIndice =  0
        maxSucursal = None
        for sucur in self.sucursales:
            if sucur.getIndice() > maxIndice:
                maxIndice = sucur.getIndice()
                maxSucursal = sucur
        if maxIndice != 0:
            print(f'La sucursal con el mayor indice de rentabilidad fue la N{maxSucursal.numero} de tipo {maxSucursal.__class__.__name__} con un indice de {maxSucursal.getIndice()}')
        else:
            print("No hubo ninguna sucursal con un indice mayor a 0")
    def __str__(self):
        txt = "####Lista de Sucursales####\n"
        for sucur in self.sucursales:
            txt += str(sucur) + "\n"
        txt += "#########################\n"
        return txt
            
class Sucursal():
    def __init__(self,numero,superficie,facturacion):
        self.numero = numero
        self.superfice = superficie
        self.facturacion = facturacion
    
    def getResultado(self):
        pass
    
    def getIndice(self):
        indice = 0
        resultado = self.getResultado()
        try:
            indice = resultado/self.superfice
            return indice
        except Exception as inst:
            print(f'Error! {inst}')
    
    def esRentable(self):
        pass

    def __str__(self):
        str = f'Sucursal N{self.numero} con una superficie  {self.superfice} y una facturacion {self.facturacion}'
        return str

class Hiper(Sucursal):
    def __init__(self,numero,superficie,facturacion,alquileres):
        super().__init__(numero,superficie,facturacion)
        self.alquileres = alquileres
    
    def __str__(self):
        str = super().__str__()
        str += f' y gano {self.alquileres} en alquileres'
        return str
    
    def getResultado(self):
        ''' Pero en el caso de los locales de hipermercados se
        debe sumar el total ganado en concepto de alquileres,'''
        resultado = self.facturacion + self.alquileres
        return resultado
    
    def esRentable(self):
        indice = self.getIndice()
        if indice > 50:
            return True
        return False
            
    
class Super(Sucursal):
    def __init__(self,numero,superficie,facturacion,esMayorista):
        super().__init__(numero,superficie,facturacion)
        self.esMayorista = bool(int(esMayorista))
    def __str__(self):
        str = super().__str__()
        if self.esMayorista:
            str += f' y es mayorista'
        else:
            str += f' y no es mayorista'
        return str
    
    def esRentable(self):
        indice = self.getIndice()
        if self.esMayorista:
            if indice > 45:
                return True
            else:
                return False
        else:
            if indice > 40:
                return True
            else:
                return False


    def getResultado(self):
        '''El resultado comercial de cada sucursal tipo supermercado es equivalente a la facturación'''
        resultado = self.facturacion
        return resultado

class Mini(Sucursal):
    def __init__(self,numero,superficie,facturacion,alquiler):
        super().__init__(numero,superficie,facturacion)
        self.alquiler = alquiler
    def __str__(self):
        str = super().__str__()
        str += f' y pago {self.alquiler} en alquiler'
        return str
    
    def getResultado(self):
        ''', mientras que en el caso de los locales de modalidad Mini debe restarse el alquiler abonado
        al edificio.'''
        resultado = self.facturacion - self.alquiler
        return resultado

    def esRentable(self):
        indice = self.getIndice()
        if indice > 35:
            return True
        return False
