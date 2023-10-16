# Genéticos_y_8_reinas

## Introducción

## Materiales

### Pyhton
Para la realización del código se ha utilizado como lenguaje de programación a _Python_, el cual es un lenguaje de alto nivel de programación interpretado cuya filosofía hace hincapié en una sintaxis muy limpia y un código legible. 

Es un lenguaje dinámico (_el programa se ejecuta de forma inmediata mientras sea sintácticamente corecto_) y multiplataforma. 

Se trata de un lenguaje de programación multiparadigma, ya que soporta parcialmente la programación:
- _Orientada a objetos:_ Se basa en la definición y uso de objetos generados por clases.
- _Imperativa:_ El programa se representa como órdenes dadas a la computadora
- _Funcional:_ Resulta de la programación declarativa, en la cual se le da a la computadora declaraciones que se usan para llegar a la solución. Este tipo lo acepta en menor medida.

Para más información visite [Python](https://www.python.org/).

#### Spyder IDE
Como entorno se ha utilizado a Spyder de Anaconda, el cual es un potente entorno científico escrito en Python, para Python, y diseñado por y para científicos, ingenieros y analistas de datos. Ofrece una combinación única de la funcionalidad avanzada de edición, análisis, depuración y creación de perfiles de una herramienta de desarrollo integral con la exploración de datos, la ejecución interactiva, la inspección profunda y las hermosas capacidades de visualización de un paquete científico.

Para más información visite [spyder](https://pypi.org/project/spyder/).

### Bibliotecas usadas de Python
#### random:
El módulo random es una biblioteca en Python que permite incorporar elementos de aleatoriedad y azar, debido a que brinda las herramientas para generar números aleatorios, seleccionar elementos de manera aleatoria y barajar listas. Las funciones proporcionadas por este módulo en realidad son métodos enlazados a instancias ocultas a la clase random.Random. 

De esta biblioteca se han utilizado las funciones para enteros:
##### 
        random.randrange(a)
#####
Regresa un valor (_entero_) arbitrario de 'range(a)', es decir un número entero entre 0 y a-1.
##### 
        random.uniform(a,b)
#####
Regresa un valor (_flotante_) arbitrario del intervalo [a,b).
##### 
        random.sample(Pob,n,counts=None)
#####
Retorna una nueva lista que contiene 'n' elementos únicos de la población 'Pob' sin modificarla. Si la población incluye repeticiones, entonces cada ocurrencia es una posible selección en la muestra. Los elementos repetidos pueden especificarse con el parámetro opcional counts, que es una palabra clave.

Para más información sobre esta biblioteca visite [random](https://docs.python.org/es/3/library/random.html).
  
#### matplotlib:
Matplotlib es una biblioteca completa para crear visualizaciones estáticas, animadas e interactivas en Python. 

De esta biblioteca se han utilizado las funciones: 
##### 
        plot(x,y)
#####
Grafica la lista 'x' contra la lista 'y'.
##### 
        title('Titulo')
#####
Asigna un título a la gráfica.
##### 
        xlabel('Título de lista x')
#####
Asigna un título al eje correspondiente a la lista x en la gráfica.
##### 
        ylabel('Título de lista y').
#####
Asigna un título al eje correspondiente a la lista y en la gráfica.
##### 
        show().
#####
Muestra en una ventana emergente la gráfica. No acepta ningún argumento.

Para más información visite [matplotlib](https://matplotlib.org/stable/).

### Estructura: Lista
Las listas son colecciones de datos los cuales pueden ser de cualquier tipo. Las listas se agrupan dentro de corchetes. Los elementos de una lista se separan con comas.

A cada elemento de una lista se le asocia una posición llamada índice, de esta manera el primer elemento de izquierda a derecha es el elemento de laposición cero, el quesigue hacia la derecha ocupa la posición uno y así sucesivamente.

Las operaciones con listas utilizadas son:

##### 
        len(lista)
#####
Regresa la longitud (tamaño) de la lista.
##### 
        max(lista)
#####
Regresa el elemento con el valor máximo.
##### 
        min(lista)
#####
Regresa el elemento con el valor mínimo.
##### 
        lista.append(obj)
#####
Adiciona objetos a la lista
##### 
        lista1.extend(lista2)
#####
Adiciona _lista2_ al final de _lista1_
##### 
        lista.insert(índice,obj)
#####
Inserta _obj_ en la posición _índice_.
##### 
        lista.reverse()
#####
Invierte el orden de los objetos de la lista.
##### 
        lista.copy()
#####
Crea una copia de los objetos de la lista.

También se utilizaron las siguientes listas de comprensión:

#####
        lst_res=[expresión for miembro in iterable]
#####
Tiene una estructura de ciclo _for_.
#####
        lst_res=[exprif if condición else exprElse for miembro in iterable]
#####
Tiene una estructura de ciclo _for_ con un condicional _if_.

## Métodos
            
### Tabla de datos
A continuación se presenta una tabla con los métodos utilizados en el código para el algoritmo genetico.
####
   | Representación   | Inicialización   | Selección de padres     | Cruza       | Mutación   | Selección de descencientes   |
   |:----------------:|:----------------:|:-----------------------:|:-----------:|:----------:|:----------------------------:|
   | Permutación      | Aleatoria        | Universal estocástica   | Ordenada    | Mezcla     | Brecha generacional          |
   
### Descripción de los métodos de la tabla
#### Representación: Permutación
Esta representación utiliza los índices de la lista como indicador del número de la *columna*, mientras que el valor asignado a dicho índice indica el número de la *fila* donde está situada la reina. 

Por ello es que cada individuo de la población está representado por una lista de tamaño 8, cuyos índices y elementos van del 0 al 7. La decisión de utilizar solo los valores del  0 al 7, y no del 1 al 8, resulta de la forma de enumeración de los índices de las listas en Python. 

Un ejemplo de esta representación sería considerar el individuo dado por
#####
        [5, 2, 6, 1, 3, 7, 0, 4] 
#####
cuya matriz representada es
##### 
|<!-- -->|<!-- -->|<!-- -->|<!-- -->|<!-- -->|<!-- -->|<!-- -->|<!-- -->|
|:------:|:------:|:------:|:------:|:------:|:------:|:------:|:------:|
|        |        |        |        |        |        |    1   |        |
|        |        |        |     1  |        |        |        |        |
|        | 1      |        |        |        |        |        |        |
|        |        |        |        |     1  |        |        |        |
|        |        |        |        |        |        |        |  1     |
| 1      |        |        |        |        |        |        |        |
|        |        | 1      |        |        |        |        |        |
|        |        |        |        |        |   1    |        |        |
##### 
Para generar de forma aleatoria un solo individuo se utiliza la función sample de la forma:
#####
        random.sample(range(8),8)
#####
Lo cual permitirá escoger de la lista [0,1,2,3,4,5,6,7] solo 8 únicos valores.

#### Inicialización: Aleatoria
Este tipo de inicialización genera a toda la población inicial de forma arbitraria sin condiciones. 

Para ello se definió una función llamada _inicializacion_ que acepta como argumento al tamaño deseado para la población, _n_. 

Por medio de una lista de comprensión (_del tipo ciclo for_) se agregan en una lista,  denomidada *Pob*, _n_ individuos generados como se explicó con anterioridad.

De esta forma, tendremos en una lista, *Pob*, almacenados a los individuos de la población inicial.
        
#### Selección de padres: Universal estocástica
Se da la probabilidad acumulada de distribución para cada miembro de la población denominada por 'a' y un valor 'lamda' que indica la cantidad de miembros a seleccionar. Se inicializan las variables 'i' y 'current_member' en 1. Se toma un valor (flotante) aleatorio 'r' entre 0 y 1/'lamda'. Mientras 'current_member' sea menor o igual que 'lamda' y mientras 'r' sea menor o igual que 'a[i]' (la probabilidad acumulada del miembro i) se selecciona el miembro i y se guarda en una lista 'selecc', luego a 'r' se le suma 1/'lamda' y a 'current_member' se le suma 1. De no cumplirse el segundo while a 'i' se le suma 1.
Observese que ambos ciclos se detedrán cuando no se cumpla el primer while, es decir cuando 'current_member' sea mayor que 'lamda', ya que significará que se han seleccionado 'lamda' miembros de la población.
        
#### Cruza: Ordenada
Este tipo de cruza toma un solo segmento de elementos aleatorio del padre y lo hereda al hijo. En caso de tener espacios vacíos en el hijo, son rellenados por elementos de la madre, heredados de forma ordenada, partiendo después del índice del último elemento heredado por el padre y regresando al primer indice de la madre hasta heredar, en conjunto con el padre, 8 elementos al hijo sin que estos se repitan.

Para ello se define una función _cruza_ que tiene como argumentos a dos individuos de _Pob_ denominados _Mama_ y _Papa_.

En ella se definen dos variables llamadas _punto_c1_ y _punto_c2_ las cuales tomarán un valor aleatorio menor que 8 usando:
#####
        random.randrange(8)
#####
Por medio de un _ciclo for_ iterado en 

#####
        range(punto_c1,punto_c2+1)
#####

se copia segmento de elementos, desde _punto_c1_ al _punto_c2_, del padre al hijo, por medio de la función _insert_ de listas.

Luego se inicializan dos variables
#####
        contador=0
#####
#####
        contador2=0
#####
de forma que al iterar en un _ciclo for_ a
#####
        range(punto_c2+1,8)
#####
se cuente, por medio de _contador_ cuántas veces se han agregado elementos de la madre al hijo después del último elemento heredado por el padre. 

Para poder agregar elementos de la madre que no hayan sido heredados en el segmento del padre, se utiliza _if-else_ cuya condición será verificar que el elemento de la madre no esté en el hijo, esto con la función _count_ de listas.

En caso de cumplirse, se debe insertar en la posición siguiente al elemento de la madre.

En caso de llegar al final de la lista de la madre se abre otro _ciclo for_ iterando en 
#####
        range(punto_c2+1)
#####
cuyo proceso esta determinado por un condicional _if-else_.

Si aún no se llega al final de la lista del hijo, es decir si se cumple la condición del _if_ determinada por 
#####
        punto_c2 + contador < 7
#####
los elementos de mamá que no estén en el hijo, en los indices del rango a iterar, se heredarán al hijo.

En cuanto no se cumpla la condición, usando _contador2_, se heredarán los elementos de la madre al hijo mediante la función _insert_ de listas.

Cada vez que se le herede un elemento al hijo de la madre tanto _contador_ como _contador2_ deben incrementarse en 1. 

Con ello, se tiene como resultado una lista con la representación utilizada,  la cual es denominada _Hijo_
    
#### Mutación: Mezcla
Dado un individuo toma un solo segmento de elementos aleatorio de él y solo esos elementos los mezcla, el resto se quedan fijos en sus posiciones de la lista. Es un tipo de permutación no ordenada.

Para ello se define una función _mutación_ que solo admite como argumento a un individuo de la población de los Hijos.

En ella se definen dos variables llamadas _punto_c1_ y _punto_c2_ las cuales tomarán un valor aleatorio menor que 8 usando:
#####
        random.randrange(8)
#####

Por medio de la función _copy()_ de listas se clona al individuo a mutar y se nombra, a dicha clonación, por _Ind_mut_.

Por otra parte, se crea una lista de índices, _Index_, por medio de la función random._sample_ descrita por
#####
        random.sample(range(punto_c1,punto_c2+1), abs(punto_c2-punto_c1+1))
#####
Dichos índices corresponden a los del segmento a mezclar.

Se inicializa una variable
#####
        k=0
#####
la cual nos va a permitir tener control en la iteración de los índices de _Index_.

Por medio de un _ciclo for_ iterado en 

#####
        range(punto_c1,punto_c2+1)
#####
se renombran los elementos de _Ind_mut_ en los índices de la iteración del ciclo por los elementos del individuo original en los indices de _Index_ cuyo índice es _k_. 

Por cada iteración, _k_ se incrementa en 1.

No hay cabida de error en el ciclo debido a que la longitud de _Index_ corresponde al número de iteraciones.

Finalmente, obtenemos al individuo mutado.

#### Selección de descendientes: Brecha generacional
Se selecciona un número, _k_, estrictamente menor que la cantidad de hijos, _n/2_, y solo esa parte de padres es reemplazada. Justo esa parte corresponde con los _k_ padres con peor _fitness_.

Para ello se define una función llamada _reemplazo_ que admite como único argumento a la población de padres.

Se le asigna al máximo de _all_fitness_ el nombre _i_.

Por medio de un ciclo _while_, mientras m sea mayor o igual que el mínimo de _all_fitness_ se efectúa un ciclo _for_ iterado en los elementos de la población, tal que si el _fitness_ del elemento de la población es igual a _i_ entonces se almacena en una lista llamada _Peores_ind_. En cada iteración se le resta 1 a _i_.

Por otra parte, se define una variable, _k_, que toma un valor arbitrario de _range(25)_ por medio de la función _random.randrange(25)_.

Se hace un ciclo _for_ que itera m en _range(k+1)_, en donde cada elemento de _Peores_ind_ es reemplazado por un elemento de _Hijos_ cuyos índices corresponden al valor _m_ iterado.

La lista resultante es la antigua lista  _Peores_ind_ pero los primeros _k_ elementos son elementos de Hijos.

### Gráfica de convergencia
La gráfica de convergencia se realizó considerando como métrica el promedio del _fitness_ de cada generación.

Considerando un ejemplo particular, tomando la  población:
####
         [[4, 2, 6, 1, 0, 3, 7, 5], [6, 4, 5, 3, 1, 0, 7, 2], [0, 6, 4, 3, 1, 5, 7, 2], [5, 2, 7, 1, 4, 0, 3, 6], [2, 3, 0, 7, 4, 1, 6, 5], [0, 1, 7, 3, 6, 2, 5, 4], [1, 5, 2, 7, 6, 0, 3, 4], [5, 3, 0, 6, 4, 7, 2, 1], [5, 6, 0, 7, 1, 4, 3, 2], [2, 3, 7, 5, 4, 1, 0, 6], [7, 4, 1, 2, 0, 3, 5, 6], [1, 6, 2, 4, 0, 5, 3, 7], [7, 1, 5, 0, 2, 4, 3, 6], [7, 1, 6, 4, 0, 3, 5, 2], [0, 1, 2, 7, 3, 4, 6, 5], [2, 1, 6, 7, 3, 4, 5, 0], [2, 4, 0, 3, 7, 6, 1, 5], [0, 7, 3, 4, 6, 1, 5, 2], [3, 7, 5, 1, 2, 4, 0, 6], [4, 7, 3, 1, 5, 0, 2, 6], [7, 0, 5, 4, 3, 6, 2, 1], [0, 3, 7, 1, 2, 5, 4, 6], [3, 0, 4, 1, 5, 6, 2, 7], [1, 0, 5, 6, 3, 4, 7, 2], [4, 0, 1, 6, 7, 2, 3, 5], [6, 0, 3, 5, 2, 4, 7, 1], [7, 2, 3, 4, 6, 5, 1, 0], [3, 4, 5, 2, 0, 1, 7, 6], [0, 1, 3, 2, 6, 4, 7, 5], [5, 6, 1, 0, 4, 7, 3, 2], [7, 2, 3, 0, 1, 4, 5, 6], [2, 5, 3, 4, 7, 6, 1, 0], [2, 5, 7, 1, 0, 6, 3, 4], [3, 5, 6, 4, 1, 2, 0, 7], [0, 3, 6, 1, 2, 4, 5, 7], [1, 5, 7, 6, 2, 3, 0, 4], [6, 2, 5, 4, 1, 3, 0, 7], [6, 5, 7, 2, 1, 4, 3, 0], [3, 7, 6, 2, 5, 4, 0, 1], [5, 2, 0, 1, 7, 4, 6, 3], [4, 1, 5, 6, 0, 2, 3, 7], [2, 3, 7, 6, 4, 1, 0, 5], [1, 4, 0, 6, 5, 2, 3, 7], [6, 0, 1, 2, 7, 4, 5, 3], [3, 6, 7, 1, 0, 4, 5, 2], [4, 0, 1, 5, 3, 7, 6, 2], [4, 0, 2, 6, 1, 7, 3, 5], [6, 5, 3, 0, 1, 7, 2, 4], [5, 6, 0, 4, 2, 7, 1, 3], [7, 1, 2, 5, 4, 6, 0, 3]]
####
Se obtiene que después de 20 generaciones, el promedio de sus fitness tiende a cero.


    
