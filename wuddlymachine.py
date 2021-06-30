import numpy as np
import matplotlib.pyplot as plt
from IPython.display import Image

# Incubator's Initial State
WuddlySet = {'Cuddly':23,'Duddly':33,'Fuddly':43}

def WuddlyMachine(x):
    trip = 999 
    while True:
        egg = input("Which egg would you like? (Cuddly/Duddly/Fuddly): ")
        if egg not in ('Cuddly','Duddly','Fuddly'):
            print('Please enter a valid Wuddly')
            continue
        else:
            break
    vis = input("Would you like to see the fusion process? (Y/N): ")
    
    WuddlySet[egg] += 1 # Add one egg to the initial state of the Incubator
    
    while trip > 1: # Repeat operation until the sum of eggs in the incubator is less than 1
        eggTot = 0 
        low = [key for key in WuddlySet if WuddlySet[key] == min(WuddlySet.values())] # Identify lowest key in dict
        for wuddly in WuddlySet:
            if wuddly == low[0]:
                WuddlySet[wuddly] += 1 # if lowest key, add one egg
            else:
                WuddlySet[wuddly] -= 1 # if not the lowest key, add subtract egg
            eggTot += WuddlySet[wuddly] # count the number of eggs after each fusion
        trip = eggTot # if total number of eggs is 1, operation is complete, trip will fire
        if vis == 'Y': # Visualise the egg piles change
            print(WuddlySet)
    return egg

print(WuddlySet)
egg = WuddlyMachine(1)
print('\n ---------------- \n The final incubator state:')
print(WuddlySet)
print('\n Congratulations on your new',egg)
Image(filename='images/'+egg+'.png')
