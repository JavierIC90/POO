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
Pepe = Estudiante("Pepe", 40, "femenino", "Tercer", 100)

class Profesor(Estudiante):
Javier = Profesor("Javier", 35, "masculino", "Cuarto", "N/A")

class Administrativo(Estudiante):
Maria = Administrativo("Maria", 30, "femenino", "N/A", "N/A")

class PersonalLimpieza(Estudiante):
Pedro = PersonalLimpieza("Pedro", 45, "masculino", "N/A", "N/A")

class Prefecto(Estudiante):
Luis = Prefecto("Luis", 50, "masculino", "Tercero", "N/A")

