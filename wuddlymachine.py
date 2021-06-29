import numpy as np
import matplotlib.pyplot as plt
from IPython.display import Image

# Incubator's Initial State
WuddlySet = [['Cuddly',23],['Duddly',33],['Fuddly',43]]

def WuddlyMachine(x):
    trip = 100 #
    while True:
        egg = input("Which egg would you like? (Cuddly/Duddly/Fuddly): ")
        if egg not in ('Cuddly','Duddly','Fuddly'):
            print('Please enter a valid Wuddly')
            continue
        else:
            break
    vis = input("Would you like to see the fusion process? (Y/N): ")
    # Add one egg to the initial state of the Incubator
    if egg == 'Cuddly':
        WuddlySet[0][1] += 1
    elif egg == 'Duddly':
        WuddlySet[1][1] += 1
    elif egg == 'Fuddly':
        WuddlySet[2][1] += 1
    # Repeat operation until the sum of eggs in the incubator is less than 1
    while trip > 1:
        eggTot = 0
        WuddlySet.sort(key = lambda x: x[1]) # sort egg piles by the number of eggs in each ones
        WuddlySet[1][1] -= 1 # Remove an egg from the two
        WuddlySet[2][1] -= 1 #    most plentiful piles
        WuddlySet[0][1] += 1 # Add an egg to the remaining pile
        for i in range(3):
            eggTot += WuddlySet[i][1] # count the number of eggs in the incubator at each step
        trip = eggTot # if total number of eggs is 1, operation is complete
        if vis == 'Y':
            print(WuddlySet)
    return egg

print(WuddlySet)
egg = WuddlyMachine(0)
print('\n ---------------- \n The final incubator state:')
print(WuddlySet)
print('\n Congratulations on your new',egg)
Image(filename='images/'+egg+'.png')
