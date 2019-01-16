import time
def bubbleSort(individuals, k):
    n = len(individuals)
 
    # Traverse through all individualsay elements

    for i in range(n):
 
        # Last i elements are already in place
        for j in range(0, n-i-1):
 
            # traverse the individualsay from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            
            if individuals[j].fitness.values[1] < individuals[j+1].fitness.values[1] :
                individuals[j], individuals[j+1] = individuals[j+1], individuals[j]
    

    return individuals[:k]
