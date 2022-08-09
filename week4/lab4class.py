#The Python Pals
#Lab 4
# 08/08/2022
#SE126_202240

#PROGRAM PROMPT
#Write a program that reads the data file (below) and stores the data into lists (remember, one list for every field).  Once the lists are populated (and the file is "closed"), process the lists to reprint the file data, record by record as they originally appear in the file.
#Next, reprocess the lists to find each student's current average score along with the class average.  While processing in the for loop, store each student's average into a new list called 'avg' and reprint the records to include this numeric average.  Reprocess the lists one final time to find the letter equivalent of each student's average and store this into a new list called 'let_avg'.  Reprint the lists for a third and final time, record by record including average score and average letter equivalent.  After this third print, print to the console the total number of student's in the class along with the class numeric average.  

#VARIABLE DICTIONARY



#---------------------------MAIN PROGRAM------------------------------------------------------------------------------------------

import csv

students = 0
classAvg = 0

firstname = []
lastname = []
test1 = []
test2 = []
test3 = []
avg = []
letAvg = []

with open("C:/Users/ghard/Desktop/SE126_202240/week4/listPractice1.txt") as csvfile:

    file = csv.reader(csvfile)

    for rec in file:

        students += 1

        firstname.append(rec[0])
        lastname.append(rec[1])
        test1.append(int(rec[2]))
        test2.append(int(rec[3]))
        test3.append(int(rec[4]))


print("{0:13}\t {1:13}\t {2:5}\t {3:5}\t {4:5}\t\n".format("LASTNAME", "FIRSTNAME", "TEST 1", "TEST 2", "TEST 3"))  
print("----------------------------------------------------------")


for index in range(0, students):

    print("{0:13}\t {1:13}\t {2:5.2f}\t {3:5.2f}\t {4:5.2f}\t".format(lastname[index], firstname[index], test1[index], test2[index], test3[index]))

print("\n\n")
print("{0:13}\t {1:13}\t {2:5}\t {3:5}\t {4:5}\t {5:5}\t\n".format("LASTNAME", "FIRSTNAME", "TEST 1", "TEST 2", "TEST 3", "AVERAGE"))


for index in range(0, students):

    gradeAvg = (test1[index] + test2[index] + test3[index]) / 3
    avg.append(gradeAvg)

    print("{0:13}\t {1:13}\t {2:5.2f}\t {3:5.2f}\t {4:5.2f}\t {5:5.2f}\t".format(lastname[index], firstname[index], test1[index], test2[index], test3[index], avg[index]))

print("\n\n")
print("{0:13}\t {1:13}\t {2:5}\t {3:5}\t {4:5}\t {5:2}\t {6:5}\t\n".format("LASTNAME", "FIRSTNAME", "TEST 1", "TEST 2", "TEST 3", "AVERAGE", "LETTER AVG"))

for index in range(0, students):

    gradeAvg = (test1[index] + test2[index] + test3[index]) / 3
    avg.append(gradeAvg)

    classAvg += gradeAvg

    if avg[index] >= 90:
        let = "A"
        letAvg.append(let)
    elif avg[index] < 90 and avg[index] >= 80:
        let = "B"
        letAvg.append(let)
    elif avg[index] < 80 and avg[index] >= 70:
        let = "C"
        letAvg.append(let)
    elif avg[index] < 70 and avg[index] >= 60:
        let = "D"
        letAvg.append(let)
    else:
        let = "F"
        letAvg.append(let)

    print("{0:13}\t {1:13}\t {2:5.2f}\t {3:5.2f}\t {4:5.2f}\t {5:5.2f}\t\t {6:5}\t".format(lastname[index], firstname[index], test1[index], test2[index], test3[index], avg[index], letAvg[index]))

classAvg /= students

print("\n\n\tStudents in class: {}".format(students))
print("\tTotal class average: {}\n".format(classAvg))