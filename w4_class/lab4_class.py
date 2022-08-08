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


for index in range(0,records):

    num_average = (test_1[index] + test_2[index] + test_3[index]) / 3
    average.append((int(num_average)))
    ltr_grade = []


    if average[index] >= 90:
        grade = "A"
        ltr_grade.append(grade)
        

    if average[index] >= 80:
        grade = "B"
        ltr_grade.append(grade)
        

    if average[index] >= 70:
        grade = "C"
        ltr_grade.append(grade)

    if average[index] >= 60:
        grade = "D"
        ltr_grade.append(grade)

    else:
        grade = "F"
        ltr_grade.append(grade)

    print("{0:13} \t {1:13} \t {2} \t {3} \t {4} \t {5:7.2f} \t {6}".format(fName[index], lName[index], test_1[index], test_2[index], test_3[index], average[index], ltr_grade[index]))





print("\n\tTOTAL RECORDS PROCESSED:", records)