### Introducción

En este proyecto implementamos algoritmos de optimización para hallar mínimos globales de algunas funciones, algunos están basados en comportamientos de animales en la naturaleza como el *Bat Algorithm* que simula la eco-localización realizada por los murciélagos. Estos algoritmos son de punto fijo, con la abstracción de en cada iteración tenemos algunos puntos en el dominio de la función, en cada iteración actualizamos la posición de estos puntos, se espera, pero no tiene por qué, que estas posiciones converjan a un mínimo global de la función. La diferencia entre estos algoritmos radica en la forma en que actualizan estos puntos. El reto de estos algoritmos consiste en combinar tanto información global como información local de el espacio de búsqueda.

Un algoritmo que solamente usa información local sobre el espacio de búsqueda es el de *gradient descent*, en el cuál los puntos son actualizados de acuerdo a la dirección opuesta a el gradiente de la función en el punto, usar solamente información local, provoca que los puntos se estanquen en mínimos locales, pero no necesariamente globales.

Para visualizar nuestra implementación, son ploteados los puntos en un *contour* de una función de dos variables en un espacio acotado de búsqueda, además creamos una interfaz para escoger que algoritmo usar, pudiendo usar un algoritmo o dos para ver las diferencias entre ellos.

A continuación explicamos en que consiste cada uno de los algoritmos usados:

#### Particle Swarm Optimization:

En este contexto partícula, ave, punto se refieren a una solución candidate en el espacio de búsqueda. El algoritmo comienza con una población de aves distribuidas uniformemente en el espacio de búsqueda, el movimiento de cada ave está influenciado por su la mejor posición en la que ha estado ( menor valor de la función objetivo ) y la mejor posición de el grupo de aves en general. Esto combina el factor global y el factor local.

En cada iteración la posición de las partículas es aumentado con el vector de velocidad de esta partícula, inicialmente este vector es 0, en cada iteración se recalcula este vector, se le añade a la posición de la partícula y se repite el proceso.

Para calcular la velocidad de la partícula se calculan tres componentes y se añaden, el algoritmo posee tres parámetros constantes que influencian cada una de estas velocidades, *inercia*, *aceleración personal*, *aceleración social*. Cada uno de estos controla que tanto aporta cada una de las tres velocidades: $i * v$, $a_p * R(0,1) * (G_p - P)$, $a_s * R(0,1) * (G - P)$ a el resultado final.

Donde $i$ es la inercia, $v$ es la velocidad actual de la partícula, $a_p, a_s$ es la aceleración personal y social respectivamente. $R(0, 1)$ es un número al azar entre $0,1$. $G$ es la mejor posición global, $G_p$ es la mejor posición de la partícula y $P$ es la posición de la partícula.

A continuación algunas estadísticas con respecto a la ejecución de este algoritmo con algunas de las funciones :

Los siguientes resultados fueron obtenidos tras realizar 20 ejecuciones del Particle Swarm Optimization sobre las funciones de prueba ([código fuente](../src/notes/notes_pso.ipynb)). Las datos comprenden: *duración*, *error con respecto al mínimo real* (valor absoluto), *error con respecto al punto óptimo real* (distancia euclidiana).

Podemos ver como los resultados son sensitivos a la semilla inicial utilizada en el caso de la función Ripple No. 25:

![](./images/pso-ripple1.png)
![](./images/pso-ripple2.png)

En el caso de la función Schaffer No 1, observamos estabilidad con respecto a obtener el mínimo, sin embargo la duración promedio requerida varía. Lo que es justificado por la aleatoriedad de la semilla inicial

#### Shuffled Frog Leaping Algorithm (*SFLA*)

El Shuffled Frog Leaping Algorithm fue originalmente desarrollado para resolver problemas combinatoriales de optimización. El SFLA es una búsqueda cooperativa poblacional inspirado en meméticas de la naturaleza. El algoritmo contiene elementos de búsqueda local e intercambio de información global. Este consiste en una población virtual interactiva de ranas que es particionado en diferentes "memeplexes". Las ranas virtuales actúan como huéspedes o transportadores de los memes; donde un meme no es más que una unidad cultural de evolución (en nuestro caso, son vectores reales). El algoritmo realiza de forma simultánea e independiente una búsqueda local en cada memeplex (una característica que combina perfectamente con el paralelismo, utilizado en nuestra implementación). La búsqueda local es completada usando un método similar al "particle swarm" que enfatiza en la localidad. Para asegurar la exploración global, la ranas virtuales son periódicamente mezcladas y reorganizadas en nuevos memeplexes, una técnica similar a la mezcla utilizada en algoritmos evolutivos complejos. En adición, para proveer de una oportunidad para la generación aleatoria, ranas aleatorias son creadas y sustituidas en la población.

Dadas estas características del SFLA, y en particular su efectiva combinación de búsqueda local y global, decidimos seleccionarlo para optimizar las funciones de prueba; las cuales, en su mayoría, poseen más de un mínimo local (el SFLA es capaz de escaparlos para encontrar su camino hacia el mínimo global).

Los siguientes resultados fueron obtenidos tras realizar 100 ejecuciones del SFLA sobre las funciones de prueba ([código fuente](../src/notes/notes_pso.ipynb)). Las datos comprenden: *duración*, *error con respecto al mínimo real* (valor absoluto), *error con respecto al punto óptimo real* (distancia euclidiana).

- **Mishra No. 7**

![](./images/sfla_mishra_7.png)

- **Ripple No. 25**

![](./images/sfla_ripple_25.png)

- **Schaffer No. 1**

![](./images/sfla_schaffer_1.png)

- **Schaffer No. 2**

![](./images/sfla_schaffer_2.png)

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

El algoritmo de Simulated Annealing es una técnica de optimización inspirada en el proceso de enfriamiento de metales fundidos. El cual funciona de la siguiente manera.

## Simulated Annealing:

### Funcionamiento del Algoritmo

1. **Inicialización**: El algoritmo comienza con una solución inicial aleatoria dentro de los límites definidos.

2. **Iteraciones**: Se realiza un número máximo de iteraciones, en cada una se genera una nueva solución cercana a la actual.

3. **Evaluación**: La función objetivo se calcula para ambas soluciones (actual y nueva).

4. **Aceptación**: Si la nueva solución es mejor o tiene una probabilidad de ser aceptada (determinada por la temperatura), se adopta como nueva solución.

5. **Enfriamiento**: La temperatura disminuye gradualmente a lo largo de las iteraciones.

6. **Conclusión**: El algoritmo termina cuando la temperatura alcanza un valor mínimo o se supera el número máximo de iteraciones.

Trabajamos con la función **Schaffer No. 1** y corrimos 20 veces el algoritmo obteniendo los siguientes resultados.

### Resultados de las 20 ejecuciones:
```
Ejecución 1:
Duración: 0.0189 segundos
Error absoluto promedio respecto al mínimo real: 0.425197
Distancia euclidiana promedio respecto al punto óptimo real: 5.619342
Diferencia estándar de la duración: 0.186079
Punto óptimo encontrado: [1.1368224534254008, 3.589823835851483] en 0.08382150411093797

Ejecución 2:
Duración: 0.0200 segundos
Error absoluto promedio respecto al mínimo real: 0.430092
Distancia euclidiana promedio respecto al punto óptimo real: 4.436518
Diferencia estándar de la duración: 0.255969
Punto óptimo encontrado: [-0.9866316854967326, -0.8947822967086092] en 0.0016017895036985474

Ejecución 3:
Duración: 0.0196 segundos
Error absoluto promedio respecto al mínimo real: 0.485535
Distancia euclidiana promedio respecto al punto óptimo real: 8.764836
Diferencia estándar de la duración: 0.056678
Punto óptimo encontrado: [-4.855332909253431, 5.1746864579869] en 0.35870738098699984

Ejecución 4:
Duración: 0.0193 segundos
Error absoluto promedio respecto al mínimo real: 0.479625
Distancia euclidiana promedio respecto al punto óptimo real: 7.165770
Diferencia estándar de la duración: 0.104972
Punto óptimo encontrado: [-3.7054105440003666, -4.337000652170758] en 0.2631649389426926

Ejecución 5:
Duración: 0.0194 segundos
Error absoluto promedio respecto al mínimo real: 0.498885
Distancia euclidiana promedio respecto al punto óptimo real: 11.467669
Diferencia estándar de la duración: 0.023224
Punto óptimo encontrado: [6.197976092428567, 6.747486911855162] en 0.4387209330324816

Ejecución 6:
Duración: 0.0193 segundos
Error absoluto promedio respecto al mínimo real: 0.440935
Distancia euclidiana promedio respecto al punto óptimo real: 6.801864
Diferencia estándar de la duración: 0.133201
Punto óptimo encontrado: [4.737969792424383, -2.0195189270246656] en 0.2076971909123832

Ejecución 7:
Duración: 0.0200 segundos
Error absoluto promedio respecto al mínimo real: 0.413074
Distancia euclidiana promedio respecto al punto óptimo real: 4.743940
Diferencia estándar de la duración: 0.241217
Punto óptimo encontrado: [-2.1579382173071364, 0.1777609891762874] en 0.010872651154847424

Ejecución 8:
Duración: 0.0173 segundos
Error absoluto promedio respecto al mínimo real: 0.449892
Distancia euclidiana promedio respecto al punto óptimo real: 7.556039
Diferencia estándar de la duración: 0.103038
Punto óptimo encontrado: [4.479399508312773, -3.4476670171880945] en 0.26013888406960417

Ejecución 9:
Duración: 0.0172 segundos
Error absoluto promedio respecto al mínimo real: 0.408343
Distancia euclidiana promedio respecto al punto óptimo real: 4.295763
Diferencia estándar de la duración: 0.261807
Punto óptimo encontrado: [1.5763245271440545, -0.10608221257438] en 0.00587512482989172

Ejecución 10:
Duración: 0.0171 segundos
Error absoluto promedio respecto al mínimo real: 0.490583
Distancia euclidiana promedio respecto al punto óptimo real: 9.750970
Diferencia estándar de la duración: 0.037718
Punto óptimo encontrado: [-7.457797967982029, 3.4084534087356717] en 0.4096072042755916

Ejecución 11:
Duración: 0.0171 segundos
Error absoluto promedio respecto al mínimo real: 0.492327
Distancia euclidiana promedio respecto al punto óptimo real: 8.214255
Diferencia estándar de la duración: 0.078644
Punto óptimo encontrado: [4.802775751974287, -2.5574098752873646] en 0.23617214341498338

Ejecución 12:
Duración: 0.0173 segundos
Error absoluto promedio respecto al mínimo real: 0.472534
Distancia euclidiana promedio respecto al punto óptimo real: 8.043638
Diferencia estándar de la duración: 0.083699
Punto óptimo encontrado: [-6.3379586959607375, 0.12606992631186115] en 0.31298395090989656

Ejecución 13:
Duración: 0.0176 segundos
Error absoluto promedio respecto al mínimo real: 0.496138
Distancia euclidiana promedio respecto al punto óptimo real: 10.061214
Diferencia estándar de la duración: 0.036045
Punto óptimo encontrado: [-5.564985506090534, -5.93765801293203] en 0.4079926258918129

Ejecución 14:
Duración: 0.0171 segundos
Error absoluto promedio respecto al mínimo real: 0.494337
Distancia euclidiana promedio respecto al punto óptimo real: 11.090152
Diferencia estándar de la duración: 0.025917
Punto óptimo encontrado: [-8.399077284835508, 3.8626608869776633] en 0.43979078193994703

Ejecución 15:
Duración: 0.0170 segundos
Error absoluto promedio respecto al mínimo real: 0.323071
Distancia euclidiana promedio respecto al punto óptimo real: 2.217684
Diferencia estándar de la duración: 0.336957
Punto óptimo encontrado: [0.0016592610102741934, -0.03823588088993811] en 1.0773283376508402e-09

Ejecución 16:
Duración: 0.0176 segundos
Error absoluto promedio respecto al mínimo real: 0.496261
Distancia euclidiana promedio respecto al punto óptimo real: 10.022585
Diferencia estándar de la duración: 0.033621
Punto óptimo encontrado: [6.693177120804245, 5.136965165850739] en 0.4243882198188733

Ejecución 17:
Duración: 0.0169 segundos
Error absoluto promedio respecto al mínimo real: 0.331680
Distancia euclidiana promedio respecto al punto óptimo real: 2.797162
Diferencia estándar de la duración: 0.330230
Punto óptimo encontrado: [-0.46778701712615484, 1.6902915240565064] en 0.006001492190780056

Ejecución 18:
Duración: 0.0174 segundos
Error absoluto promedio respecto al mínimo real: 0.381985
Distancia euclidiana promedio respecto al punto óptimo real: 5.229741
Diferencia estándar de la duración: 0.220726
Punto óptimo encontrado: [-3.201120678726288, 2.090846934865072] en 0.09349205610169137

Ejecución 19:
Duración: 0.0183 segundos
Error absoluto promedio respecto al mínimo real: 0.359209
Distancia euclidiana promedio respecto al punto óptimo real: 4.805017
Diferencia estándar de la duración: 0.251893
Punto óptimo encontrado: [-2.5723662674987953, 0.09899962541314283] en 0.025315245645719242

Ejecución 20:
Duración: 0.0189 segundos
Error absoluto promedio respecto al mínimo real: 0.487740
Distancia euclidiana promedio respecto al punto óptimo real: 9.853454
Diferencia estándar de la duración: 0.038148
Punto óptimo encontrado: [6.81702689407828, 5.286765810413013] en 0.4236799345398037


Estadísticas finales:
Duración media total: 0.0182 segundos
Error absoluto promedio respecto al mínimo real: 0.442872
Distancia euclidiana promedio respecto al punto óptimo real: 7.146881 
```

### Valoración
Los puntos óptimos encontrados varían significativamente entre ejecuciones, indicando que el algoritmo puede converger a diferentes soluciones óptimas dependiendo de la configuración inicial y las iteraciones realizadas. El error absoluto promedio respecto al mínimo real oscila entre 0.323071 y 0.498885, lo que sugiere una cierta precisión en la búsqueda del punto óptimo. Con valores entre 2.217684 y 11.467669, muestra que algunos puntos óptimos están relativamente cerca del punto óptimo real, mientras que otros están más lejanos. Las duraciones promedio son muy cortas (0.0182 segundos), lo cual es positivo para aplicaciones que requieren cálculos rápidos. Ejecuciones como la 15 y la 17 muestran errores absolutos muy bajos (0.323071 y 0.331680 respectivamente), sugiriendo que en ocasiones el algoritmo logra encontrar soluciones muy cercanas al optimo real.  No parece haber una clara correlación entre la duración de la ejecución y la precisión del resultado óptimo.