# Giana Hardin
# SE126_202240
# Lab6 individual
# 09/01/22

#---------PROGRAM PROMPT-----------------
#Write a Python program that reads the data from the file and stores all data into appropriate lists. The program should then prompt the user for the person’s last name they are searching for and display all available information on that person if they are found.  ***You must use the binary search method***.  The program should allow the user to search for as many people as they want. The program should also print a statement telling the user how many iterations of the search loop the program went through before finding (or not finding) the requested person.

#---------VARIABLE DICTIONARY-----------------
#lName              index[0] Last Name
#fName              index[1] First Name
#dob                index[2] Date of Birth
#records            records count
#binary_loop        binary loop count
#min                lowest starting index
#max                hightest starting index
#guess              starting middle index of binary search
#search             user input for Last Name
#---------MAIN PROGRAM-----------------

import csv

lName = []
fName = []
dob = []

records = 0

with open("C:/Users/ghard/Desktop/SE126_202240/week7/lab6A.txt") as csvfile:
    file = csv.reader(csvfile)

    for rec in file:
        records += 1
        lName.append(rec[0].lower())
        fName.append(rec[1].lower())
        dob.append(rec[2])

print("\n\nFile processed. There are {} records.".format(records))
print("-----------------------------------------------------------------")
print("{0:12} \t{1:12}\t {2:15}  {3:7}".format("Index", "Last Name", "First Name", "Date of Birth"))
print("-----------------------------------------------------------------")

for i in range(0,records):
    print("Index: {0:2} \t {1:12}\t  {2:12} \t   {3:7}".format(i + 1, lName[i].title(), fName[i].title(), dob[i]))

answer = "y"

while answer == "y":
    #use starting values inside loop to reset Binary count!!
    binary_loop = 0
    min = 0
    max = records - 1  
    guess = int((min + max) / 2)

    search = input("\n\nEnter the LAST NAME of the record you are looking for: ").lower()

    while (min < max and search != lName[guess]):  # Less than < used for lists in Ascending order! This loop splits record in half everytime until search is found

        binary_loop += 1

        if search < lName[guess]:
            max = guess - 1

        else:
            min = guess + 1

        guess = int((min + max) / 2)

    if search == lName[guess]: 
        print("\n\nLast name {} was Found at index: {}".format(search.upper(), (guess + 1)))
        print("\n\t {1:12}\t  {2:12} \t   {3:7}".format(guess, lName[guess].title(), fName[guess].title(), dob[guess]))

    else:
        print("\n\nYour search for ", search.upper(), " Has Not been Found. \n Check your spelling and try again!")

    print("\nBINARY SEARCH LOOPS PERFORMED: {} ".format(binary_loop))
    answer = input("\n\n\tWould you like to search another Record? [y/n]: ").lower()
    while answer != "n" and answer != "y":
        print("\t\t **ERROR** Sorry Invalid Entry")
        answer = input("\nWould you like to search another Record? [y/n]: ").lower()


print("\n\n\t\t\tHave a great day!!! :) \n\n\n")



