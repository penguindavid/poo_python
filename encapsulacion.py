class Coordenada:

    # metodo constructor
    def __init__(self, x, y):
        self.__X = x 
        self.__Y = y 
    
    # metodos de lectura y escritura e cada atributo
    def __getX(self):
        return self.__X

    def getY(self):
        return self.__Y
    
    def setX(self, x):
        self.__X = x
    
    def setY(self, y):
        self.__Y = y 




    # metodo para mostrar coordenada
    def mostrarCoordenada(self):
        print("(", self.__X, ",", self.__Y, ")")
class Cuadrado:

    # metodo constructor 
    def __init__(self, v1, v2, v3, v4):
        self.__V1 = v1
        self.__V2 = v2
        self.__V3 = v3
        self.__V4 = v4

    # metodos privados para mostrar los verices
    def __mostrarCoordenadaV1(self):
        print("(",self.__V1.getX(),",", self.__V1.getY(), ")")

    def __mostrarCoordenadaV2(self):
        print("(",self.__V2.getX(),",", self.__V2.getY(), ")")

    def __mostrarCoordenadaV3(self):
        print("(",self.__V3.getX(),",", self.__V3.getY(), ")")

    def __mostrarCoordenadaV4(self):
        print("(",self.__V4.getX(),",", self.__V4.getY(), ")")


    # metodo para mostrar los vertices
    def mostrarVertices(self):
        print("El cuadrado esta compuesto por los siguiente vertices")
        self.__mostrarCoordenadaV1()
        self.__mostrarCoordenadaV2()
        self.__mostrarCoordenadaV3()
        self.__mostrarCoordenadaV4()
    
# Metodo principal 
def main():
    # imput
    x1 = int(input("digite el valor de x: "))
    x2 = int(input("digite el valor de y: "))

    c1 = Coordenada(x1 , x2)
    c1.mostrarCoordenada()

    v1 = Coordenada(7, 8)
    v2 = Coordenada(10, 8)
    v3 = Coordenada (7, 5)
    v4 = Coordenada (10, 5)


    cuadrado1 = Cuadrado(v1, v2, v3, v4)
    cuadrado1.mostrarVertices()

# que ocurre si el metodo getX() lo hacemos privado: __getX()?
coordenada = Coordenada (3,4)
print("(", coordenada.__getX(), ",", coordenada._Coordenada__getY(), ")")


if __name__ == "__main__":
    main()