
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
SEEDNBR = 300

random.seed(SEEDNBR)

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
        import hall_of_fame 
        random.seed(SEEDNBR)
        pop = self.toolbox.population(n=self.population)                                
        hof = hall_of_fame.HallOfFame(10)        
        stats = tools.Statistics(lambda ind: ind.fitness.values)
    
        algorithms.eaSimple(pop, self.toolbox, cxpb=0.5, mutpb=0.4, ngen=self.generation, stats=stats,
                            halloffame=hof ,verbose=True)

        return pop, stats, hof


