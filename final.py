
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

# SISZE: The number of variables that we are trying to solve in the problem
CHROMOSOME_SIZE = 6
# Choosing Seed Number is crucial, each is corresponding to 
# a pseudo-random sequence of number
SEEDNBR = 200  
# we want to have the program run in deterministic way: the program generates 
# the same results everytime we run it
random.seed(SEEDNBR) 

UPPER_BOUND = 250  # 10^7
LOWER_BOUND = 0  # -10^7
NBR_BUCKETS = 8
IND_SIZE = 48

# types of assets or liabilities, each has 8 values corresponding to 8 buckets



def init2d(icls):
	indGenerator = [
        random.uniform(23, 27),
        random.uniform(0, 1),
        random.uniform(0, 44),
        random.uniform(0, 1),
        random.uniform(12, 160),
        random.uniform(0, 207), # end one bucket
        
        random.uniform(23, 27),
        random.uniform(0, 1),
        random.uniform(0, 44),
        random.uniform(0, 1),
        random.uniform(12, 160),
        random.uniform(0, 207), # end one bucket
        
        random.uniform(23, 27),
        random.uniform(0, 1),
        random.uniform(0, 44),
        random.uniform(0, 1),
        random.uniform(12, 160),
        random.uniform(0, 207), # end one bucket
        
        random.uniform(23, 27),
        random.uniform(0, 1),
        random.uniform(0, 44),
        random.uniform(0, 1),
        random.uniform(12, 160),
        random.uniform(0, 207), # end one bucket
        
        random.uniform(23, 27),
        random.uniform(0, 1),
        random.uniform(0, 44),
        random.uniform(0, 1),
        random.uniform(12, 160),
        random.uniform(0, 207), # end one bucket
        
        random.uniform(23, 27),
        random.uniform(0, 1),
        random.uniform(0, 44),
        random.uniform(0, 1),
        random.uniform(12, 160),
        random.uniform(0, 207), # end one bucket 

        random.uniform(23, 27),
        random.uniform(0, 1),
        random.uniform(0, 44),
        random.uniform(0, 1),
        random.uniform(12, 160),
        random.uniform(0, 207), # end one bucket 

        random.uniform(23, 27),
        random.uniform(0, 1),
        random.uniform(0, 44),
        random.uniform(0, 1),
        random.uniform(12, 160),
        random.uniform(0, 207) # end one bucket 
    ]
    
	return icls(indGenerator)



# def myatr():
#     #typeOfAL = ("RABCB", "RABOB", "RAGS", "RADB", "RAA", "LB")
#     #for i in range(NBR_BUCKETS):
#     #for i in typeOfAL:
#     variables = (random.uniform(UPPER_BOUND, LOWER_BOUND),
#                     random.uniform(UPPER_BOUND, LOWER_BOUND),
#                     random.uniform(UPPER_BOUND, LOWER_BOUND),
#                     random.uniform(UPPER_BOUND, LOWER_BOUND),
#                     random.uniform(UPPER_BOUND, LOWER_BOUND),
#                     random.uniform(UPPER_BOUND, LOWER_BOUND),
#                     random.uniform(UPPER_BOUND, LOWER_BOUND),
#                     random.uniform(UPPER_BOUND, LOWER_BOUND))
#     return variables


def myatr():
    my_val = [random.uniform(UPPER_BOUND, LOWER_BOUND)]


creator.create("FitnessMax", base.Fitness, weights=(1.0,))
creator.create("Individual", list, fitness=creator.FitnessMax)

toolbox = base.Toolbox()

# Attribute generator
# toolbox.register("attr_float", myatr)
#toolbox.register("attr_float", random.uniform, UPPER_BOUND, LOWER_BOUND)
#toolbox.register("attr_float", init2d)
# Structure initializers
#toolbox.register("individual", tools.initRepeat, creator.Individual,
#                 toolbox.attr_float, n=IND_SIZE)

# toolbox.register("individual", tools.initRepeat, creator.Individual,
#                  toolbox.attr_float, n=8)
toolbox.register("individual", init2d, creator.Individual)
#toolbox.register("individual", init2d, creator.Individual)
#toolbox.register("individual", tools.initRepeat, creator.Individual, 
#                               init2d, n=CHROMOSOME_SIZE)
toolbox.register("population", tools.initRepeat, list, toolbox.individual)
toolbox.individual()


#%%
# x = list(toolbox.individual())

#toolbox.individual()

#%%
# Our evaluation function
import evaluation
toolbox.register("evaluate", evaluation.evalALM)
toolbox.register("mate", tools.cxOnePoint)
#toolbox.register("mutate", tools.mutFlipBit, indpb=0.09)
toolbox.register("mutate", tools.mutGaussian, mu=0, sigma=0.2, indpb=0.2)
toolbox.register("select", tools.selTournament, tournsize=3)



def main():
    random.seed(SEEDNBR)
    
    NGEN = 500
    MU = 50
    LAMBDA = 100
    CXPB = 0.7
    MUTPB = 0.2
    
    pop = toolbox.population(n=1000)
    hof = tools.HallOfFame(10)
    stats = tools.Statistics(lambda ind: ind.fitness.values)
    stats.register("avg", numpy.mean, axis=0)
    stats.register("std", numpy.std, axis=0)
    stats.register("min", numpy.min, axis=0)
    stats.register("max", numpy.max, axis=0)
    
    # algorithms.eaSimple(pop, toolbox, cxpb=0.5, mutpb=0.2, ngen=50, stats=stats,
    #                     halloffame=hof, verbose=True)
    # algorithms.eaSimple(pop, toolbox, cxpb=0.9, mutpb=0.8, ngen=50, stats=stats,
    #                     halloffame=hof, verbose=True)

    algorithms.eaMuPlusLambda(pop, toolbox, MU, LAMBDA, CXPB, MUTPB, NGEN, stats,
                              halloffame=hof, verbose=True)

    data = hof[0]
    
    
    start = 0 
    for i in range(NBR_BUCKETS):        
        print(data[start+0:start+6])
        print()
        start += 6
    
    
    
    return pop, stats, hof
                 
if __name__ == "__main__":
    main()                 
