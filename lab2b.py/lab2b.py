#Giana Hardin
#Lab 2B
# 08/01/2022
#Program Prompt - You have been asked to produce a report that lists all the computers in the csv file lab2b.csv. Your report should look like the following sample output.  The last line should print the number of computers in the file.

#VARIABLE DICTIONARY
#records            csv file "../se126_202240/lab2b.csv"
#type_              column 1
#manu               column 2
#cpu                column 3
#ram                column 4
#first_disk         column 5
#num_disks          column 6
#second_disk        column 7
#os                 column 8
#year               column 9

#---------MAIN PROGRAM----------------------------------------------------

import csv

records = 0

#header
print("\nDATA FROM FILE----------------------------------------------------------------------\n")
print("{0:10} {1:9} {2:8} {3:8} {4:11} {5:13} {6:11} {7:8} {8:8}".format(" TYPE", "BRAND", "CPU", "RAM", "DISK 1", "NUM DISKS", "DISK 2", "OS", "YEAR"))
print("---------------------------------------------------------------------------------------------")


with open("C:/Users/ghard/Desktop/SE126_202240/lab2b.py/lab2b.csv") as csvfile:

    file = csv.reader(csvfile)

    for rec in file: #one record at a time 
        #entire code block applies to ONE record..... at a time

        records += 1

        type_ = rec[0]
        manu = rec[1]
        cpu = rec[2]
        ram = rec[3]
        first_disk = rec[4]
        num_disks = rec[5]

        #fields below change per year
        second_disk = ""
        os = ""
        year = ""
        

        if type_ =="D":
            type_ = "Desktop"

        elif type_ == "L":
            type_ = "Laptop"

        else:
            #error in file check 
            point = records - 1
            type_ = "ERROR @ record " + str(point)




        if num_disks == "1":
            #no second disk
            os = rec[6]
            year = rec[7]
            second_disk = " ---"
            
        elif num_disks == "2":
            second_disk = rec[6]
            os = rec[7]
            year = rec[8]
            
            

            


        print("{0:12} {1:7} {2:8} {3:8} {4:14} {5:10} {6:11} {7:9} {8:5}".format(type_, manu, cpu, ram, first_disk, num_disks, second_disk, os, year))

print("\nNumber of computers in File:  {0}\n\n".format(records))