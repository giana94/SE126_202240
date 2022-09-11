#Giana Hardin
#SE126_202240
#Lab 7 Individual
#9/12/22

#-----------PROGRAM PROMPT-----------
#7. Write a program that gives the user a menu of options to search through the file. 

#Depending on how the user wants to search, you may need to sort the searched-through list before performing Binary Search.  Binary Search should be used for Menu Options 1 (First Name) and 2 (ID codes)  and the full record for the individual searched should be included if found (the user should be alerted if the person cannot be found).  If the user chooses options 3 or 4, you must print a list of everyone and their full record that fits the searched item (think: sequential search!) that has that Last Name or Allegiance.  Use the GOT_bubble_sort_7.txt file (you may change the name if you wish but you may NOT edit the text file outside of checking for and deleting empty end records).  The user should be able to search as many times as they would like.  If the user enters an option that does not exist, the program must tell them this before asking if the user would like to search for a new record


#-----------VARIABLE DICTIONARY-----------
def menu():
    print("\tSEARCH MENU\n")
    print("1.	Search by FIRST NAME")
    print("2.	Search by ID CODE")
    print("3.	Search by LAST NAME")
    print("4.	Search by ALLEGIANCE")
    print("5.	EXIT")
    
    choice = int(input("Please enter your selection [1 - 5]: "))
    
    while choice < 0 or choice > 5:
        
        print("**ERROR!**")
        choice = int(input("Please enter your selection [1 - 5]: "))

    return choice

def again():
    answer = input("\nWould you like to search again? [y/n]----------: ").lower()
    while answer != "n" and answer != "y":
        print("\t\t **ERROR** Invalid Entry")
        answer = input("\nWould you like to search again? [y/n]: ").lower()
    return answer

def bye():
    print("okayyyy byeeeeeeee")
    

def bubble():
    #BUBBLE SORT - REQUIRED for BINARY SEARCH! MUST HAPPEN FIRST :]
    
        for i in range(0, records - 1):#outter loop

            print("OUTER LOOP! i = ", i)


            for index in range(0, records - 1):#inner loop

                print("\t INNER LOOP! k = ", index)

                #below if statement determines the sort

                #list used is the list being sorted

                # > is for increasing order, < for decreasing

                if(fName[index] > fName[index + 1]):

                    print("\t\t SWAP! ", fName[index], "<-->", fName[index + 1])

                    #if above is true, swap places!

                    temp = fName[index]
                    fName[index] = fName[index + 1]
                    fName[index + 1] = temp

                    #swap all other values

                    temp = age[index]
                    age[index] = age[index + 1]
                    age[index + 1] = temp
                    
                    temp = idCode[index]
                    idCode[index] = idCode[index +1]
                    idCode[index + 1] = temp

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
    print("\n\n{0:20} {1:15} {2:17} {3:10} {4}".format("ID Code", "Last Name", "First Name", "Age", "Allegience"))
    print("--------------------------------------------------------------------------------\n")

for i in range(0,records):
    print("{0:20} {1:15} {2:17} {3:10} {4}".format(idCode[i].title(), lName[i].title(), fName[i].title(), age[i], allegience[i].title()))
print("\n")



answer = "y"

while answer == "y":
    choice = menu()

    while choice != 5:
        
        if choice == 1:
            print("first name")
            bubble()
            search = input("Enter the FIRST NAME of the person/people you are looking for: ")

            min = 0                         #this is the lowerst starting INDEX
            max = records -1                #the highest starting INDEX
            guess = int((min + max) / 2) #or: guess = (min + max) // 2 -> starting MIDDLE index

            while min < max and search != fName[guess]:

                if search < fName[guess]:   #this is for ASCENDING ORDER LISTS   " > " for descending

                    max = guess - 1

                else:
                    min = guess + 1

                guess = int((min + max) / 2)
                
            if search == fName[guess]:

                print("\t\tYour BINARY SEARCH results for ", search, ": ")
                
                print("{0:20} {1:15} {2:17} {3:10} {4}".format(idCode[guess].title(), lName[guess].title(), fName[guess].title(), age[guess], allegience[guess].title()))
                answer = again()

            elif search != fName[guess]:
                print("\t\tYour BINARY SEARCH results for ", search, ": could NOT BE FOUND. ")
                print("Please check your spelling and try again :]")


        if choice == 2:
            print("id code")
            bubble()
            search = input("Enter an ID Code: ")

            min = 0                         #this is the lowerst starting INDEX
            max = records -1                #the highest starting INDEX
            guess = int((min + max) / 2) #or: guess = (min + max) // 2 -> starting MIDDLE index

            while min < max and search != idCode[guess]:

                if search < idCode[guess]:   #this is for ASCENDING ORDER LISTS   " > " for descending
                    max = guess - 1

                else:
                    min = guess + 1

                guess = int((min + max) / 2)
            
            if search == idCode[guess]:
                print("\t\tYour BINARY SEARCH results for ", search, ": ")
                
                print("{0:20} {1:15} {2:17} {3:10} {4}".format(idCode[guess].title(), lName[guess].title(), fName[guess].title(), age[guess], allegience[guess].title()))

            else:
                print("\t\tYour BINARY SEARCH results for ", search, ": could NOT BE FOUND. ")
                print("Please check your spelling and try again :]")


        if choice == 3:
            
            search_count = 0
            
            search = input("\nEnter the full LAST NAME of the person you want to search for: ")
            found = []

            for i in range(0, records):
                search_count += 1

                if search == lName[i]:
                    found.append(i)

            print("\n\n\t\tSEQUENTIAL SEARCH COMPLETE.")
            print("-----------------------------------------------------------------")
            
            if len(found) > 0:
                for i in range(0, len(found)):
                    print("{0}\t{1:15} {2:17} {3:17} {4:5} {5}".format(found[i], idCode[found[i]].title(), lName[found[i]].title(), fName[found[i]].title(), age[found[i]], allegience[found[i]].title()))
            else:
                print("\n\t\tYour search for {} was NOT FOUND.".format(search))

            print("\n\nSearch Loop Iterations Performed: {}".format(search_count))

        if choice == 4:

            search_count = 0
            
            search = input("\nEnter the Allegience you are searching for: ").lower()
            found = []

            for i in range(0, records):
                search_count += 1

                if search == allegience[i]:
                    found.append(i)

            print("\n\n\t\tSEQUENTIAL SEARCH COMPLETE.")
            print("-----------------------------------------------------------------")
            
            if len(found) > 0:
                for i in range(0, len(found)):
                    print("{0}\t{1:15} {2:17} {3:17} {4:5} {5}".format(found[i], idCode[found[i]].title(), lName[found[i]].title(), fName[found[i]].title(), age[found[i]], allegience[found[i]].title()))
            else:
                print("\n\t\tYour search for {} was NOT FOUND. Please check your spelling!".format(search))

            print("\n\nSearch Loop Iterations Performed: {}".format(search_count))      
        
    answer = again()
bye()

