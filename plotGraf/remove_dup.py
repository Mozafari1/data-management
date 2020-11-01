import csv
inFile = open('list.csv', 'r', encoding="utf-8")

outFile = open('list2.csv', 'w', encoding="utf-8")

listLines = []

for line in inFile:

    if line in listLines:
        continue

    else:
        outFile.write(line)
        listLines.append(line)

outFile.close()

inFile.close()
