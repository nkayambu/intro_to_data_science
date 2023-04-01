import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math
import scipy.stats as stats
import statsmodels.api as sm
import os

movies = pd.read_csv("airport_routes.csv")
print(movies)

mov_min = movies["NumberOfRoutes"].min()
print(mov_min)

mov_max = movies["NumberOfRoutes"].max()
print(mov_max)

mov_mean = movies["NumberOfRoutes"].mean()
print("mean ", mov_mean)

mov_std = movies["NumberOfRoutes"].std()
print("std ", mov_std)

mov_mount = len(movies)
print(mov_mount)

mov_lambda = 1/mov_mean
print("lambda ", mov_lambda)

total = 0
for num in movies['NumberOfRoutes']:
    total += np.log(num / mov_min)
    
mov_alpha = 1 + (mov_mount / total)
print("alph ", mov_alpha)


plt.hist(movies["NumberOfRoutes"], bins=100, color='red')
plt.show()

def uniformDist(x, mn, mx):
    return 1/(mn - mx)

def powerlawDist(x, alpha, mn):
    return ((alpha - 1)/mn) * ((x/mn)**(-alpha))

mov_powerlaw_theory = []
x = []
for i in range(1,100):
    x += [i]
    mov_powerlaw_theory += [powerlawDist(i, mov_alpha, mov_min)]
    
plt.hist(mov_powerlaw_theory[0:50], bins = 100)
plt.show()

mov_normal_theory = np.random.normal(loc=mov_mean, scale = mov_std, size = 1000)
plt.hist(mov_normal_theory, bins=100, color = 'lime')
plt.show()

mov_exponential_theory = np.random.exponential(scale = 1/mov_lambda, size = 1000)
plt.hist(mov_exponential_theory, bins = 100, color = "magenta")
plt.show()

mov_uniform_theory = []
x = []
for i in range(round(mov_min), round(mov_max)):
    x += [i]
    mov_uniform_theory += [uniformDist(i, mov_min, mov_max)]
    
plt.hist(mov_uniform_theory, bins = 100, color = 'orange')
plt.show()

mov_powerlaw_theory = np.array(mov_powerlaw_theory[0:50])

#sm.qqplot((mov_powerlaw_theory), line = 's')
#plt.show()

#sm.qqplot((mov_normal_theory), line = 's')
#plt.show()

#mov_uniform_theory = np.array(mov_uniform_theory)
#sm.qqplot((mov_uniform_theory), line = 's')
#plt.show()

#mov_exponential_theory = np.array(mov_exponential_theory)
#sm.qqplot((mov_exponential_theory), line = 's')
#plt.show()



#stats.probplot(mov_powerlaw_theory, dist = 'powerlaw', plot = 'plt')
#plt.show*()