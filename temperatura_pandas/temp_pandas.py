#1
import pandas as pd

#2
dane = pd.read_csv('temperature.csv', sep=";")
#print(dane.to_string())

#3
il = len(dane)
print(f"Ilosc rekordow w obiekcie df wynosi: {il}")

#4
print(dane[:100].to_string())

#5
print(dane.tail(100).to_string())

#6
print(dane[["Country", "City"]])

#7
print(dane["AverageTemperatureFahr"][dane["Country"]=="Poland"])

#8
print(dane["AverageTemperatureFahr"][dane["City"]=="Wroclaw"][dane["year"] >= 1900][dane["year"] <= 1999])

#9
print(dane["AverageTemperatureFahr"][dane["City"]=="Warsaw"][dane["month"]==1].mean())

#10
print(dane["AverageTemperatureFahr"][dane["Country"]=="Poland"].min())
print(dane["AverageTemperatureFahr"][dane["Country"]=="Poland"].max())

#11
dane.rename(columns={'AverageTemperatureFahr':'AvgTmpF'}, inplace=True) #zmiana nazwy w oryginale
dane.rename(columns={'AverageTemperatureUncertaintyFahr':'AvgTmpUnF'}, inplace=True)

def F2C(tmp):
    return 5*(tmp-32)/9

#towrzymy nowa kolumne z C
dane["AvgTmpC"] = dane["AvgTmpF"].map(F2C)
dane["AvgTmpUnC"] = dane["AvgTmpUnF"].map(F2C)

dane2 = dane[["City", "AvgTmpC", "year"]]

print(dane)
print(dane2)

#usuwanie kolumny
del dane["AvgTmpUnF"] 

#
def Latitude(lat):
    if lat[-1] == 'N':
        return float(lat[:-1])
    elif lat[-1] == 'S':
        return -float(lat[:-1])
    else:
        return 0.0
dane['Latitude'] = dane['Latitude'].map(Latitude)

def Longitude(lon):
    if lon[-1] == "E":
        return float(lon[:-1])
    elif lon[-1] == "S":
        return -float(lon[:-1])

  
