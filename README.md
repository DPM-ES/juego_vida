# El juego de la vida
Desarrollo del juego ***El juego de la Vida***

El ***Juego de la vida*** es un autómata celular diseñado por el matemático británico John Horton Conway en 1970. Es un juego de cero jugadores, en el que su evolución es determinada por un estado inicial, sin requerir intervención adicional. Se considera un sistema Turing completo que puede simular cualquier otra Máquina de Turing.

Fuente: [Wikipedia](https://es.wikipedia.org/wiki/Juego_de_la_vida)

___
#### Requisitos
Neceista las librerías Numpy y Pygame
~~~
pip install numpy pygame
~~~
___

## El juego de la vida
~~~
Juego_Vida_v1.py
~~~

En el juego de la vida existen 2 reglas:
- Regla 1: Si una célula está viva y tiene dos o tres vecinas vivas, sobrevive.
- Regla 2: Si una célula está muerta y tiene tres vecinas vivas, nace.
- Regla 3: En caso contrario muere. Del mismo modo que una célula muerta, permanece muerta.

En cada tiempo, se comprueban los vecinos y si se cumple alguna de las reglas, se aplicará su efecto, y al final del cálculo de toda la matriz de manera simultánea, se dibujará el nuevo estado de la misma. Así en cada tiempo de reloj.

~~~
Juego_Vida_v2.py
~~~

La versión 2 es igual que la 1, sin embargo, he hecho el código más legible mediante funciones. Respecto al juego, he añadido márgenes al universo y he añadido los cuadros de información para saber la velocidad el juego, el número de células vivas y el número de tiempos pasados desde el inicio.

### Controles

- Barra espaciadora: Detiene o activa el reloj
- Clic Izq: Revive la célula apuntada
- Clic Der: Mata la célula apuntada
- Tecla e: Mata todas las células
- Tecla f: Revive todas las células (tened en cuenta que si se activa el tiempo así, al siguiente paso estarán todas muertas)
- Tecla q: Cierra el juego
- Tecla +: Aumenta la velocidad (hay 5 tiempos)
- Tecla -: Rebaja la velocidad (hay 5 tiempos)

___

## El juego de la vida color
~~~
Juego_Vida_v1_color.py
~~~

Sigue la misma lógica que el juego base, sin embargo la matriz tiene una dimensión adicional, lo que se traduce en que existen tres capas independientes, una para el rojo, otra para el verde y una tercera para el azul. Son independientes, una célula roja no interactua con una verde, sin embargo, a la hora de representar, solo se ve una matriz bidimensional, por tanto, si una célula tiene solo el rojo activado, se verá ese color, pero si tiene el rojo y el verde se verá el amarillo (que es la composición de ambos colores). Funciona de manera similar a una pantalla.

### Controles

- Barra espaciadora: Detiene o activa el reloj
- Clic Izq: Revive la célula apuntada (sólo del color activo)
- Clic Der: Mata la célula apuntada (quita todos los colores)
- Tecla e: Mata todas las células
- Tecla f: Revive todas las células (tened en cuenta que si se activa el tiempo así, al siguiente paso estarán todas muertas)
- Tecla q: Cierra el juego
- Tecla +: Aumenta la velocidad (hay 5 tiempos)
- Tecla -: Rebaja la velocidad (hay 5 tiempos)
- Tecla 1: Activa el color rojo
- Tecla 2: Activa el color verde
- Tecla 3: Activa el color azul
- Tecla 4: Activa el color blanco (rojo, verde y azul a la vez)
