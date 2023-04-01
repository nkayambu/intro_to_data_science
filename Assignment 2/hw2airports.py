import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math
import scipy.stats as stats
import statsmodels.api as sm
import os

airports = pd.read_csv("movie_votes.csv")
print(airports)

air_min = airports["AverageVote"].min()
print(air_min)

air_max = airports["AverageVote"].max()
print(air_max)

air_mean = airports["AverageVote"].mean()
print("mean ", air_mean)

air_std = airports["AverageVote"].std()
print("std ", air_std)

air_mount = len(airports)
print(air_mount)

air_lambda = 1/air_mean
print("lambda ", air_lambda)

total = 0
for num in airports['AverageVote']:
    total += np.log(num / air_min)
    
air_alpha = 1 + (air_mount / total)
print("alpha ", air_alpha)


plt.hist(airports["AverageVote"], bins=100, color='red')
plt.show()

def uniformDist(x, mn, mx):
    return 1/(mn - mx)

def powerlawDist(x, alpha, mn):
    return ((alpha - 1)/mn) * ((x/mn)**(-alpha))

air_powerlaw_theory = []
x = []
for i in range(1,100):
    x += [i]
    air_powerlaw_theory += [powerlawDist(i, air_alpha, air_min)]
    
plt.hist(air_powerlaw_theory[0:50], bins = 100)
plt.show()

air_normal_theory = np.random.normal(loc=air_mean, scale = air_std, size = 1000)
plt.hist(air_normal_theory, bins=100, color = 'lime')
plt.show()

air_exponential_theory = np.random.exponential(scale = 1/air_lambda, size = 1000)
plt.hist(air_exponential_theory, bins = 100, color = "magenta")
plt.show()

air_uniform_theory = []
x = []
for i in range(round(air_min), round(air_max)):
    x += [i]
    air_uniform_theory += [uniformDist(i, air_min, air_max)]
    
plt.hist(air_uniform_theory, bins=100, color = 'black')
plt.show()

sm.qqplot(air_normal_theory, line = 's')
plt.show()