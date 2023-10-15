# Genéticos_y_8_reinas

## Introducción

## Materiales y métodos
### pyhton
### Bibliotecas usadas de Python
    - random
    De esta biblioteca se han utilizado las funciones:
        - 'random.randrange(stop)'
            Regresa un valor (entero) arbitrario de 'range(stop)'.
        - 'random.uniform(a,b)'
            Regresa un valor (flotante) arbitrario entre a y b.
        - 'random.sample(Población,n)'
            Regresa una lista de 'n' valores arbitrarios de Población sin repetir.
    - matplotlib
    De esta biblioteca se han utilizado las funciones: 
        - 'plot(x,y)'
            Grafica la lista 'x' contra la lista 'y'.
        - 'title('Titulo')'
            Asigna un título a la gráfica.
        - 'xlabel('Título de lista x')'
            Asigna un título al eje correspondiente a la lista x en la gráfica.
        - 'ylabel('Título de lista y')'
            Asigna un título al eje correspondiente a la lista y en la gráfica.
        - 'show()'
            Muestra en una ventana emergente la gráfica.
    
            
### Tabla de datos
   | Representación   | Inicialización   | Selección de padres     | Cruza       | Mutación   | Selección de descencientes   |
   |:----------------:|:----------------:|:-----------------------:|:-----------:|:----------:|:----------------------------:|
   | Permutación      | Aleatoria        | Universal estocástica   | Ordenada    | Mezcla     | Brecha generacional          |
   
### Descripción de los métodos de la tabla
    - Representación: Permutación
        Este tipo de representación utiliza los índices de la lista como indicador del número de la columna (o fila), mientras que el             valor asignado a dicho índice indica el número de la fila (o columna) donde está situada la reina.
        Un ejemplo de esta representación sería considerando la matriz:

   |      |      |      |      |      |      |      |      |
   |:----:|:----:|:----:|:----:|:----:|:----:|:----:|:----:|
   |      |      |      |      |      |      |  1   |      |
   |      |      |      |   1  |      |      |      |      |
   |      | 1    |      |      |      |      |      |      |
   |      |      |      |      |   1  |      |      |      |
   |      |      |      |      |      |      |      |  1   |
   | 1    |      |      |      |      |      |      |      |
   |      |      | 1    |      |      |      |      |      |
   |      |      |      |      |      |   1  |      |      |

       Su representación con una lista del tipo permutación sería:
       '[5, 2, 6, 1, 3, 7, 0, 4]'
        
    - Inicialización: Aleatoria
        Genera a toda la población inicial de forma arbitraria sin condiciones.
    - Selección de padres: Universal estocástica
        
    - Cruza: Ordenada
        Hojas
    - Mutación: Mezcla
        Este tipo de
    - Selección de descendientes: Brecha generacional
        Bre
### Gráfica de convergencia
    En la siguiente gráfica se puede observar como el fitness promedio de cada generación se acerca a cero cuando las generaciones            avanzan, respecto a los métodos efetuados para el algoritmo genético.
    
