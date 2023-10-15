import random

n=int(input('Ingrese la cantidad de individuos de la población: '))

#Funciones

def inicializacion(n):
    Pob=[random.sample(range(8),8) for i in range(n)]
    return Pob

def fitness(Individuo):
    fitness=0
    for i in range(8):
        for j in range(8):
            if (j+i+1==8):
                break
            else:
                if abs(Individuo[i]-Individuo[j+i+1])==abs(j+i+1-i):
                        fitness=fitness+1
    return fitness

def seleccion(Pob):
    suma_fitness=0
    for i in range(n):
        suma_fitness = suma_fitness + all_fitness[i]
    ind_prob=[all_fitness[i]/suma_fitness for i in range(n)]
    acum_prob_num=0
    acum_prob_lista=[]
    for i in range(n):
        acum_prob_num=acum_prob_num + ind_prob[i]
        acum_prob_lista.append(acum_prob_num)
    acum_prob=[acum_prob_lista[i] if i==0 else 
               acum_prob_lista[i-1]+acum_prob_lista[i] 
               for i in range(n)]
    lamda=n/2
    current_member=1
    i=1
    r=random.uniform(0, 1/lamda)
    selec=[]
    while current_member <= lamda:
        while r <= acum_prob[i]:
            selec.append(Pob[current_member])
            r = r+(1/lamda)
            current_member=current_member+1
        i=i+1
    return selec

def cruza(Papa,Mama):
    punto_c1=random.randrange(8)
    punto_c2=random.randrange(8)
    if punto_c1 > punto_c2:
        punto_c1=abs(punto_c2-punto_c1+1) 
    Hijo=[]
    for i in range(punto_c1,punto_c2+1):
        Hijo.insert(i,Papa[i])
    contador=0
    contador2=0
    for i in range(punto_c2+1,8):
        if Hijo.count(Mama[i])==0:
            Hijo.insert(punto_c2+1+contador,Mama[i])
            contador=contador+1
    for i in range(punto_c2+1):
        if Hijo.count(Mama[i])==0:
            if punto_c2 + contador < 7:
                Hijo.insert(punto_c2+1+contador,Mama[i])
                contador=contador+1
            else:
                Hijo.insert(contador2,Mama[i])
                contador2=contador2+1
    return Hijo       

def mutacion(Ind):
    punto_c1=random.randrange(8)
    punto_c2=random.randrange(8)
    Ind_mut=Ind.copy()
    if punto_c1 > punto_c2:
        punto=punto_c1
        punto_c1=punto_c2
        punto_c2=punto
    Index=random.sample(range(punto_c1,punto_c2+1), abs(punto_c2-punto_c1+1))
    k=0
    for i in range(punto_c1,punto_c2+1):
        Ind_mut[i]=Ind[Index[k]]
        k=k+1
    return Ind_mut

def reemplazo(Pob):
    i=max(all_fitness)
    Peores_ind=[]
    while i>= min(all_fitness):
        for j in Pob:
            if fitness(j)==i:
                Peores_ind.append(j)
        i=i-1
    k=random.randrange(25)
    for i in range(k+1):
        Peores_ind[i]=Hijos[i]
    return Peores_ind  

#  Código fuente

#Inicialización de la poblacion
Pob=inicializacion(n)
all_fitness=[fitness(Pob[i]) for i in range(n)]
print('\n', 'Sus fitness son:', '\n', all_fitness)

for generation in range(20):
    print('\n', 'GENERACION ', generation)

    #Seleccion de padres
    papa=seleccion(Pob)
    mama=seleccion(Pob)
    mama.reverse()

    #Generacion de hijos por cruza
    Hijos=[cruza(papa[i], mama[i]) for i in range(25)]

    #Mutacion de los hijos
    Hijos=[mutacion(Hijos[i]) for i in range(25)]

    #Brecha generacional
    Pob=reemplazo(Pob)

    #Nuevo fitness
    all_fitness=[fitness(Pob[i]) for i in range(n)]
    print('\n', 'Sus fitness son:', '\n', all_fitness)

Mejores_ind=[]
for i in Pob:
    if fitness(i)==min(all_fitness):
        Mejores_ind.append(i)

print('\n', 'Los mejores individuos son: ')
for i in range(len(Mejores_ind)):
    print('\n',Mejores_ind[i])