import csv

#create empty lists
lastname = []
firstname = []
test1 = []
test2 = []
test3 = []

#hand populate lists
teacher = ["KT","KT","KT","KT","KT","KT","KT","KT","KT","KT","KT","KT","KT","KT","KT","KT","KT","KT","KT","KT"]

for i in range(0, len(teacher)):
    print(teacher[i])


records = 0

with open("C:/Users/008018155/Desktop/SE126_202240/week4/listPractice1.txt") as csvfile:

    file = csv.reader(csvfile)

    for rec in file:

        print("ROW# {}, {}".format(records + 1, rec))
        records += 1

        lastname.append(rec[0])
        firstname.append(rec[1])
        test1.append(int(rec[2]))
        test2.append(int(rec[3]))
        test3.append(int(rec[4]))

print("Records in file: {}".format(records))

print("\n\n{:10}\t{:10}\t{}\t{}\t{}".format("FIRST", "LAST", "T#1", "T#2", "T#3"))
print("---------------------------------------------------------------------")

for i in range(0, records):

    print("{:10}\t{:10}\t{}\t{}\t{}".format(firstname[i], lastname[i], test1[i], test2[i], test3[i]))

className = []
stars= []
for i in range(0, records):

    className.append("C++")

    star_add = ""

    if test1[i] >= 85:
        star_add += "*"

    if test2[i] >= 85:
        star_add += "*"

    if test3[i] >= 85:
        star_add += "*"

    stars.append(star_add)


print("\n\n{:10}\t{:10}\t{}\t{}\t{}".format("FIRST", "LAST", "T#1", "T#2", "T#3"))
print("---------------------------------------------------------------------")

for i in range(0, records):

    print("CLASS: {}\t{:10}\t{:10}\t{}\t{}\t{}\t{}".format(className[i], firstname[i], lastname[i], test1[i], test2[i], test3[i],stars[i]))
