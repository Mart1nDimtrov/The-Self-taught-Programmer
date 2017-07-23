import csv

with open("countriesoftheworld.csv", "rt") as csvfile:
    spamreader = csv.reader(csvfile)
    for row in spamreader:
        print("Hello " + row[0] + "!")
    
