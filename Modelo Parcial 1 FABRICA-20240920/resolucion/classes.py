class Maquina:
    def cargar_datos_desde_csv(self):
        file = open('./mantenimientos.csv','rt')
        for linea in file:
            campos = linea[:-1].split(',')
            #print(campos)
            tipo = int(campos[0])
            fecha = campos[1]
            operario = campos[2]
            importe = float(campos[3])
            if (tipo == 1):
                resultado = int(campos[4])
                insumos = float(campos[5])
                mantenimiento = Preventivo(operario,fecha,importe,resultado,insumos)
            else:
                horas_parada = int(campos[4])
                importe_tecnico = float(campos[5])
                mantenimiento = Correctivo(operario,fecha,importe,horas_parada,importe_tecnico)
            self.mantenimientos.append(mantenimiento)
        file.close()
    
    def __str__(self):
        txt = "--- INFORME DE MANTENIMENTOS ---\n"
        for mant in self.mantenimientos:
            txt += str(mant)+"\n"
        txt += "--- ######################## ---"
        return txt
        

    def __init__(self):
        self.mantenimientos = []
        self.cargar_datos_desde_csv()
    
    def suma_gastos(self):
        suma = 0
        for mant in self.mantenimientos:
            suma += mant.get_costo()
        return suma

    def mantenimientos_caros(self):
        mant_caros = [ m for m in self.mantenimientos if m.get_costo() > 10000 ]
        return len(mant_caros)

    def rotura_mas_larga(self):
        mayor_duracion = 0
        operario = None
        fecha = None

        for m in self.mantenimientos:
            if isinstance(m,Correctivo):
                if (m.horas_parada > mayor_duracion):
                    mayor_duracion = m.horas_parada
                    operario = m.operario
                    fecha = m.fecha
        
        if mayor_duracion != 0:
            print(f"El mantenimiento correctivo más largo demandó {mayor_duracion} horas, fué realizado por {operario} en fecha {fecha}")
        else:
            print ("No hubo mantenimientos correctivos con duración mayor a 0")

class Mantenimiento:
    def __init__(self, operario, fecha, importe):
        self.operario = operario
        self.fecha = fecha
        self.importe = importe

    def __str__(self):
        return f"OPERARIO:{self.operario} - FECHA:{self.fecha} - IMPORTE:{self.importe}"

class Preventivo(Mantenimiento):
    def __init__(self, operario, fecha, importe, resultado, insumos):
        super().__init__(operario,fecha,importe)
        self.insumos = insumos
        self.resultado = resultado

    def __str__(self):
        mant_str = super().__str__()
        str = f"<< PREVENTIVO >> {mant_str} -> INSUMOS:{self.insumos} - RESULTADO:{self.resultado}"
        return str
    
    def get_costo(self):
        return self.importe + self.insumos

class Correctivo(Mantenimiento):
    def __init__(self, operario, fecha, importe, horas_parada, importe_tecnico):
        super().__init__(operario,fecha,importe)
        self.horas_parada = horas_parada
        self.importe_tecnico = importe_tecnico

    def __str__(self):
        mant_str = super().__str__()
        str = f"<< CORRECTIVO >> {mant_str} -> HS. PARADA:{self.horas_parada} - IMPORTE TECNICO:{self.importe_tecnico}"
        return str

    def get_costo(self):
        return self.importe + self.importe_tecnico
