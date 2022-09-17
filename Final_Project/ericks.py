#Python Pals Final 

#Prompt: 

#Function Def:
import csv #allows pything to view csv files

from os import system, name 

import random

import webbrowser

def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')
    # for mac 
    else:
        _ = system('clear')

def menu():

    print("Welcome to the Python Pals Music Shop. Feel free to take a look at our Search Menu Below")

    print("\nSearch Menu")
    print("\n1. Search by Album")
    print("2. Search By Artist")
    print("3. Search By Year")
    print("4. Recommend a Random Album")
    print("5. Check out our playlist")
    print("6. Exit")


    pick = input("\nPlease make a selection from the following options [1-5]: ")

    while pick != "1" and pick != "2" and pick != "3" and pick !="4" and pick != "5" and pick != "6":
    
        print("\nSorry...An invalid input was made. Please try again")

        pick = input("Hello, Please make a selection friom the following below [1-5]: ")

    return pick 

def bubble():#make sure to edit this and add the varriables

    for i in range(0, records - 1):#this is the outter loop

        for index in range(0, records - 1): #inner loop
            
            if(album[index] > album[index + 1]):

                temp = album[index]
                album[index] = album[index +1]
                album[index + 1] = temp

                temp = artist[index]
                artist[index] = artist[index + 1]
                artist[index + 1] = temp

                temp = year[index]
                year[index] = year[index + 1]
                year[index + 1] = temp

                temp = explicit[index]
                explicit[index] = explicit[index + 1]
                explicit[index + 1] = temp


def again():

    answer = input("\nWould you like to add another search? [y/n]: ").lower()

    while answer != "y" and answer != "n":
        print("\nSorry wrong input")

        answer = input("Would you like to add another search? [y/n]: ").lower()

    return answer

def goodbye():
    print("Thank you for coming to the Python Pals music shop")
#Varriable Def:

#album = []
#artist = []
#year = []
#explicit = []

#records = 0

#Main Code Below:

album = []
artist= []
year = []
explicit = []

records = 0

with open ("C:/Users/ghard/Desktop/SE126_202240/Final_Project/Final_Project_Data.txt") as csvfile:

    file = csv.reader(csvfile)

    for rec in file:

        records += 1

        #add appends here
        album.append(rec[0])
        artist.append(rec[1])
        year.append(rec[2])
        explicit.append(rec[3])


print("------------------------------------------------------------------------------------------------------------------")

print("Index: {0}\t{1:15}\t{2:15}\t{3:15}\t{4:10}".format("", "Album", "Artist", "Year", "Explicit"))

print("------------------------------------------------------------------------------------------------------------------")

for i in range(0, records): 

    print("Index: {0}\t{1:15}\t{2:15}\t{3:15}\t{4:10}".format(i, album[i], artist[i],year[i],explicit[i]))

answer = "y"

while answer == "y": 

    print("\n\n")

    choice = menu()

    clear()

    if choice == "1": #search based off of album / binary search

        print("\nYou are now searching for an album")

        sort = bubble() #calls the bubble sort function

        search = input("\nPlease enter the Album you are looking for: ")

        #binary search algorithim:
        min = 0 # this is the lowest starting index
        max = records - 1 #this is the highest starting index
        guess = int((min + max) / 2)

        search_count = 0 

        while min < max and search != album[guess]:

            search_count += 1

            if search < album[guess]:

                max = guess - 1
            
            else:  

                min = guess + 1
            
            guess = int((min + max) / 2)
        
        if search == album[guess]:

            print("\nYour search results for", search,":")

            print("\nIndex: {0}\t{1:15}\t{2:15}\t{3:15}\t{4:10}".format(guess, album[guess], artist[guess],year[guess],explicit[guess]))

        else:
            print("\n\tHey sorry...It looks like we dont carry",search,"Check for spelling errors just incase")

        print("\nBINARY SEARCH LOOPS: {}".format(search_count))

    if choice == "2":#search by artist

        print("\nNow searching by Artist")

        search = input("Please enter the name of the Artist you are searching for: ")

        found = [] #empty list 
        f = - 1

        search_count = 0

        for i in range(0, records):

            if search == artist[i]:

                found.append(i)

                f = i

        if f >= 0:

            print("\nHey this is all the info we have for", search,": \n")
            for i in range(0, len(found)):
                print("Index: {0}\t{1:35}\t{2:27}\t{3:15}\t{4:10}".format(found[i], album[found[i]], artist[found[i]],year[found[i]],explicit[found[i]]))

        else:
            print("Sorry your search for", search, "could NOT be found")

    if choice == "3": #search by year

        print("\nNow searching by Year")

        search = input("Please enter the Year you are searching for: ")

        found = []
        f = - 1

        search_count = 0

        for i in range(0, records):

            if search == year[i]:

                found.append(i)

                f = i 

        if f >= 0:

            print("Your search for",search,": ")
            
            for i in range(0, len(found)):
                print("Index: {0}\t{1:35}\t{2:27}\t{3:15}\t{4:10}".format(found[i], album[found[i]], artist[found[i]],year[found[i]],explicit[found[i]]))


        else:
            print("Sorry your search for", search, "could NOT be found")

    if choice == "4": #pick a random album # hey fix this 
        with open ("C:/Users/ghard/Desktop/SE126_202240/Final_Project/Final_Project_Data.txt") as csvfile:
            file = csv.reader(csvfile)
            print("Hey, we recomend you listen to:",random.choice([line[0] for line in file]))

    if choice =="5": #opens a spotify playlsit
        webbrowser.open("https://www.google.com/")

    if choice == "6":

        print("You have choosen to exit")

    answer = again()
    clear()

done = goodbye()