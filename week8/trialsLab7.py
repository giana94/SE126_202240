def menu():
    print("\tSEARCH MENU\n")
    print("1.	Search by FIRST NAME")
    print("2.	Search by ID CODE")
    print("3.	Search by LAST NAME")
    print("4.	Search by ALLEGIANCE")
    print("5.	EXIT")
    
    choice = int(input("Please enter your selection[1 - 5]: "))
    
    while choice < 0 or choice > 5:
        
        print("**ERROR!**")
        choice = int(input("Please enter your selection [1 - 5]: "))

    return choice

def again():
    answer = input("\nWould you like to search again? [y/n]: ").lower()
    while answer != "n" and answer != "y":
        print("\t\t **ERROR** Invalid Entry")
        answer = input("\nWould you like to search again? [y/n]: ").lower()
    return answer


                


#-----------MAIN PROGRAM-----------
import os
import csv
records = 0

idCode = []
lName = []
fName = []
age = []
allegience = []


with open("C:/Users/ghard/Desktop/SE126_202240/week8/GOT_bubble_sort_7.txt") as csvfile:
    file = csv.reader(csvfile)

    for rec in file:

        records += 1
        idCode.append(rec[0].lower())
        lName.append(rec[1].lower())
        fName.append(rec[2].lower())
        age.append(rec[3])
        allegience.append(rec[4].lower())

    print("\nrecords in file: ",records)
    print("\n\n{0:15} {1:15} {2:15} {3:5} {4}".format("ID Code", "Last Name", "First Name", "Age", "Allegience"))
    print("--------------------------------------------------------------------------------\n")

for i in range(0,records):
    print("{0:15} {1:15} {2:15} {3:5} {4}".format(idCode[i].title(), lName[i].title(), fName[i].title(), age[i], allegience[i].title()))
print("\n")


answer = "y"
choice = menu()

while answer == "y":
    
    while choice != 5:
        if choice == 1:
            print("id stufffffffff")
    answer = again()
            
print("okayyyy byeeeeeeee")