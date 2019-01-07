
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
SEEDNBR = 100  
# we want to have the program run in deterministic way: the program generates 
# the same results everytime we run it
random.seed(SEEDNBR) 

UPPER_BOUND = 10000000  # 10^7
LOWER_BOUND = -10000000  # -10^7

#variables = {}
# types of assets or liabilities, each has 8 values corresponding to 8 buckets

NBR_BUCKETS = 8


def myatr():
    #typeOfAL = ("RABCB", "RABOB", "RAGS", "RADB", "RAA", "LB")
    #for i in range(NBR_BUCKETS):
    #for i in typeOfAL:
    variables = (random.uniform(UPPER_BOUND, LOWER_BOUND),
                    random.uniform(UPPER_BOUND, LOWER_BOUND),
                    random.uniform(UPPER_BOUND, LOWER_BOUND),
                    random.uniform(UPPER_BOUND, LOWER_BOUND),
                    random.uniform(UPPER_BOUND, LOWER_BOUND),
                    random.uniform(UPPER_BOUND, LOWER_BOUND),
                    random.uniform(UPPER_BOUND, LOWER_BOUND),
                    random.uniform(UPPER_BOUND, LOWER_BOUND))
    return variables

creator.create("FitnessMax", base.Fitness, weights=(1.0,))
creator.create("Individual", numpy.ndarray, fitness=creator.FitnessMax)
# numpy.ndarray is used for the purpose of efficient and functionality, 
# but list also okay
toolbox = base.Toolbox()

# Attribute generator
toolbox.register("attr_float", myatr)

# Structure initializers
toolbox.register("individual", tools.initRepeat, creator.Individual, 
                               toolbox.attr_float, n=CHROMOSOME_SIZE)
toolbox.register("population", tools.initRepeat, list, toolbox.individual)


#%%
x = list(toolbox.individual())
print(x)
# for i in range(0, 8):
#     print(x[i])

#%%
data = pd.read_excel("data.xlsx", None)  # Load all sheets
for i in range(0, 8):        
    print(data['Return'].iloc[i]['RABCB'])



#%%
# Our evaluation function
import evaluation
#evaluation.evalALM()

#%%
toolbox.register("evaluate", evaluation.evalALM)
toolbox.register("mate", tools.cxTwoPoints)
toolbox.register("mutate", tools.mutFlipBit, indpb=0.09)
toolbox.register("select", tools.selTournament, tournsize=10)


def main():
    random.seed(SEEDNBR)

    
    pop = toolbox.population(n=1000)
    hof = tools.HallOfFame(10)
    stats = tools.Statistics(lambda ind: ind.fitness.values)
    stats.register("avg", numpy.mean, axis=0)
    stats.register("std", numpy.std, axis=0)
    stats.register("min", numpy.min, axis=0)
    stats.register("max", numpy.max, axis=0)
    
    algorithms.eaSimple(pop, toolbox, cxpb=0.6, mutpb=0.6, ngen=50, stats=stats,
                        halloffame=hof, verbose=True)
    print(pop[0:5])
    return pop, stats, hof
                 
if __name__ == "__main__":
    main()                 
