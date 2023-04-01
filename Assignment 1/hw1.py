import pandas as pd
import numpy as np
import os

#create dataframe
dataframe = pd.read_excel('excel.xlsx')

#print(dataframe)


print(dataframe.iloc[:,4])

# all different restaurants
r = dataframe.restaurant.unique()
print(len(r))

# all different foods
food = dataframe.type.unique()
print(len(food))

# average calories of all the different foods
avgcal = dataframe.calories.mean()
avgcal = round(avgcal)
print(avgcal)

# minimum serving size of a single item
minss = dataframe.serving_size.min()
print(minss)

# maximum sodium of a single item
maxsodium = dataframe.sodium.max()
print(dataframe.loc[dataframe["sodium"]==maxsodium])
print(maxsodium)

# sum of calories
calsum = dataframe.calories.sum()
print(calsum)

# maximum amount of sugars of a single item
maxsugar = dataframe.sugars.max()
maxsugar = int(maxsugar)
print(maxsugar)
print(dataframe.loc[dataframe["sugars"] == maxsugar])



#data filtering

# number of milkshakes in the dataset
milkshakes = dataframe.loc[dataframe["type"] == "Milkshake"]
print(len(milkshakes))


# Summarize by group 

# average calories for each type of food
type_foods = dataframe.groupby("type")["calories"].mean().round()
print(type_foods)

# highest calorie count for each menu item for each restaurant

rest = dataframe.groupby(["calories"], as_index=False, sort=False, group_keys=True).max()
r = dataframe.groupby(["restaurant"], as_index=False, sort = True, group_keys=True)["calories"].max().reset_index()

print(rest)
print(r)

