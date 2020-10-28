import pandas as pd
import numpy as np
import seaborn as sns

test = pd.read_csv("./network_info/network_info.csv")
# print(test.head())

test.head(71825).to_csv("./network_info/asn_num.csv")
dd = pd.read_csv("./network_info/asn_num.csv")

# print(dd.head())

data = open("asn_final.csv", "w", encoding="utf-8")
with open("./network_info/asn.csv", encoding="utf-8") as file:
    next(file)
    for f in file:
        lines = f.split(',')
        with open("./network_info/asn_num.csv", encoding="utf-8") as test:
            next(test)
            for t in test:
                columns = t.split(',')
                if lines[1] == columns[5]:

                    data.write(columns[1]+"," + columns[2]+"," +
                               columns[3]+"," + columns[4]+"," + lines[0]+"," + columns[6])
