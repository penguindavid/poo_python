# Clase base para un estudiante
class Estudiante:
    def __init__(self, nombre, carrera):
        self.nombre = nombre
        self.carrera = carrera

    def estudiar(self):
        return f"{self.nombre} está estudiando {self.carrera}."

# Clase base para un atleta
class Atleta:
    def __init__(self, deporte):
        self.deporte = deporte

    def entrenar(self):
        return f"Está entrenando para el deporte: {self.deporte}."

# Clase derivada que combina ambos roles
class EstudianteAtleta(Estudiante, Atleta):
    def __init__(self, nombre, carrera, deporte):
        Estudiante.__init__(self, nombre, carrera)
        Atleta.__init__(self, deporte)

    def mostrar_informacion(self):
        return (f"Estudiante: {self.nombre}, Carrera: {self.carrera}, Deporte: {self.deporte}.\n"
                f"{self.estudiar()}\n"
                f"{self.entrenar()}")

# Crear una instancia de EstudianteAtleta
persona = EstudianteAtleta("Ana", "Ingeniería", "Natación")

# Mostrar la información
print(persona.mostrar_informacion())


