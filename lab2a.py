import csv
from unicodedata import name
total_records = 0 
total_people = 0

with open("C:/Users/ghard/Desktop/SE126_202240/w2_classLab/lab2a.csv") as csvfile: 

    file = csv.reader(csvfile)

    for rec in file:
        total_records += 1

        name = rec[0]
        maxCap = int(rec[1])
        attendees = int(rec[2])

        total_records += attendees

        print("{0:10}| \t{1:2}| \t{2:7.2f}| ".format(name, maxCap, attendees))

print("TOTAL RECORDS IN FILE: {0}".format(total_records))
print("TOTAL of ATTENDEES: {0:.2f}".format(attendees))
