#1
import pandas as pd

#2
dane = pd.read_csv('temperature.csv', sep=";")
print(dane.to_string())

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