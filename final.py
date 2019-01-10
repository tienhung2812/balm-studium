
#%%

# The program is based on DEAP Framework
# The program aims to solve the bank asset liability management problem
# desbribed in the book Business Applications of Operation Research by Bodhibrata Nag
# Author: Phat Vo Tan, CS2015 @ VGU


import random
import numpy
import pandas as pd

from deap import algorithms
from deap import base
from deap import creator
from deap import tools

# import from our implemented evaluation
import evaluation

# SISZE: The number of variables that we are trying to solve in the problem
CHROMOSOME_SIZE = 6
# Choosing Seed Number is crucial, each is corresponding to
# a pseudo-random sequence of number
SEEDNBR = 300
# we want to have the program run in deterministic way: the program generates
# the same results everytime we run it
random.seed(SEEDNBR)
# Number of buckets
NBR_BUCKETS = 8
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
        self.toolbox.register("mate", tools.cxBlend, alpha=0.5)
        self.toolbox.register("mutate", tools.mutUniformInt, low=0, up=48, indpb=0.5)
        self.toolbox.register("select", tools.selTournament, tournsize=3)

        self.population = population
        self.generation = generation


    def init2d(self,icls):
        # types of assets or liabilities, each has 8 values corresponding to 8 buckets
        indGenerator = [
            random.uniform(23, 27),
            random.uniform(0, 1),
            random.uniform(0, 44),
            random.uniform(0, 1),
            random.uniform(12, 160),
            random.uniform(0, 207),  # end one bucket

            random.uniform(23, 27),
            random.uniform(0, 1),
            random.uniform(0, 44),
            random.uniform(0, 1),
            random.uniform(12, 160),
            random.uniform(0, 207),  # end one bucket

            random.uniform(23, 27),
            random.uniform(0, 1),
            random.uniform(0, 44),
            random.uniform(0, 1),
            random.uniform(12, 160),
            random.uniform(0, 207),  # end one bucket

            random.uniform(23, 27),
            random.uniform(0, 1),
            random.uniform(0, 44),
            random.uniform(0, 1),
            random.uniform(12, 160),
            random.uniform(0, 207),  # end one bucket

            random.uniform(23, 27),
            random.uniform(0, 1),
            random.uniform(0, 44),
            random.uniform(0, 1),
            random.uniform(12, 160),
            random.uniform(0, 207),  # end one bucket

            random.uniform(23, 27),
            random.uniform(0, 1),
            random.uniform(0, 44),
            random.uniform(0, 1),
            random.uniform(12, 160),
            random.uniform(0, 207),  # end one bucket

            random.uniform(23, 27),
            random.uniform(0, 1),
            random.uniform(0, 44),
            random.uniform(0, 1),
            random.uniform(12, 160),
            random.uniform(0, 207),  # end one bucket

            random.uniform(23, 27),
            random.uniform(0, 1),
            random.uniform(0, 44),
            random.uniform(0, 1),
            random.uniform(12, 160),
            random.uniform(0, 207)  # end one bucket
        ]

        return icls(indGenerator)



    def main(self):        
        random.seed(SEEDNBR)


        pop = self.toolbox.population(n=self.population)
        
        import hall_of_fame 
        x = hall_of_fame
        hof = tools.HallOfFame(10)
        hof = hall_of_fame.HallOfFame(10)
        # hof = x
        
        stats = tools.Statistics(lambda ind: ind.fitness.values)
        stats.register("avg", numpy.mean, axis=0)
        stats.register("std", numpy.std, axis=0)
        stats.register("min", numpy.min, axis=0)
        stats.register("max", numpy.max, axis=0)

        

        algorithms.eaSimple(pop, self.toolbox, cxpb=0.5, mutpb=0.4, ngen=self.generation, stats=stats,
                            halloffame=hof ,verbose=True)

        # NGEN = 5
        # MU = 50
        # LAMBDA = 100
        # CXPB = 0.7
        # MUTPB = 0.2
        # algorithms.eaMuPlusLambda(pop, self.toolbox, MU, LAMBDA, CXPB, MUTPB, NGEN, stats,
        #                           halloffame=hof, verbose=True)

        # print("HALL OF FAME")
        # print("FIRST")
        # data = hof[0]
        
        # # print(type(data))
        # # print(data.fitness)
        # start = 0
        # print("FITNESS VALUE" + str(data.fitness.values[0]))
        # print("COUNT: "+str(data.fitness.values[1]))
        # for i in range(NBR_BUCKETS):
        #     print(data[start+0:start+6])
        #     print()
        #     start += 6

        # print("HALL OF FAME")
        # print("SECOND")
        # data = hof[1]
        # # print(type(data))
        # # print(data.fitness)
        # start = 0
        # print("FITNESS VALUE" + str(data.fitness.values[0]))
        # print("COUNT: "+str(data.fitness.values[1]))
        # for i in range(NBR_BUCKETS):
        #     print(data[start+0:start+6])
        #     print()
        #     start += 6

        # print("HALL OF FAME")
        # print("LAST")
        # data = hof[-1]
        # # print(type(data))
        # # print(data.fitness)
        # start = 0
        # print("FITNESS VALUE:\t" + str(data.fitness.values[0]))
        # print("COUNT: "+str(data.fitness.values[1]))
        # for i in range(NBR_BUCKETS):
        #     print(data[start+0:start+6])
        #     print()
        #     start += 6

        return pop, stats, hof


    # if __name__ == "__main__":
    #     main()

