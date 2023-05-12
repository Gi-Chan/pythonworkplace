# Imports 
import numpy as np



prob = np.array([1,2,3,4,5])
reci = 1/prob
total = reci.sum()
prob_list = reci/total

test = np.random.choice(prob, len(prob), p=prob_list, replace=False)
print(test)