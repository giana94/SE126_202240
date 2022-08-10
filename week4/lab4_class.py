#The Python Pals
#Lab 4 (class lab)
#08/15/2022
#SE126_202240

#PROGRAM PROMPT --- Write a program that reads the data file (below) and stores the data into lists (remember, one list for every field).  Once the lists are populated (and the file is "closed"), process the lists to reprint the file data, record by record as they originally appear in the file.
#Original File Headers
#FIELD0             FIELD1            FIELD2       FIELD3        FIELD4     
#Lastname          Firstname        Test1         Test2             Test3
#Next, reprocess the lists to find each student's current average score along with the class average.  While processing in the for loop, store each student's average into a new list called 'avg' and reprint the records to include this numeric average.  Reprocess the lists one final time to find the letter equivalent of each student's average and store this into a new list called 'let_avg'.  Reprint the lists for a third and final time, record by record including average score and average letter equivalent.  After this third print, print to the console the total number of student's in the class along with the class numeric average.  
#Final Print Headers
#FIELD0             FIELD1            FIELD2       FIELD3        FIELD4     FIELD5        FIELD6
#Lastname          Firstname        Test1         Test2             Test3       Num Avg    Letter Avg

#----------VARIABLE DICTIONARY------------------------
#records            student counter
#classAvg           class average counter for equation
#lName              index[0]
#fName              index[1]
#test_1             index[2]
#test_2             index[3]
#test_3             index[4]
#avg                additional index[5]
#gradeAvg           individual number grade
#let_avg            individual letter grade index[6]
#grade              assigned letter grade

#--------------------------------MAIN PROGRAM---------------------------

#import the csv file
import csv

records = 0
classAvg = 0
#assign headers to index
fName = []
lName = []
test_1 = []
test_2 = []
test_3 = []
avg = []
gradeAvg = []
let_avg = []


with open("C:/Users/008018155/Desktop/SE126_202240/week4/listPractice1.txt") as csvfile:
    
    file = csv.reader(csvfile)
    
    for rec in file:
        records += 1
        
        #last name first
        lName.append(rec[1])
        fName.append(rec[0])
        test_1.append(int(rec[2]))
        test_2.append(int(rec[3]))
        test_3.append(int(rec[4]))

#FORMATTING
print("\n\n\t-------------------ORIGINAL FILE DATA------------------------")
print("\t{0:13} \t {1:13} \t {2:9} {3:9} {4:9}".format("Last Name","First Name","Test 1","Test 2","Test 3"))
print("\t-------------------------------------------------------------")

for index in range(0,records):
    
    #orginal data from file
    print("\t{0:13}\t {1:13} \t {2:7.2f}  {3:7.2f}   {4:7.2f}".format(lName[index],fName[index],test_1[index],test_2[index], test_3[index]))

#More formatting headers
print("\t-------------------------------------------------------------")
print("\n\n\t-------------------------INDIVIDUAL AVERAGES---------------------------")
print("\t{0:13} \t {1:13} \t {2:9} {3:9} {4:9} {5:9}".format("Last Name","First Name","Test 1","Test 2","Test 3","Num Avg"))
print("\t-----------------------------------------------------------------------")

#Adding new index for individual number averages
for index in range(0,records):
    gradeAvg = (test_1[index] + test_2[index] + test_3[index]) / 3
    avg.append(gradeAvg)
    
    classAvg += gradeAvg
    
    print("\t{0:13}\t {1:13} \t {2:7.2f}  {3:7.2f}   {4:7.2f}   {5:7.2f}".format(lName[index],fName[index],test_1[index],test_2[index], test_3[index],avg[index]))
    
print("\t------------------------------------------------------------------------")



print("\n\n\t-----------------------------------GRADE AVERAGES-----------------------------------")
print("\t{0:13} \t {1:13} \t {2:9} {3:9} {4:9} {5:9} {6:13}".format("Last Name","First Name","Test 1","Test 2","Test 3","Num Avg","Letter Avg"))
print("\t------------------------------------------------------------------------------------")

for index in range(0,records):
    
    #assign letter grades for number grades per student
    if avg[index] >= 90:
        grade = "A"
        let_avg.append(grade)
        
    if avg[index] >= 80 and avg[index] < 90:
        grade = "B"
        let_avg.append(grade)
    
    if avg[index] >= 70 and avg[index] < 80:
        grade = "C"
        let_avg.append(grade)
    
    if avg[index] >= 60 and avg[index] < 70:
        grade = "D"
        let_avg.append(grade)
    
    elif avg[index] < 60:
        grade = "F"
        let_avg.append(grade)

    #last print of record
    print("\t{0:13}\t {1:13} \t {2:7.2f}  {3:7.2f}   {4:7.2f}   {5:7.2f}\t    {6}".format(lName[index],fName[index],test_1[index],test_2[index], test_3[index],avg[index],let_avg[index]))

#class average equation
classAvg = classAvg / records


print("\n\n\t\tTOTAL STUDENTS PROCESSED:", records)
print("\t\t\t   CLASS AVERAGE:",classAvg,"\n\n")