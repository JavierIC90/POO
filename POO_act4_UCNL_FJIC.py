# Gestion de inventarios

class producto:
    def __init__(self, nombre, precio, marca, modelo, cantidad):
        self.nombre = nombre
        self.precio = precio
        self.marca = marca
        self.modelo = modelo
        self.cantidad = cantidad

    def mostrar_informacion(self):
        print(f"Producto: {self.nombre}")
        print(f"Precio: ${self.precio}")
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Cantidad en inventario: {self.cantidad}")

    def actualizar_cantidad(self, nueva_cantidad):
        self.cantidad = nueva_cantidad
        print(f"La cantidad de {self.nombre} ha sido actualizada a {self.cantidad}.")


class usodeoficina(producto):
    def __init__(self, nombre, precio, marca, modelo, cantidad, tipo):
        super().__init__(nombre, precio, marca, modelo, cantidad)
        self.tipo = tipo


    def mostrar_informacion(self):
        super().mostrar_informacion()
        print(f"Tipo de producto: {self.tipo}")


class usopersonal(producto):
    def __init__(self, nombre, precio, marca, modelo, cantidad, categoria):
        super().__init__(nombre, precio, marca, modelo, cantidad)
        self.categoria = categoria

    def mostrar_informacion(self):
        super().mostrar_informacion()
        print(f"Categoría de producto: {self.categoria}")


class laptop(usodeoficina):
    def __init__(self, nombre, precio, marca, modelo, cantidad, tipo, procesador, sistema_operativo):
        super().__init__(nombre, precio, marca, modelo, cantidad, tipo)
        self.procesador = procesador
        self.sistema_operativo = sistema_operativo

    def mostrar_informacion(self):
        super().mostrar_informacion()
        print(f"Procesador: {self.procesador}")

class smartphone(usopersonal):
    def __init__(self, nombre, precio, marca, modelo, cantidad, categoria, sistema_operativo):
        super().__init__(nombre, precio, marca, modelo, cantidad, categoria)
        self.sistema_operativo = sistema_operativo

    def mostrar_informacion(self):
        super().mostrar_informacion()
        print(f"Sistema Operativo: {self.sistema_operativo}")

# Ejemplo de uso
laptop_modelo1 = laptop("Laptop HP", 1200, "HP", "Pavilion", 10, "Oficina", "Intel Core i7", "Windows 10")
laptop_modelo1.mostrar_informacion()
laptop_modelo1.actualizar_cantidad(8)
laptop_modelo1.mostrar_informacion()

smartphone_modelo1 = smartphone("Smartphone Samsung", 800, "Samsung", "Galaxy S21", 15, "Personal", "Android")
smartphone_modelo1.mostrar_informacion()       
smartphone_modelo1.actualizar_cantidad(12)
smartphone_modelo1.mostrar_informacion()

laptop_modelo2 = laptop("Laptop Lenovo", 1500, "Serie3", "Lite", 10, "Oficina", "AMD", "Windows 11")
laptop_modelo2.mostrar_informacion()
laptop_modelo2.actualizar_cantidad(8)
laptop_modelo2.mostrar_informacion()