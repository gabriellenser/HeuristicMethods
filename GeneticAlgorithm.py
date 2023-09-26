from math import ceil, sin, pi
from random import randint, random, uniform
min_x, max_x=-2, 4
pop_size=300
breed_rate = 0.75
select_amount = 0.03
mutation_rate = 0.02
elet_rate = 0.01
nun_gen = 30
gen = 1
class element:
    def __init__(self) -> None:
        self.x=uniform(min_x, max_x)
    def get_fit(self):
        return self.x*sin(10*pi*self.x)+5
    fit=property(get_fit)

population=[]
def generate_random_population():
    for i in range(pop_size):
        population.append(element())

def select():
    elements = []
    for i in range(ceil(pop_size/select_amount)):
        elements.append(population[randint(0, pop_size-1)])
    final = elements[0]
    for i in elements:
        if(final.fit<i.fit):
            final=i
    return final

def generate_son(p1, p2):
    f1, f2 = element(), element()
    if(random()<breed_rate):
        beta = random()
        f1.x = beta*p1.x+(1-beta)*p2.x
        f2.x = beta*p2.x+(1-beta)*p1.x
    else:
        f1, f2 = p1, p2
    return f1, f2

def mutate(x):
    if(random()<=mutation_rate):
        x.x=uniform(min_x, max_x)
    return x

def elet():
    best=[]
    while(len(best)<round(pop_size*elet_rate, 0)):
        aux = population[0]
        for i in population:
            if(i.fit>aux.fit):
                aux=i
        population.remove(aux)
        best.append(aux)
    return best

generate_random_population()
def breed():
    new_population=[]
    while (len(new_population)<pop_size):
        p1, p2=select(), select()
        f1, f2 = generate_son(p1, p2)
        f1=mutate(f1)
        f2=mutate(f2)
        new_population.append(f1)
        new_population.append(f2)
    elet_list = elet()
    for i in elet_list:
        new_population.append(i)
    while(len(new_population)>pop_size):new_population.pop(randint(0, len(new_population)-1))
    global population
    population=new_population

def print_population():
    print("generation ", gen, ": ", sep='')
    for i in population:
        print(i.x, ", ", i.fit, sep='')
    #print("best element:", elet()[0])


for i in range(1, nun_gen):
    print_population()
    breed()
    gen=i+1
print_population()