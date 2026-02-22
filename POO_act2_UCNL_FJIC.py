# Actividad 2: Programación Orientada a Objetos (POO) Francisco Javier Iracheta Carrion
# POO estudiantes
# atributos: nombre, edad, semestre, promedio
# métodos: aprobado_o_no(), describir()
# constructores: __init__()

class Estudiante:
    def __init__(self, nombre, edad, sexo, semestre, promedio):
        self.nombre = nombre
        self.edad = edad
        self.__sexo = sexo # este atributo es privado ya que no es relevante para la informacion 
        # que se desea consultar sobre el estudiante, solo se utiliza para determinar el mensaje 
        # de aprobado/a o reprobado/a. 
        self.semestre = semestre
        self.promedio = promedio

    def aprobado_o_no(self): 
        # aqui utilice "and" para evaluar no solo el promedio, tambien el sexo del estudiante,
        # al escribir el mensaje de aprobado/a o reprobado/a 
        if self.promedio >= 70 and self.__sexo.lower() == "masculino":
            return f"{self.nombre} está aprobado."
        elif self.promedio >= 70 and self.__sexo.lower() == "femenino":
            return f"{self.nombre} está aprobada."
        elif self.promedio < 70 and self.__sexo.lower() == "masculino":
            return f"{self.nombre} está reprobado."
        # en esta linea solo queda la condicion de reprobada para el caso de ser mujer.
        else:
            return f"{self.nombre} está reprobada."

    def describir(self):
        return f"{self.nombre}\ntiene {self.edad} años\nestudiante de {self.semestre} semestre\npromedio de {self.promedio}"
    
# Crear instancias de estudiantes
Juan = Estudiante("Juan", 20, "masculino", "Segundo", 85)
Josefina = Estudiante("Josefina", 18, "Femenino", "Primer", 65)

# Usar los métodos
print(Juan.describir())
print(Juan.aprobado_o_no())
print(Josefina.describir())
print(Josefina.aprobado_o_no())