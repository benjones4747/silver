import csv

with open('lib\pollster-ratings.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter = ',')
    names = []
    ppms = []
    for row in readCSV:
        name = row[1]
        ppm = row[10]

        names.append(name)
        ppms.append(ppm)

    print(names)
    print(ppms)
