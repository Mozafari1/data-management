import csv
inFile = open('./network_info/network_info.csv', 'r', encoding="utf-8")

outFile = open('./network_info/network_info2.csv', 'w', encoding="utf-8")

listLines = []

for line in inFile:

    if line in listLines:
        continue

    else:
        outFile.write(line)
        listLines.append(line)

outFile.close()

inFile.close()
