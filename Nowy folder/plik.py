import pandas as pd 
from matplotlib import pyplot

players = pd.read_csv('players-data.csv', sep=';')
collages = pd.read_csv('players-collage.csv', sep=';')
salories = pd.read_csv('players-salary.csv', sep=';')


"""print(players.head(3))
print(players.info())
print(collages.head(3))
print(collages.info())
print(salories.head(3))
print(salories.info())"""

#złączenie
m1 = pd.merge(left=players, right=collages, how="inner")
merged_left = m1.merge(salories, how="left")

print(merged_left)
print(merged_left.info()) #wyświetlenie informacji

def waga_na_kg(x):
    return float(x * 0.45359237)

def wzrost_na_m(x):
    wzr = x.split("-")
    return float(wzr[0]) * 30.48 + float(wzr[1]) * 2.54

merged_left["Weight [kg]"] = merged_left["Weight"].map(waga_na_kg)
merged_left["Height [m]"] = merged_left["Height"].map(wzrost_na_m)

print(merged_left)

#grupowanie po drużynie
grp1 = merged_left.groupby("Team").agg(srednie = ('Salary', 'mean'))
print(grp1)

#zamiana sredniej na inny format
grp1['srednie'] = grp1['srednie'].map('{:.2f}'.format)
print(grp1)
print(grp1.info())
