import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sn
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score

dane = pd.read_csv("users.csv", sep=";")
print(dane.head(5))

dane.drop('User ID', inplace=True, axis=1)


def na_dolary(x):
    x = x.replace(" ", "")
    x = x.replace("$", "")
    x = x.replace(",", "")
    return x

dane["EstimatedSalary"] = dane["EstimatedSalary"].map(lambda x: na_dolary(x))
dane["EstimatedSalary"] = dane["EstimatedSalary"].map(lambda x: float(x)) 
print(dane.head(5))


def gender(x):
    if x == 'Female': return 1
    elif x == 'Male': return 0
dane["Gender"] = dane["Gender"].map(lambda x: gender(x)) 

def purchased(x):
    if x == 'Yes': return 1
    elif x == 'No': return 0
dane["Purchased"] = dane["Purchased"].map(lambda x: purchased(x)) 
print(dane.head(5))



#X = np.array(dane[["Gender","Age","EstimatedSalary"]])
#y = np.array(dane["y"])

#X_treningowe, x_testowe, y_treningowe, y_testowe = train_test_split(X,y,test_size=0.3)


#---------5----------


zarobki = dane.groupby('Gender').agg(srednia=('EstimatedSalary','mean'))
zarobki.reset_index(inplace=True) 

plt.pie(zarobki["srednia"],labels= zarobki["Gender"])
plt.show()

zarobki_wiek = dane.groupby('Age').agg(srednia=('EstimatedSalary','mean'))
zarobki_wiek.reset_index(inplace=True)

plt.bar(zarobki["srednia"],zarobki["EstimatedSalary"])
plt.show()

