# poo_python
introduccion a la POO en python 

- el paradigma de POO esta basado en una abstraccion del mundo real que nos va a permitir desarrollar programas de forma mas cercana a como vemos el mundo, pensando en objetos que tenemos delante y en acciones que podemos hacer con ellos.

## clase

- una clase es un tipo de dato cuyas variables se llaman objetos o instancias 
- la clase es la definicion del concepto del mundo real y los objetos o instancias son el propio objeto del mundo real.
- las clases estan compuestas por 2 elementos: atributos y metodos. 

### atributos 
-informacion que almacena la clase

### metodos
- operaciones que pueden realizar las clases 

## definicion de una clase en python 
```python
 class Nombreclase:

    def__init__(self,variable1, variable2) :
        self.atributo1= valor1
        self.atributo2= valor2

    def nombreMetodo(self)
        bloque de codigo 
```
### componentes

```class```: palabra reservada en python para definir una clase.

```NombreClase```: nombre de la clase que quieres crear

```def```: palabra reservada en python que se utiliza para definir tanto el constructor de la clase(metodo que se ejecuta la primera vez que usas una clase) como los diferentes metodos que tiene. 

```__init__```: palabra reservada en python para definir el metodo constructor de la clase. Es lo primero que se ejecuta cuando creas un objeto de una clase.

```(self, variableX)```: parametro del constrctor de la clase. El parametro self es obligatorio y despues puedes tener tantos parametros como quieras. la forma de añadir parametros es la misma que en las funciones 

```self.atributoX```:  forma de utilizacion  y acceso a los atributos de la clase.

```nombreMetodo```:nombre del metodo de la clase.

```(self)```: parametro del metodo. el parametro selff es obligatorio y despues puedes tener tantos parametros como quieras. la forma de añadir parametros es la misma que en las funciones.

```bloqueCodigo```: instrucciones que ejecutara el metodo.

- cuando defines una clase debes tener en cuenta los siguientes puntos:
    -puedes definir tantos atributos como necesites
    -puedes definir tantos metodos como necesites 
    -puedes definir tantos parametros en el constructor y en los  metodos como necesite.





