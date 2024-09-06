### Introducción

En este proyecto implementamos algoritmos de optimización para hallar mínimos globales de algunas funciones, algunos están basados en comportamientos de animales en la naturaleza como el *Bat Algorithm* que simula la ecolocalización realizada por los murciélagos. Estos algoritmos son de punto fijo, con la abstracción de en cada iteración tenemos algunos puntos en el dominio de la función, en cada iteración actualizamos la posición de estos puntos, se espera, pero no tiene por qué, que estas posiciones converjan a un mínimo global de la función. La diferencia entre estos algoritmos radica en la forma en que actualizan estos puntos. El reto de estos algoritmos consiste en combinar tanto información global como información local de el espacio de búsqueda.

Un algoritmo que solamente usa información local sobre el espacio de búsqueda es el de *gradient descent*, en el cuál los puntos son actualizados de acuerdo a la dirección opuesta a el gradiente de la función en el punto, usar solamente información local, provoca que los puntos se estanquen en mínimos locales, pero no necesariamente globales.

Para visualizar nuestra implementación, son ploteados los puntos en un *contour* de una función de dos variables en un espacio acotado de búsqueda, además creamos una interfaz para escoger que algoritmo usar, pudiendo usar un algoritmo o dos para ver las diferencias entre ellos.

A continuación explicamos en que consiste cada uno de los algoritmos usados:

#### Particle Swarm Optimization:

En este contexto partícula, ave, punto se refieren a una solución candidate en el espacio de búsqueda. El algoritmo comienza con una población de aves distribuidas uniformemente en el espacio de búsqueda, el movimiento de cada ave está influenciado por su la mejor posición en la que ha estado ( menor valor de la función objetivo ) y la mejor posición de el grupo de aves en general. Esto combina el factor global y el factor local.

En cada iteración la posición de las partículas es aumentado con el vector de velocidad de esta partícula, inicialmente este vector es 0, en cada iteración se recalcula este vector, se le añade a la posición de la partícula y se repite el proceso.

Para calcular la velocidad de la partícula se calculan tres componentes y se añaden, el algoritmo posee tres parámetros constantes que influencian cada una de estas velocidades, *inercia*, *aceleración personal*, *aceleración social*. Cada uno de estos controla que tanto aporta cada una de las tres velocidades a el resultado final:

    - $i * v$
    - $a_p * R(0,1) * (G_p - P)$
    - $a_s * R(0,1) * (G - P)$

Donde $i$ es la inercia, $v$ es la velocidad actual de la partícula, $a_p, a_s$ es la aceleración personal y social respectivamente. $R(0, 1)$ es un número al azar entre $0,1$. $G$ es la mejor posición global, $G_p$ es la mejor posición de la partícula y $P$ es la posición de la partícula.

#### Bat Algorithm

#### Shuffled Frog Leaping Algorithm (*SFLA*)

El Shuffled Frog Leaping Algorithm fue originalmente desarrollado para resolver problemas combinatoriales de optimización. El SFLA es una búsqueda cooperativa poblacional inspirado en meméticas de la naturaleza. El algoritmo contiene elementos de búsqueda local e intercambio de información global. Este consiste en una población virtual interactiva de ranas que es particionado en diferentes "memeplexes". Las ranas virtuales actúan como huéspedes o transportadores de los memes; donde un meme no es más que una unidad cultural de evolución (en nuestro caso, son vectores reales). El algoritmo realiza de forma simultánea e independiente una búsqueda local en cada memeplex (una característica que combina perfectamente con el paralelismo, utilizado en nuestra implementación). La búsqueda local es completada usando un método similar al "particle swarm" que enfatiza en la localidad. Para asegurar la exploración global, la ranas virtuales son periódicamente mezcladas y reorganizadas en nuevos memeplexes, una técnica similar a la mezcla utilizada en algoritmos evolutivos complejos. En adición, para proveer de una oportunidad para la generación aleatoria, ranas aleatorias son creadas y sustituidas en la población.

Dadas estas características del SFLA, y en particular su efectiva combinación de búsqueda local y global, decidimos seleccionarlo para optimizar las funciones de prueba; las cuales, en su mayoría, poseen más de un mínimo local (el SFLA es capaz de escaparlos para encontrar su camino hacia el mínimo global).

Los siguientes resultados fueron obtenidos tras realizar 20 ejecuciones del SFLA sobre las funciones de prueba ([código fuente](../src/notes/notes_sfla.ipynb)). Las datos comprenden: *duración*, *error con respecto al mínimo real* (valor absoluto), *error con respecto al punto óptimo real* (distancia euclidiana).

- **Mishra No. 7**

![](./images/sfla_mishra_7.png)

- **Ripple No. 25**

![](./images/sfla_ripple_25.png)

- **Schaffer No. 1**

![](./images/sfla_schaffer_1.png)

- **Schaffer No. 2**

![](./images/sfla_schaffer_2.png)

**Nota**: Dado que la documentación carece del punto óptimo para **Mishra No. 7** (depende de los parámetros de la función -D, N-), decidimos en este caso computar el punto óptimo promedio, mediana y desviación estándar, respectivamente.

## Algoritmo Genético: Differential Evolution (DE)

Differential Evolution (DE) es un algoritmo de optimización evolutivo, que pertenece a la misma familia de algoritmos que los Algoritmos Genéticos (GA). Se utiliza generalmente para funciones multidimensionales, donde el objetivo es encontrar el mínimo (o máximo) de una función objetivo. DE no utiliza el gradiente del problema que se optimiza, lo que significa que no requiere que el problema de optimización sea diferenciable.

El funcionamiento de este algoritmo procede de la siguiente forma: Comienza generando una población inicial de soluciones candidatas. Estas soluciones son vectores aleatorios generados dentro de los límites especificados para cada variable del problema. Cada individuo en la población representa una posible solución al problema. ***DE*** introduce la variación mediante una operación llamada mutación. Para cada vector de la población, se seleccionan aleatoriamente tres individuos diferentes. Se crea un nuevo vector (mutante) sumando la diferencia entre dos de estos vectores multiplicada por un factor de escalamiento (F) al tercero.

   $Mutante = Individuo_1 + F × (Individuo_2 − Individuo_3)$


   Después de la mutación, DE realiza un cruce entre el vector original y el vector mutante para crear un nuevo vector (trial vector). Se decide, para cada componente del vector, si se toma el valor del vector original o del mutante, basándose en una probabilidad predefinida (CR).

   $Trial Vector_i = { Mutante_i si rand(0,1) ≤ CR Individuo_i si rand(0,1) > CR }$


   Finalmente, se compara el valor de la función objetivo del nuevo vector generado con el del vector original. Si el nuevo vector tiene un valor de función objetivo mejor (menor para un problema de minimización), reemplaza al vector original en la población.

  $Población_{i+1} = { Trial Vector si f(Trial Vector) ≤ f(Individuo) Individuo en otro caso }$

Estos pasos se repiten durante varias iteraciones hasta que se cumple algún criterio de parada, como alcanzar un número máximo de iteraciones o una mejora mínima en la solución.

Los siguientes resultados fueron obtenidos tras realizar 20 ejecuciones del [GA (Differential Evolution)](../src/notes/notes_ga.ipynb) sobre las funciones de prueba. Las datos comprenden: *duración*, *error con respecto al mínimo real* (valor absoluto), *error con respecto al punto óptimo real* (distancia euclidiana).

- **Mishra No. 7**

![](./images/ga_mishra_7.png)

- **Ripple No. 25**

![](./images/ga_ripple_25.png)

- **Schaffer No. 1**

![](./images/ga_schaffer_1.png)

- **Schaffer No. 2**

![](./images/ga_schaffer_2.png)

**Nota**: Dado que la documentación carece del punto óptimo para **Mishra No. 7** (depende de los parámetros de la función -D, N-), decidimos en este caso computar el punto óptimo promedio, mediana y desviación estándar, respectivamente.
