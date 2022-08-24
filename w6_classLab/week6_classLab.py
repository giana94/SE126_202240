# The Python Pals
#SE126_202240
#08/23/22
#Class Lab 6

#----VARIABLE DICTIONARY--------




##------------*******HEY!!!! DONT FORGET ABOUT ME!!!!!******-------------------------





#-----PROGRAM PROMPT--------------
#Write a Python program that reads the data from the file and stores all data into appropriate lists. The program should then prompt the user for the person’s last name they are searching for and display all available information on that person if they are found.  You must use the sequential search.  The program should allow the user to search for as many people as they want. The program should also print a statement telling the user how many iterations of the search loop the program went through before finding (or not finding) the requested person.

#----------------------------------------------------------------------------------------


import csv

records = 0
search_count = 0

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
print("\n\n---------------------------------------------------")
print("{0:12}\t {1:15}  {2:7}".format("Last Name", "First Name", "Date of Birth"))
print("---------------------------------------------------")

for i in range(0,records):
    print("{0:12}\t  {1:12} \t   {2:7}".format(lName[i], fName[i], bday[i]))
    
    
answer = "y"
while answer == "y":
    
    search = input("\n\nEnter the FULL LAST NAME of the record you are looking for: ")
    found = -1 
    
    for i in range(0, records):
        search_count += 1
        if search == lName[i]:
            found = i
            print("We have FOUND ", search, " at INDEX: ", i)
            print("\t{1:12}\t  {2:12} \t   {3:7}".format(i, lName[i], fName[i], bday[i]))
            
    if found > 0:
        if search == lName[i]:
            found = i
            print("\t{1:12}\t  {2:12} \t   {3:7}".format(i, lName[i], fName[i], bday[i]))
        
    else:
        print("Your search for ", search, " has NOT BEEN FOUND.")
        print("Please check Your spelling and try again!")
    print("\n\nLOOPS PERFORMED FOR THIS SEARCH: ", search_count)
    
    
    search_count = 0 #resets the counter for the next search
    answer = input("\n\n Would you like to search again? [y/n]: ")
    
    answer = answer.lower() #finds lowercase equivalent of object before '.'
    while answer != "y" and answer != "n":
        print("**INVALID ENTRY**")
        answer = input("\n\n Would you like to search again? [y/n]: ")
    
        answer = answer.lower() #finds lowercase equivalent of object before '.'
print("\n\n\nThank you for using our program! Bye!\n\n")