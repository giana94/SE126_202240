# Giana Hardin
# SE126_202240
# Lab5 individual
# 8/26/22

#Program Prompt:
#Re-write the Week #5 Class Lab but instead of searching for a person’s name, search for their birthday.  If the person is found, reprint their entire record to the console.  The program should allow the user to search for as many birthdays as they want. The program should also print a statement telling the user how many iterations of the search loop the program went through before finding (or not finding) the requested person.

#------------Variable Dictionary-----------------------------------------------------
#records            record count
#lName              last name index 0
#fName              first name index 1
#bday               date of birth index 2
#answer             input answer. start of while loop. answer == "y"
#search             input bday to be searched as string 
#search_count       search counter in loop. resets after each new search
#found              search found within record
#date_object        birthday index converted into datetime format
#cAge               imported 'todays' date formulated to find current age of person by birthday

#------------MAIN CODE------------------------------------------------------------------
import csv
from datetime import datetime

records = 0

lName = []
fName = []
bday = []


with open("C:/Users/ghard/Desktop/SE126_202240/week6/lab6_updated.txt") as csvfile:
    
    file = csv.reader(csvfile)

    for rec in file:

        records += 1

        lName.append(rec[0])
        fName.append(rec[1])
        bday.append(rec[2])

print("\n\n-----------------------------------------------------------------")
print("{0:12} \t {1:12}\t {2:15}  {3:7}".format("Index", "Last Name", "First Name", "Date of Birth"))
print("-----------------------------------------------------------------")

for i in range(0,records):
    print("Index: {0:2} \t {1:12}\t  {2:12} \t   {3:7}".format(i, lName[i].title(), fName[i].title(), bday[i]))

print("\n")

answer = "y"

while answer == "y":

    search_count = 0

    search = input("\nEnter the Date of Birth of the person you want to search for [MM/DD/YYYY]: ")
    found = []

    for i in range(0, records):

        search_count += 1

        if search == bday[i]:

            found.append(i)

    print("\n\n\t\tSEQUENTIAL SEARCH COMPLETE.")
    print("-----------------------------------------------------------------")

    if len(found) > 0:

        for i in range(0, len(found)):
            print("INDEX: {0} \t {1:10} \t {2:10} \t {3:10}".format(found[i], lName[found[i]], fName[found[i]], bday[found[i]]))
            date_object = datetime.strptime(bday[found[i]], '%m/%d/%Y').date() #this converts the 'bday' string into datetime formatting '%m/%d%y. 
            cAge = datetime.today().year - date_object.year - ((datetime.today().month, datetime.today().day) < (date_object.month, date_object.day)) #formual to calculate current age using imported todays date subtracted by the date of birth of searched record. " .today().year/month/day "
            print("\n\t\tCurrent Age: ",cAge)

    else:
        print("\n\t\tYour search for {} was NOT FOUND.".format(search))

    print("\n\nSearch Loop Iterations Performed: {}".format(search_count))

    answer = input("\n\n Would you like to search again? [y/n]: ").lower()

    while answer != "y" and answer != "n":
        print("**INVALID ENTRY**")
        answer = input("\n\n Would you like to search again? [y/n]: ").lower()
print("\n\n\n\t\t\tThank you, Byeeeeee!\n\n")