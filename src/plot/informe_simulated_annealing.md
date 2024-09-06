El algoritmo de Simulated Annealing es una técnica de optimización inspirada en el proceso de enfriamiento de metales fundidos. El cual funciona de la siguiente manera.

### Funcionamiento del Algoritmo

1. **Inicialización**: El algoritmo comienza con una solución inicial aleatoria dentro de los límites definidos.

2. **Iteraciones**: Se realiza un número máximo de iteraciones, en cada una se genera una nueva solución cercana a la actual.

3. **Evaluación**: La función objetivo se calcula para ambas soluciones (actual y nueva).

4. **Aceptación**: Si la nueva solución es mejor o tiene una probabilidad de ser aceptada (determinada por la temperatura), se adopta como nueva solución.

5. **Enfriamiento**: La temperatura disminuye gradualmente a lo largo de las iteraciones.

6. **Conclusión**: El algoritmo termina cuando la temperatura alcanza un valor mínimo o se supera el número máximo de iteraciones.

Trabajamos sobre la funcion **Schaffer No. 1** y corrimos 20 veces el algoritmo obteniendo los siguientes resultados.

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
A partir de esta fue la informacion obtenida al correr el algoritmo genera un informe donde expliques en que consiste el algoritmo pq se usa 
```


### Valoración
Los puntos óptimos encontrados varían significativamente entre ejecuciones, indicando que el algoritmo puede converger a diferentes soluciones óptimas dependiendo de la configuración inicial y las iteraciones realizadas. El error absoluto promedio respecto al mínimo real oscila entre 0.323071 y 0.498885, lo que sugiere una cierta precisión en la búsqueda del punto ṕptimo. Con valores entre 2.217684 y 11.467669, muestra que algunos puntos óptimos están relativamente cerca del punto óptimo real, mientras que otros están más lejanos. Las duraciones promedio son muy cortas (0.0182 segundos), lo cual es positivo para aplicaciones que requieren cálculos rápidos. Ejecuciones como la 15 y la 17 muestran errores absolutos muy bajos (0.323071 y 0.331680 respectivamente), sugiriendo que en ocasiones el algoritmo logra encontrar soluciones muy cercanas al optimo real.  No parece haber una clara correlación entre la duración de la ejecución y la precisión del resultado óptimo.


El Simulated Annealing demuestra ser una herramienta útil para la optimización, capaz de encontrar soluciones decentes en un tiempo relativamente rápido