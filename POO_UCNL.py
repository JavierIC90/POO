class Empleado:  # Clase base para empleados
    def __init__(self, nombre, sueldo): 
        self.nombre = nombre # atributo público
        self.__sueldo = sueldo # encapsulamiento

    def calcular_pago(self):
        return self.__sueldo # 

class EmpleadoPorHoras(Empleado): # herencia
    def __init__(self, nombre, horas, pago_hora):
        super().__init__(nombre, 0)
        self.horas = horas # objeto 
        self.pago_hora = pago_hora

    def calcular_pago(self): 
        return self.horas * self.pago_hora 

class EmpleadoFijo(Empleado):
    pass
# 
empleados = [ # polimorfismo
    EmpleadoPorHoras("Ana", 40, 100),
    EmpleadoFijo("Luis", 15000)
]

for e in empleados:
    print(f"{e.nombre} cobra {e.calcular_pago()}")
