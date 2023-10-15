# Genéticos_y_8_reinas

## Introducción

## Materiales y métodos

### Pyhton
Para la realización del código se ha utilizado como lenguaje de programación a _Python_ el cual es un lenguaje de alto nivel de programación interpretado cuya filosofía hace hincapié en una sintaxis muy limpia y un código legible. Es un lenguaje dinámico (_el programa se ejecuta de forma inmediata mientras sea sintácticamente corecto_) y multiplataforma. Se trata de un lenguaje de programación multiparadigma, ya que soporta parcialmente la programación:
- _Orientada a objetos:_ Se basa en la definición y uso de objetos generados por clases.
- _Imperativa:_ El programa se representa como órdenes dadas a la computadora
- _Funcional:_ Resulta de la programación declarativa, en la cual se le da a la computadora declaraciones que se usan para llegar a la solución. Este tipo lo acepta en menor medida.

#### Spyder IDE
Como entorno se ha utilizado a Spyder de Anaconda, el cual es un potente entorno científico escrito en Python, para Python, y diseñado por y para científicos, ingenieros y analistas de datos. Ofrece una combinación única de la funcionalidad avanzada de edición, análisis, depuración y creación de perfiles de una herramienta de desarrollo integral con la exploración de datos, la ejecución interactiva, la inspección profunda y las hermosas capacidades de visualización de un paquete científico.
Para más información visite [spyder](https://pypi.org/project/spyder/).

### Bibliotecas usadas de Python
#### random:
El módulo random es una biblioteca en Python que permite incorporar elementos de aleatoriedad y azar, debido a que brinda las herramientas para generar números aleatorios, seleccionar elementos de manera aleatoria y barajar listas. Las funciones proporcionadas por este módulo en realidad son métodos enlazados a instancias ocultas a la clase random.Random. 

Para más información sobre esta biblioteca visite [random](https://docs.python.org/es/3/library/random.html).

De esta biblioteca se han utilizado las funciones para enteros:
##### 'random._randrange(a)_'.
        Regresa un valor (_entero_) arbitrario de 'range(a)', es decir un número entero entre 0 y a-1.
##### 'random._uniform(a,b)_'.
        Regresa un valor (_flotante_) arbitrario del intervalo [a,b).
##### 'random._sample(Pob,n,counts=None)_'.
        Retorna una nueva lista que contiene 'n' elementos únicos de la población 'Pob' sin modificarla. Si la población incluye repeticiones, entonces cada ocurrencia es una posible selección en la muestra. Los elementos repetidos pueden especificarse con el parámetro opcional counts, que es una palabra clave.
  
#### matplotlib:
Matplotlib es una biblioteca completa para crear visualizaciones estáticas, animadas e interactivas en Python. 

Para más información visite [matplotlib](https://matplotlib.org/stable/).

De esta biblioteca se han utilizado las funciones: 
##### 'plot(x,y)'.
        Grafica la lista 'x' contra la lista 'y'.
##### 'title('Titulo')'.
        Asigna un título a la gráfica.
##### 'xlabel('Título de lista x')'.
        Asigna un título al eje correspondiente a la lista x en la gráfica.
##### 'ylabel('Título de lista y')'.
        Asigna un título al eje correspondiente a la lista y en la gráfica.
##### 'show()'.
        Muestra en una ventana emergente la gráfica. No acepta ningún argumento.
            
### Tabla de datos
   | Representación   | Inicialización   | Selección de padres     | Cruza       | Mutación   | Selección de descencientes   |
   |:----------------:|:----------------:|:-----------------------:|:-----------:|:----------:|:----------------------------:|
   | Permutación      | Aleatoria        | Universal estocástica   | Ordenada    | Mezcla     | Brecha generacional          |
   
### Descripción de los métodos de la tabla
#### Representación: Permutación
Este tipo de representación utiliza los índices de la lista como indicador del número de la *columna* (o fila), mientras que el valor asignado a dicho índice indica el número de la *fila* (o columna) donde está situada la reina.
Un ejemplo de esta representación sería [5, 2, 6, 1, 3, 7, 0, 4] cuya matriz representada es
##### Matriz
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
        
#### Inicialización: Aleatoria
Genera a toda la población inicial de forma arbitraria sin condiciones.
        
#### Selección de padres: Universal estocástica
Se da la probabilidad acumulada de distribución para cada miembro de la población denominada por 'a' y un valor 'lamda' que indica la cantidad de miembros a seleccionar. Se inicializan las variables 'i' y 'current_member' en 1. Se toma un valor (flotante) aleatorio 'r' entre 0 y 1/'lamda'. Mientras 'current_member' sea menor o igual que 'lamda' y mientras 'r' sea menor o igual que 'a[i]' (la probabilidad acumulada del miembro i) se selecciona el miembro i y se guarda en una lista 'selecc', luego a 'r' se le suma 1/'lamda' y a 'current_member' se le suma 1. De no cumplirse el segundo while a 'i' se le suma 1.
Observese que ambos ciclos se detedrán cuando no se cumpla el primer while, es decir cuando 'current_member' sea mayor que 'lamda', ya que significará que se han seleccionado 'lamda' miembros de la población.
        
#### Cruza: Ordenada
    
#### Mutación: Mezcla

#### Selección de descendientes: Brecha generacional
        Bre
### Gráfica de convergencia
    En la siguiente gráfica se puede observar como el fitness promedio de cada generación se acerca a cero cuando las generaciones            avanzan, respecto a los métodos efetuados para el algoritmo genético.
    
