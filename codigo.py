import random

n=int(input('Ingrese la cantidad de individuos de la población: '))

#Funciones


def inicializacion(n):
    Pob=[random.sample(range(8),8) for i in range(n)]
    return Pob

def fitness(Individuo):
    i=0
    fitness=0
    while i<7:
        k=0
        while k<7:
            if (k+i+1==8):
                k=7
            else:
                if abs(Individuo[i]-Individuo[k+i+1])==abs(k+i+1-i):
                    fitness=fitness+1
                k=k+1
        i=i+1
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


    acum_prob=[acum_prob_lista[i] if i==0 else acum_prob_lista[i-1]+acum_prob_lista[i] for i in range(n)]

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
    k=0
    for i in range(punto_c2+1,8):
        if Hijo.count(Mama[i])==0:
            Hijo.insert(i,Mama[i])
            k=k+1
    if punto_c2+k<7:
        i=punto_c2+k+1
        for j in range(punto_c2):
            while i<=8:
                if Hijo.count(Mama[j])==0:
                    Hijo.insert(i,Mama[j])
                    i=i+1
    if len(Hijo)<8:
        Hijo_parteinicial=[]
        for i in range(9):
            if Hijo.count(Mama[i])==0:
                Hijo_parteinicial.append(Mama[i])
        Hijo_parteinicial.extend(Hijo)
        Hijo=Hijo_parteinicial

    return Hijo



#Código

Pob=inicializacion(n)

all_fitness=[fitness(Pob[i]) for i in range(n)]

Papa=seleccion(Pob)
Mama=seleccion(Pob)