#Final Project
#Python Pals

#Program Prompt: Our program takes a list of rap/hip-hop albums and lists them out starting from album name, artist name, year, and whether it’s explicit or not. Then the program will ask you to pick an option from a list of search methods:
#1.    Search my Album
#2.    Search by Artist
#3.    Search by Year
#4.    Give Random Album
#5.    Exit
#Depending on which option the user chooses, the program will use either binary search or sequential search. Then Random Album will give the user a random album from the list. Exit will just simply exit the program. Also, before each new search the screen will clear.

#Variable Dictionary:
#records - number of records in file
#album - list of the album titles
#artistName - list of the artists names
#year - list of the years
#exp - list of whether or not an album is explicit

#Functions:
def menu():
    os.system('cls')

    print("\n\tSEARCH OPTIONS")
    print("1. Search by ALBUM NAME")
    print("2. Search by ARTIST NAME")
    print("3. Search by YEAR")
    print("4. Give Random Album")
    print("5. EXIT")

    choice = input("\nWhat would you like to do? [1-5]: ")

    while choice != "1" and choice != "2" and choice != "3" and choice != "4" and choice != "5":
        print("\t\t**ERROR** INVALID ENTRY!")
        choice = input("\nWhat would you like to do? [1-5]: ")
    
    return choice

def bubSort():
    for i in range(0, records - 1):#outter loop

            print("OUTER LOOP! i = ", i)


            for index in range(0, records - 1):#inner loop

                print("\t INNER LOOP! k = ", index)

                #below if statement determines the sort

                #list used is the list being sorted

                # > is for increasing order, < for decreasing

                if(album[index] > album[index + 1]):

                    print("\t\t SWAP! ", album[index], "<-->", album[index + 1])

                    #if above is true, swap places!

                    temp = album[index]

                    album[index] = album[index + 1]

                    album[index + 1] = temp

        
                    #swap all other values

                    temp = artistName[index]

                    artistName[index] = artistName[index + 1]

                    artistName[index + 1] = temp


                    temp = year[index]
                    year[index] = year[index + 1]
                    year[index + 1] = temp

                    temp = exp[index]
                    exp[index] = exp[index + 1]
                    exp[index + 1] = temp

def repeat():
    ans = input("\n\tWould you like to search again? [y/n]: ")
    if ans != "y" and ans != "Y" and ans != "n" and ans != "N":
        print("**ERROR!** Invalid input!")
        ans = input("\n\tWould you like to search again? [y/n]: ")
    
    return ans

def goodbye():
    print("\n\tThank you for using our program! Goodbye!")

#MAIN CODE--------------------------------------------------------------------------------------------------------------------------
import csv
import os
import random

records = 0

album = []
artistName = []
year = []
exp = []

with open("C:/Users/ghard/Desktop/SE126_202240/Final_Project/Final_Project_Data.txt") as csvfile:
    file = csv.reader(csvfile)

    for rec in file:

        records += 1

        album.append(rec[0])
        artistName.append(rec[1])
        year.append(rec[2])
        exp.append(rec[3])

print("{0:35}\t{1:20}\t{2:5}\t{3:10}".format("ALBUM TITLE","ARTIST","YEAR","EXPLICIT"))
for i in range(0, records):
    print("{0:35}\t{1:20}\t{2:5}\t{3:10}".format(album[i],artistName[i],year[i],exp[i]))

answer = input("\nWould you like to start searching? [y/n]: ")

while answer == "y":

    choice = menu()

    if choice == "1":

        bubSort()

        print("\n\t\tBINARY SEARCH")

        search = input("Enter the full title of the album you are looking for: ")

        min = 0
        max = records - 1
        guess = int((min + max) / 2)

        while min < max and search != album[guess]:

            if search < album[guess]:

                max = guess - 1
                
            else:

                min = guess + 1

            guess = int((min + max) /2)
            
        if search == album[guess]:
                
            print("\t\tYour BINARY SEARCH results for", search,": ")

            print("{0:35}\t{1:20}\t{2:5}\t{3:10}".format("ALBUM TITLE","ARTIST","YEAR","EXPLICIT"))    
            print("{0:35}\t{1:20}\t{2:5}\t{3:10}".format(album[guess],artistName[guess],year[guess],exp[guess]))
            answer = repeat()
            
        else:
            print("\t\tYour BINARY SEARCH results for", search," could NOT be found. ")
            answer = repeat()
    
    if choice == "2":

        print("\n\t\tSEQUENTIAL SEARCH")

        search = input("Enter the full artist name of the person you want to search for: ")
        found = []

        for i in range(0, records):

            if search == artistName[i]:
                found.append(i)
            
    
        if len(found) > 0:
            print("\t\tYour SEQUENTIAL SEARCH results for", search,": ")
            print("{0:35}\t{1:20}\t{2:5}\t{3:10}".format("ALBUM TITLE","ARTIST","YEAR","EXPLICIT"))
            for i in range(0, len(found)):

                
                print("{0:35}\t{1:20}\t{2:5}\t{3:10}".format(album[found[i]],artistName[found[i]],year[found[i]],exp[found[i]]))
                

        else:
            print("\t\tYour SEQUENTIAL SEARCH results for", search," could NOT be found. ")
        
        answer = repeat()
    
    if choice == "3":

        print("\n\t\tSEQUENTIAL SEARCH")

        search = input("Enter the year that you want to search for: ")
        found = []

        for i in range(0, records):

            if search == year[i]:
                found.append(i)
            
    
        if len(found) > 0:
            print("\t\tYour SEQUENTIAL SEARCH results for", search,": ")
            print("{0:35}\t{1:20}\t{2:5}\t{3:10}".format("ALBUM TITLE","ARTIST","YEAR","EXPLICIT"))
            for i in range(0, len(found)):

                
                print("{0:35}\t{1:20}\t{2:5}\t{3:10}".format(album[found[i]],artistName[found[i]],year[found[i]],exp[found[i]]))
                

        else:
            print("\t\tYour SEQUENTIAL SEARCH results for", search," could NOT be found. ")
        
        answer = repeat()
    
    if choice == "4":

        randomAlbum = random.choice(album)

        bubSort()

        search = randomAlbum

        min = 0
        max = records - 1
        guess = int((min + max) / 2)

        while min < max and search != album[guess]:

            if search < album[guess]:

                max = guess - 1
                
            else:

                min = guess + 1

            guess = int((min + max) /2)
            
        if search == album[guess]:
                
            print("\n\t\t\t\tYOUR ALBUM IS:")

            print("{0:35}\t{1:20}\t{2:5}\t{3:10}".format("ALBUM TITLE","ARTIST","YEAR","EXPLICIT"))    
            print("{0:35}\t{1:20}\t{2:5}\t{3:10}".format(album[guess],artistName[guess],year[guess],exp[guess]))
            answer = repeat()

    if choice == "5":
        goodbye()
        answer = "n"
    
if answer == "n" or answer == "N":
    goodbye()