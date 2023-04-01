import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math
import scipy.stats as stats
import statsmodels.api as sm
import os

def uniformDist(x, mn, mx):
    return 1/(mn - mx)

def powerlawDist(x, alpha, mn):
    return ((alpha - 1)/mn) * ((x/mn)**(-alpha))

#inputfile = open("DoB.txt", 'r')

birth_dates = [] 

#for input in inputfile.read(): 
#    birth_dates.append(input.strip())
 
with open('DoB.txt', 'r') as file:
    for line in file:
        birth_dates.append(line.strip())
print(birth_dates)

years = [int(date.split('-')[2]) + 1900 for date in birth_dates]
print(years)

ages = [2023 - year for year in years]
ages_arr = np.array(ages)
filtered_age = ages_arr[(ages_arr > 10) & (ages_arr < 99)]

print(ages)

print('max ', np.max(filtered_age))
print('min ', np.min(filtered_age))
max = np.max(filtered_age)
min = np.min(filtered_age)

plt.hist(filtered_age, bins = 10)
plt.xlabel('Ages')
plt.ylabel('Count')
plt.show()

print("1")

#basic calc
#lmin = last_digit.min()
#lmax = last_digit.max()
mean = np.mean(filtered_age)
std = np.std(filtered_age)
mount = len(filtered_age)
alambda = 1/mean
total = 0
min = 1
for num in filtered_age:
    total += np.log(num / min)
    
alpha = 1 + (mount / total)


# normal

dob_normal_theory = np.random.normal(loc=mean, scale = std, size = 1000)
plt.hist(dob_normal_theory, bins=100, color = 'lime')
plt.show()
sm.qqplot(dob_normal_theory, line = 's')
plt.show()

# exp
dexponential_theory = np.random.exponential(scale = 1/alambda, size = 1000)
plt.hist(dexponential_theory, bins = 100, color = "magenta")
plt.show()
sm.qqplot(dexponential_theory, line = 's')
plt.show()


# uniform
dob_uniform_theory = []
x = []
for i in range(round(min), round(max)):
    x += [i]
    dob_uniform_theory += [uniformDist(i, min, max)]

plt.hist(dob_uniform_theory, bins=100, color = 'black')
plt.show()

dob_uniform_theory = np.array(dob_uniform_theory)

sm.qqplot(dob_uniform_theory, line = 's')
plt.show()

    
#powerlaw
powerlaw_theory = []
x = []
for i in range(1,100):
    x += [i]
    powerlaw_theory += [powerlawDist(i, alpha, min)]
    
plt.hist(powerlaw_theory, bins = 100)
plt.show()
powerlaw_theory = np.array(powerlaw_theory)
sm.qqplot((powerlaw_theory), line = 's')
plt.show()

#################################################################################################################

first_digits = [int(str(age)[0]) for age in filtered_age]
plt.hist(first_digits, bins = 10, color = 'red')
plt.xlabel('First Digit of Age')
plt.ylabel('Count')
plt.show()
fmax = np.max(first_digits)
fmin = np.min(first_digits)

print("2")
#basic calc
#lmin = last_digit.min()
#lmax = last_digit.max()
fmean = np.mean(first_digits)
fstd = np.std(first_digits)
fmount = len(first_digits)
flambda = 1/fmean
ftotal = 0
fmin = 1
for num in first_digits:
    ftotal += np.log(num / fmin)
    
lalpha = 1 + (fmount / ftotal)


# normal

fdob_normal_theory = np.random.normal(loc=fmean, scale = fstd, size = 1000)
plt.hist(fdob_normal_theory, bins=100, color = 'lime')
plt.show()
sm.qqplot(fdob_normal_theory, line = 's')
plt.show()

# exp
fexponential_theory = np.random.exponential(scale = 1/flambda, size = 1000)
plt.hist(fexponential_theory, bins = 100, color = "magenta")
plt.show()
sm.qqplot(fexponential_theory, line = 's')
plt.show()


# uniform
fdob_uniform_theory = []
x = []
for i in range(round(fmin), round(fmax)):
    x += [i]
    fdob_uniform_theory += [uniformDist(i, fmin, fmax)]

plt.hist(fdob_uniform_theory, bins=100, color = 'black')
plt.show()

fdob_uniform_theory = np.array(fdob_uniform_theory)

sm.qqplot(fdob_uniform_theory, line = 's')
plt.show()

    
#powerlaw
fpowerlaw_theory = []
x = []
for i in range(1,100):
    x += [i]
    fpowerlaw_theory += [powerlawDist(i, lalpha, fmin)]
    
plt.hist(fpowerlaw_theory, bins = 100)
plt.show()
fpowerlaw_theory = np.array(fpowerlaw_theory)
sm.qqplot((fpowerlaw_theory), line = 's')
plt.show()


#####################################################################################################################

last_digit = [age % 10 for age in filtered_age]
plt.hist(last_digit, bins = 10, color = 'green')
plt.xlabel('Last Digit of Age')
plt.ylabel('Count')
plt.show()
lmax = np.max(last_digit)
lmin = np.min(last_digit)

print ('3')
#basic calc
#lmin = last_digit.min()
#lmax = last_digit.max()
lmean = np.mean(last_digit)
lstd = np.std(last_digit)
lmount = len(last_digit)
llambda = 1/lmean
ltotal = 0
lmin = 1
for num in last_digit:
    ltotal += np.log(num / lmin)
    
lalpha = 1 + (lmount / ltotal)


# normal

ldob_normal_theory = np.random.normal(loc=lmean, scale = lstd, size = 1000)
plt.hist(ldob_normal_theory, bins=100, color = 'lime')
plt.show()
sm.qqplot(ldob_normal_theory, line = 's')
plt.show()

# exp
lexponential_theory = np.random.exponential(scale = 1/llambda, size = 1000)
plt.hist(lexponential_theory, bins = 100, color = "magenta")
plt.show()
sm.qqplot(lexponential_theory, line = 's')
plt.show()


# uniform
ldob_uniform_theory = []
x = []
for i in range(round(lmin), round(lmax)):
    x += [i]
    ldob_uniform_theory += [uniformDist(i, lmin, lmax)]

plt.hist(ldob_uniform_theory, bins=100, color = 'black')
plt.show()

ldob_uniform_theory = np.array(ldob_uniform_theory)

sm.qqplot(ldob_uniform_theory, line = 's')
plt.show()

    
#powerlaw
lpowerlaw_theory = []
x = []
for i in range(1,100):
    x += [i]
    lpowerlaw_theory += [powerlawDist(i, lalpha, lmin)]
    
plt.hist(lpowerlaw_theory, bins = 100)
plt.show()
lpowerlaw_theory = np.array(lpowerlaw_theory)
sm.qqplot((lpowerlaw_theory), line = 's')
plt.show()


    
