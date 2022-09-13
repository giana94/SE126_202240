#Lab 7 
# Erick Cordon


#Prompt: Write a program that gives the user a menu of options to search through the file.

#varriable Def():
#idP = [] id list
#lname= [] last name list
#fname = [] first name list
#age = [] age list
#allegiance = [] allegiance list

#records = 0 records counter

#sort = bubble() calls in the bubble sort function

#min = 0 #this is the lowest starting index
#max = records -1 #this is the highest starting index
#guess = int((min + max) // 2) #this is the middle point of the index

#found = [] found list used to store index of searched person
#f = - 1 lowest index minus start


#Function Def():
import csv #allows pything to view csv files

from os import system, name 

from time import sleep 

def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')
    # for mac 
    else:
        _ = system('clear')

def menu():

    print("SEARCH MENU")
    print("1. Search by FIRST NAME")
    print("2. Search by ID CODE")
    print("3. Search by LAST NAME")
    print("4. Search by ALLEGIANCE")
    print("5. Exit")

    pick = input("Hello, Please make a selection from the following below [1-5]: ")

    while pick != "1" and pick != "2" and pick != "3" and pick !="4" and pick != "5":
        print("\nSorry...An invalid input was made. Please try again")

        pick = input("Hello, Please make a selection friom the following below [1-5]: ")

    return pick

def bubble():
    
    for i in range(0, records - 1):#outter loop

        for index in range(0, records - 1):#inner loop

            if(fname[index] > fname[index + 1]):

                #if above is true, swap places!

                temp = fname[index]

                fname[index] = fname[index + 1]

                fname[index + 1] = temp


                #swap all other values

                temp = age[index]

                age[index] = age[index + 1]

                age[index + 1] = temp

                temp = idP[index]
                idP[index] = idP[index + 1]
                idP[index + 1] = temp

                temp = lname[index]
                lname[index] = lname[index + 1]
                lname[index + 1] = temp

                temp = allegiance[index]
                allegiance[index] = allegiance[index + 1]
                allegiance[index + 1] = temp

def idbubble():

    for i in range(0, records - 1):#outter loop

        for index in range(0, records - 1):#inner loop

            if(idP[index] > idP[index + 1]):

                #if above is true, swap places!

                temp = fname[index]

                fname[index] = fname[index + 1]

                fname[index + 1] = temp


                #swap all other values

                temp = age[index]

                age[index] = age[index + 1]

                age[index + 1] = temp

                temp = idP[index]
                idP[index] = idP[index + 1]
                idP[index + 1] = temp

                temp = lname[index]
                lname[index] = lname[index + 1]
                lname[index + 1] = temp

                temp = allegiance[index]
                allegiance[index] = allegiance[index + 1]
                allegiance[index + 1] = temp

def again():

    answer = input("\nWould you like to add another search? [y/n]: ").lower()

    while answer != "y" and answer != "n":
        print("\nSorry wrong input")

        answer = input("Would you like to add another search? [y/n]: ").lower()

    return answer

def goodbye():

    print("\nThank you for using our program")
    print("\n\t\tThe Lannisters send their regards.")

#Main Code Below ------------------------------------------------------------------------------------------

idP = []
lname= []
fname = []
age = []
allegiance = []

records = 0

with open("C:/Users/ghard/Desktop/SE126_202240/week8/GOT_bubble_sort_7.txt") as csvfile:

    csv_reader = csv.reader(csvfile)

    for rec in csv_reader:

        records += 1

        idP.append(rec[0].lower())
        lname.append(rec[1].lower())
        fname.append(rec[2].lower())
        age.append(rec[3])
        allegiance.append(rec[4].lower())

print("------------------------------------------------------------------------------------------------------------------")

print("Index: {0}\t{1:15}\t{2:15}\t{3:15}\t{4:10}\t{5:15}".format("Num","ID Code","Last Name","First Name","Age","Allegiance"))

print("------------------------------------------------------------------------------------------------------------------")

for i in range(0,records):
    print("Index: {0}\t{1:15}\t{2:15}\t{3:15}\t{4:10}\t{5:15}".format(i,idP[i].title(),lname[i].title(),fname[i].title(),age[i],allegiance[i].title()))


answer = "y"

while answer == "y":

    print("\n\n")

    choice = menu() #calls the menu

    clear() #calls the clear screen function

    if choice == "1": # search based off of First name

        print("\nYou've selected search FIRST NAME")
        
        sort = bubble() #calls the bubble sort function

        search = input("Please enter the FIRST NAME of the person you are looking for: ").lower()

        min = 0 #this is the lowest starting index
        max = records -1 #this is the highest starting index
        guess = int((min + max) // 2) #this is the middle point of the index

        search_count = 0

        while min < max and search != fname[guess]: 

            search_count += 1

            if search < fname[guess]:

                max = guess -1

            else:
                min = guess + 1

            guess = int((min + max) / 2)

        if search == fname[guess]:

            print("\n\t\tYour search results for", search,": ")

            print("\t\t\tIndex: {0}\t{1:15}\t{2:15}\t{3:15}\t{4:8}{5:18}".format(guess,idP[guess].title(),lname[guess].title(),fname[guess].title(),age[guess],allegiance[guess].title())) 

            
        else:
            print("\n\tSorry your search for",search,"could NOT be found")

            print("Please check your spelling")
        
        print("BINARY SEARCH LOOPS: {}".format(search_count))

    if choice == "2": #search based on ID CODE

        print("\nYou are now searching based on ID Code")

        sort = idbubble() #calls the id specific bubble sort function

        search = input("\nPlease Enter the ID CODE of the person/people you searhing for: ")

        min = 0
        max = records - 1
        guess = int((min + max) / 2)

        search_count = 0

        while min < max and search != idP[guess]:

            search_count += 1

            if search < idP[guess]:

                max = guess - 1
            
            else:

                min = guess + 1 
            
            guess = int((min + max) / 2)

        if search == idP[guess]:

            print("\n\t\tYour search results for", search, ": ")

            print("\t\t\tIndex: {0}\t{1:15}\t{2:15}\t{3:15}\t{4:8}{5:18}".format(guess,idP[guess].title(),lname[guess].title(),fname[guess].title(),age[guess],allegiance[guess].title())) 
        
        else:

            print("\n\t\tYour search for", search," could NOT be found")
            print("\tPlease check for spelling errors")
        
        print("BINARY SEARCH LOOPS: {}".format(search_count))

    if choice == "3": #search based of last name

        print("Search based off of LAST NAME")

        search = input("Please enter the LAST NAME of the person/people you are searching for: ")

        found = []
        f = - 1

        search_count = 0

        for i in range(0 , records):

            search_count += 1

            if search == lname [i]:

                found.append(i) #this stores index of found last names to the list

                f = i
            
        if f >= 0:

            print("Your search for", search, ": ")

            for i in range(0 , len(found)):
                print("\t\t\tIndex: {0}\t{1:15}\t{2:15}\t{3:15}\t{4:8}{5:18}".format(found[i],idP[found[i]].title(),lname[found[i]].title(),fname[found[i]].title(),age[found[i]],allegiance[found[i]].title())) 

        else:

            print("Your search for", search, "could NOT be found")
            print("Please make sure your spelling is correct")

        print("Search Loop Iterations Performed: {}".format(search_count))
            
    if choice == "4": #search based off of allegiance

        print("Search based off of ALLEGIANCE")

        search = input("Please enter the ALLEGIANCE of the person/people you are searching for: ")

        found = []
        f = - 1

        search_count = 0

        for i in range(0 , records):

            search_count += 1

            if search == allegiance[i]:

                found.append(i) #this stores index of found last names to the list

                f = i
            
        if f >= 0:

            print("Your search for", search, ": ")

            for i in range(0 , len(found)):
                print("\t\t\tIndex: {0}\t{1:15}\t{2:15}\t{3:15}\t{4:8}{5:18}".format(found[i],idP[found[i]].title(),lname[found[i]].title(),fname[found[i]].title(),age[found[i]],allegiance[found[i]].title())) 

        else:

            print("Your search for", search, "could NOT be found")
            print("Please make sure your spelling is correct")

        print("Search Loop Iterations Performed: {}".format(search_count))

    if choice == "5": #exit

        print("You have choosen to exit")
    

    answer = again() #ask if you would like another search
    clear() # clears the screen after every repeat search question

done = goodbye() #closing / goodbye message




