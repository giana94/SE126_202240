#Class Lab Week 5
#Python Pals

#Program Prompt: Python program that reads the data from the file and stores all data into appropriate lists. The program should then prompt the user for the person’s last name they are searching for and display all available information on that person if they are found.  You must use the sequential search.  The program should allow the user to search for as many people as they want. The program should also print a statement telling the user how many iterations of the search loop the program went through before finding (or not finding) the requested person.

#Variable Dictionary:

#MAIN CODE---------------------------------------------------------------------------------------------------------------

import csv

records = 0

lName = []
fName = []
bday = []

with open("C:/Users/ghard/Desktop/SE126_202240/w6_classLab/lab5_updated.txt") as csvfile:
    
    file = csv.reader(csvfile)

    for rec in file:

        records += 1

        lName.append(rec[0])
        fName.append(rec[1])
        bday.append(rec[2])

#print("Finished processing file. There are {} records.".format(records))

print("\n\n-----------------------------------------------------------------")
print("{0:12} \t {1:12}\t {2:15}  {3:7}".format("Index", "Last Name", "First Name", "Date of Birth"))
print("-----------------------------------------------------------------")

for i in range(0,records):
    print("Index: {0:2} \t {1:12}\t  {2:12} \t   {3:7}".format(i, lName[i].title(), fName[i].title(), bday[i]))

print("\n")

answer = "y"

while answer == "y":

    search_count = 0

    search = input("\nEnter the full LAST NAME of the person you want to search for: ").title()
    found = []

    for i in range(0, records):

        search_count += 1

        if search == lName[i]:

            found.append(i)

    print("\n\n\t\tSEQUENTIAL SEARCH COMPLETE.")
    print("-----------------------------------------------------------------")
    
    if len(found) > 0:
        for i in range(0, len(found)):
            #print("\nWe have FOUND ", search, " at INDEX: {}".format(found))
            print("INDEX: {0} \t {1:10} \t {2:10} \t {3:10}".format(found[i], lName[found[i]], fName[found[i]], bday[found[i]]))

    else:
        print("\n\t\tYour search for {} was NOT FOUND.".format(search))

    print("\n\nSearch Loop Iterations Performed: {}".format(search_count))

    answer = input("\n\n Would you like to search again? [y/n]: ").lower()

    while answer != "y" and answer != "n":
        print("**INVALID ENTRY**")
        answer = input("\n\n Would you like to search again? [y/n]: ").lower()
print("\n\n\n\t\t\tThank you, Byeeeeee!\n\n")
