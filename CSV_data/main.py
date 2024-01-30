# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#
#     temperatures = []
#
#     for row in data:
#         temp = row[1]
#         if temp != "temp":
#             temperatures.append(int(temp))
#     print(temperatures)

import pandas as pd

data = pd.read_csv("weather_data.csv")
#print(data)
r=data[data["temp"]=="Monday"]

print(r[1])
