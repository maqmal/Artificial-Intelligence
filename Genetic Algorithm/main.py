import random
import math
import matplotlib.pyplot as plt
from computation import *

gen = 20 #jumlah bit kromosom (x1=gen/2)
peluang_mutasi = 0.025 #Pm
peluang_rekombinasi = 0.065 #Pc
jumlah_populasi = 50 #jumlah populasi
generasi = 1000

def create_individu(genotype):
    individu = Phenotype(genotype)
    individu.set_x1(binary_encode(-1,2,individu.get_genotype_x1(),gen))
    individu.set_x2(binary_encode(-1,1,individu.get_genotype_x2(),gen))
    individu.set_fitness(fitness_function(individu.get_x1(),individu.get_x2()))
    
    return individu

def generate_individu(N):
    array_individu=[]
    for i in range(N):   
        individu = create_individu([random.randint(0,1) for x in range(gen)])
        array_individu.append(individu)
        
    return array_individu

def tournament_selection(populasi):    #pilih 2 individu secara random lalu bandingkan fitness functionnya
    duel = random.choices(populasi, k=2)
    duel.sort()
    return duel[0],duel[1]
    
def single_point_crossover(parent_1,parent_2): #tukar bit genotype berdasarkan titik potong T
    T = random.randint(1,gen-1)
    child_1 = []
    child_2 = []
    rand = random.uniform(0,1)
    if rand<=peluang_rekombinasi:
        child_1.extend(parent_1[:T])
        child_1.extend(parent_2[T:])
        child_2.extend(parent_2[:T])
        child_2.extend(parent_1[T:])
    else:
        child_1 = parent_1
        child_2 = parent_2
    return child_1,child_2
    
def mutation(genotype): #menukar 1 dengan 0 di setiap gen berdasarkan peluang mutasi
    for i in range(len(genotype)):
        a = random.random()
        if a <= peluang_mutasi:
            genotype[i] = 1 - genotype[i]
    return genotype

#Main program
if __name__ == "__main__":
    best_fitness = []
    fitness_mean = []
    iterasi = 0
    populasi = generate_individu(jumlah_populasi) #generate individu sejumlah jumlah_populasi
    while iterasi<generasi:
        populasi_baru = []
        populasi.sort() #index terakhir adalah individu dengan fitness terbaik
        populasi_baru.append(populasi[0]) #elitism - ambil 2 individu terbaik untuk dimasukkan kedalam populasi baru
        populasi_baru.append(populasi[1])
        
        while (len(populasi_baru)<jumlah_populasi):
            parent_1,parent_2 = tournament_selection(populasi)

            child_1,child_2 = single_point_crossover(parent_1.get_genotype(),parent_2.get_genotype())
            child_1,child_2 = mutation(child_1),mutation(child_2)
                
            individu_baru_1 = create_individu(child_1)
            individu_baru_2 = create_individu(child_2)

            populasi_baru.append(individu_baru_1)
            populasi_baru.append(individu_baru_2)
        
        populasi = populasi_baru
        best_fitness.append(populasi[0].get_fitness()) #taruh best fitness dari setiap generasi kedalam array untuk dimasukkan kedalam graph
        iterasi+=1

    #print("Function result = ",h(populasi[0].get_x1(),populasi[0].get_x2()))
    print("===================================Hasil Terbaik====================================")
    print("x1 = ",populasi[0].get_x1())
    print("x2 = ",populasi[0].get_x2())
    print("Kromosom terbaik =",populasi[0].get_genotype())
    print("====================================================================================")

# -------------------------Fungsi Untuk Graph------------------------------------
    x = []
    y = best_fitness
    for j in range(generasi):
        x.append(j) 
    
    plt.xlabel('Generasi')
    plt.ylabel('BEST Fitness')
    plt.plot(x,y)
    plt.savefig("graph/best.png")

    
