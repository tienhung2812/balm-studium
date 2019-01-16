

# The program is based on DEAP Framework
# The program aims to solve the bank asset liability management problem
# desbribed in the book Business Applications of Operation Research by Bodhibrata Nag
# Authors: 
# Phat Vo Tan
# Hoang Thai Duong
# Tran Huy Hoang
# Nguyen Tien Hung
# Class: CS2015, Vietnamese German Univerisy




import random
import numpy
import pandas as pd

from deap import algorithms
from deap import base
from deap import creator
from deap import tools

# import from our implemented evaluation
import evaluation




# Choosing Seed Number is crucial, each is corresponding to
# a pseudo-random sequence of number, 
# we want to have the program run in deterministic way: the program generates
# the same results everytime we run it
#SEEDNBR = 300

#random.seed(SEEDNBR)
random.seed(None)

NBR_BUCKETS = 8 # Number of buckets
class DEAP:
    def __init__(self,data,population,generation):

        creator.create("FitnessMax", base.Fitness, weights=(1.0,1.0,))
        creator.create("Individual", list, fitness=creator.FitnessMax)

        self.toolbox = base.Toolbox()

        # Attribute generator
        self.toolbox.register("individual", self.init2d, creator.Individual)
        self.toolbox.register("population", tools.initRepeat, list, self.toolbox.individual)

        # Our evaluation function

        self.toolbox.register("evaluate", evaluation.evalALM,data)
        self.toolbox.register("mate", tools.cxOnePoint)
        
        l = [23, 0, 0, 0, 12, 0,
            23, 0, 0, 0, 12, 0,
            23, 0, 0, 0, 12, 0,
            
            23, 0, 0, 0, 12, 0,
            23, 0, 0, 0, 12, 0,
            23, 0, 0, 0, 12, 0,
            23, 0, 0, 0, 12, 0,
            23, 0, 0, 0, 12, 0
        ]
        u = [
            27,1, 44, 1, 160-10, 207,
            27,1, 44, 1, 160-10, 207,
            27,1, 44, 1, 160-10, 207,
            27,1, 44, 1, 160-10, 207,
            27,1, 44, 1, 160-10, 207,
            27,1, 44, 1, 160-10, 207,
            27,1, 44, 1, 160-10, 207,
            27,1, 44, 1, 160-10, 207
        ]
        from mutation import mutUniformFloat 
        self.toolbox.register("mutate", mutUniformFloat, low=l, up=u, indpb=0.5)
        #self.toolbox.register("mutate", tools.mutUniformInt, low=l, up=u, indpb=0.5)
        from sort import bubbleSort as bs
        self.toolbox.register("select", bs)


        self.population = population
        self.generation = generation


    def init2d(self,icls):
        # types of assets or liabilities, each has 8 values corresponding to 8 buckets
        u1=12
        u2=0.05        
        u3=10
        u4=0.05
        u5=85
        u6=130
        indGenerator = [
            
            random.uniform(0, u1),
            random.uniform(0, u2),
            random.uniform(0, u3),
            random.uniform(0, u4),
            random.uniform(0, u5),
            random.uniform(0, u6),  # end one bucket

            random.uniform(0, u1),
            random.uniform(0, u2),
            random.uniform(0, u3),
            random.uniform(0, u4),
            random.uniform(0, u5),
            random.uniform(0, u6),  # end one bucket

            random.uniform(0, u1),
            random.uniform(0, u2),
            random.uniform(0, u3),
            random.uniform(0, u4),
            random.uniform(0, u5),
            random.uniform(0, u6),  # end one bucket

            random.uniform(0, u1),
            random.uniform(0, u2),
            random.uniform(0, u3),
            random.uniform(0, u4),
            random.uniform(0, u5),
            random.uniform(0, u6),  # end one bucket

            random.uniform(0, u1),
            random.uniform(0, u2),
            random.uniform(0, u3),
            random.uniform(0, u4),
            random.uniform(0, u5),
            random.uniform(0, u6),  # end one bucket

            random.uniform(0, u1),
            random.uniform(0, u2),
            random.uniform(0, u3),
            random.uniform(0, u4),
            random.uniform(0, u5),
            random.uniform(0, u6),  # end one bucket

            random.uniform(0, u1),
            random.uniform(0, u2),
            random.uniform(0, u3),
            random.uniform(0, u4),
            random.uniform(0, u5),
            random.uniform(0, u6),  # end one bucket

            random.uniform(0, u1),
            random.uniform(0, u2),
            random.uniform(0, u3),
            random.uniform(0, u4),
            random.uniform(0, u5),
            random.uniform(0, u6),  # end one bucket            
        ]
        
        return icls(indGenerator)



    def main(self):        
        import hall_of_fame 
        #random.seed(SEEDNBR)
        random.seed(None)
        pop = self.toolbox.population(n=self.population)                                
        hof = hall_of_fame.HallOfFame(20)        
        stats = tools.Statistics(lambda ind: ind.fitness.values)
        from algorithm import eaSimple
        eaSimple(pop, self.toolbox, cxpb=0.5, mutpb=0.2, ngen=self.generation, stats=stats,
                            halloffame=hof ,verbose=True)
        
        return pop, stats, hof


