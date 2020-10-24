import pandas as pd
import numpy as np
import seaborn as sns

test = pd.read_csv("merged-location.csv")
print(test.head())

test.head(6565).to_csv("test_ip.csv")
dd = pd.read_csv("test_ip.csv")
print(dd.head())
data = open("location.csv", "w", encoding="utf-8")
with open("original.csv", encoding="utf-8") as file:
    next(file)
    for f in file:
        lines = f.split(',')
        with open("test_ip.csv", encoding="utf-8") as test:
            next(test)
            for t in test:
                columns = t.split(',')
                if lines[7] == columns[1]:
                    #
                    data.write(lines[0]+","+lines[1]+","+lines[2]+","+lines[3]+","+lines[4]+","+lines[5]+","+lines[6] +
                               ","+columns[1]+","+columns[2]+"," +
                               columns[3]+","+columns[4]+","+columns[5]
                               + ","+columns[6]+","+columns[7]+"," +
                               columns[8]+","+columns[9]+","+columns[10]
                               + ","+columns[11]+","+columns[12]+"," +
                               columns[13]+","+columns[14]+","+columns[15]
                               + ","+columns[16]+","+columns[17]+"," +
                               columns[18]+","+columns[19]+","+columns[20]
                               + ","+columns[21]+","+columns[22]+"," +
                               columns[23]+","+columns[24]+","+columns[25]
                               + ","+columns[26])
