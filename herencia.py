# Clase Persona

class Persona:
    
    # método constructor
    def __init__(self):
        self.__Nombre = ""
        self.__Apellidos = ""
        self.__Edad = 0

    def getNombre(self):
        return self.__Nombre
    
    def setNombre(self, nombre):
        self.__Nombre = nombre

    def getApellidos(self):
        return self.__Apellidos
    
    def setApellidos(self, apellidos):
        self.__Apellidos = apellidos

    def getEdad(self):
        return self.__Edad
    
    def setEdad(self, edad):
        self.__Edad = edad

    # método para mostrar los datos de una persona
    def MostrarPersona(self):
        print("Nombre: " + self.__Nombre)
        print("Apellidos: " + self.__Apellidos)
        print("Edad: " + str(self.__Edad))

class Alumno(Persona):
    def __init__(self):
        self.__Curso = ""
        self.__Asignaturas = ""
    
    def getCurso(self):
        return self.__Curso
    
    def setCurso(self, curso):
        self.__Curso = curso

    def getAsignaturas(self):
        return self.__Asignaturas
    
    def setAsignaturas(self, asignaturas):
        self.__Asignaturas = asignaturas

    def mostrarAlumno(self):
        print("Alumno")
        print("\tNombre: ", self.getNombre())
        print("\tApellidos: ", self.getApellidos())
        print("\tEdad: ", self.getEdad())
        print("\tCurso: ", self.__Curso)
        print("\tMatrículas: ", self.__Asignaturas)


class Profesor(Persona):
    def __init__(self):
        super().__init__()
        self.__Antiguedad = ""  
        self.__Tutorias = []    
        self.__Telefono = ""    
    
    def getAntiguedad(self):
        return self.__Antiguedad
    
    def setAntiguedad(self, antiguedad):
        self.__Antiguedad = antiguedad

    
    def getTutorias(self):
        return self.__Tutorias
    
    def setTutorias(self, tutorias):
        self.__Tutorias = tutorias

    
    def getTelefono(self):
        return self.__Telefono

    def setTelefono(self, telefono):
        self.__Telefono = telefono 

    
    def mostrarProfesor(self):
        print("Profesor")
        print("\tNombre:", self.getNombre())
        print("\tApellidos:", self.getApellidos())
        print("\tEdad:", self.getEdad())
        print("\tAntigüedad:", self.__Antiguedad)
        print("\tTutorías:", ", ".join(self.__Tutorias))
        print("\tTeléfono:", self.__Telefono)


def main():
    profesor = Profesor()
    profesor.setNombre("Nestor")
    profesor.setApellidos("paez sarmiento")
    profesor.setEdad(25)
    profesor.setAntiguedad("10 años")
    profesor.setTutorias(["Lunes 2:00-4:00 PM", "Miércoles 3:00-5:00 PM"])
    profesor.setTelefono("311-123-4567")

    profesor.mostrarProfesor()  

if __name__ == "__main__":
    main()



# metodo principal
def main():
    alumno = Alumno()  
    alumno.setNombre("David santigo")
    alumno.setApellidos("Macias Maldonado")
    alumno.setEdad(15)
    alumno.setCurso("Bachillerato")
    alumno.setAsignaturas(["Matemáticas", "Tecnología", "Inglés"])
    alumno.mostrarAlumno()


if __name__ == "__main__":
    main()

