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







#--------------MAIN PROGRAM---------------------------
import csv

fName = []
lName = []
test_1 = []
test_2 = []
test_3 = []
average = []
num_average = []

records = 0


with open("C:/Users/ghard/Desktop/SE126_202240/w4_class/listPractice1.txt") as csvfile:
    
    file = csv.reader(csvfile)
    
    for rec in file:

        records += 1
        fName.append(rec[0])
        lName.append(rec[1])
        test_1.append(int(rec[2]))
        test_2.append(int(rec[3]))
        test_3.append(int(rec[4]))


    
    
    
    
    
    
    
    
#for i in range(0,records):

    #num_average = (test_1[i] + test_2[i] + test_3[i]) / 3
    #average.append((int(num_average)))
    #ltr_grade = []


    #print("{0:13} \t {1:13} \t {2} \t {3} \t {4} \t {5:7.2f} \t {6}".format(fName[i], lName[i], test_1[i], test_2[i], test_3[i], average[i], ltr_grade[i]))





print("\n\tTOTAL RECORDS PROCESSED:", records)