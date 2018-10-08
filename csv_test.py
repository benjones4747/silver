import csv
import os

os.getcwd()



def ppmprocess(ppm):
    ppmprocessed = 10 - (((ppm)+1.4)*(10/4.2))
    return ppmprocessed

with open( ' lib\pollster-ratings.csv ' ) as csvfile:
    reader = csv.reader ( csvfile, delimiter = ' , ' )
    for row in reader:
        weightdesc = "Pollster Weighting"
        if row[ 0 ] == "Pollster":
            row.append(weightdesc)
        else:
            predictiveplusminus = row [ 7 ]
            weight = ppmprocess(predictiveplusminus)
            row.append(weight)
print("done")
