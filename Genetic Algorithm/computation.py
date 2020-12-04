# memisahkan class phenotype/individu dan fungsi komputasi dari file utama agar lebih rapi
import math
class Phenotype:
    def __init__(self, genotype):
        self.genotype = genotype
        self.genotype_x1 = genotype[:len(genotype)//2]
        self.genotype_x2 = genotype[len(genotype)//2:]
    
    def __lt__(self, other): #sort berdasarkan fitness terbaik (fitness terbaik berada pada urutan pertama)
         return self.f > other.f

    def set_x1(self, x1): 
        self.x1 = x1
    def set_x2(self, x2): 
        self.x2 = x2

    def get_x1(self):
        return self.x1
    def get_x2(self):
        return self.x2

    def get_genotype (self):
        return self.genotype

    def get_genotype_x1(self):
        return self.genotype_x1
    def get_genotype_x2(self):
        return self.genotype_x2
    
    def set_fitness(self,f):
        self.f = f

    def get_fitness(self):
        return self.f  

def h(x1,x2):
    h = math.cos(x1)*math.sin(x2) - x1/((x2**2)+1)
    return h

def fitness_function(x1,x2):
    main_function = h(x1,x2)
    f = -main_function
    return f

def sigma(first, last, const):
    hasil = 0
    for i in range(first, last + 1):
        hasil += (const**-i) * i
    return hasil

def binary_encode(rb,ra,genotype,gen):
    binary = rb+((ra-rb)/sigma(1,gen-1,2))*(multiply(genotype))
    return binary

def multiply(genotype):
    multiply = 0
    for i in range(len(genotype)):
        multiply = multiply + genotype[i]*2**-i
    result = multiply
    return result

