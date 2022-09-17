#The Python Pals
#SE126_202240
#Final Project
#9/21/22

#-------------------PROGRAM PROMPT-------------------
#Our program takes a list of Rap/Hip-Hop albums and lists them out starting from album name, artist name, year, and whether its explicit or not. Then the program will ask you to pick an option from the list of search methods:
# 1. Search by Album
# 2. Search by Artist
# 3. Search by Year
# 4. Give Random Album
# 5. Check out our playlist
# 6. Exit
#Depending on which option the user chooses, the program will use either binary search or sequential search. Then Ransom Album will give the user a random album from the list. Exit will just simply wxit the program. Also, before each new search teh screen will clear. 

#-------------------VARIABLE DICTIONARY-------------------

#records                number of records in file
#album                  list of the album titles
#artist                 list of the artists names
#year                   list of the years
#explicit               list of whether or not an album is explicit
#answer                 Y to stay in loop 
#choice                 user input menu options
#search                 user input within each choice
#found                  sequential search found results
#search_count           sequential search loops count
#rand                   random function
#-------------------FUNCTIONS-------------------

def menu():
    print("\n\n\t\t♫ Welcome to the Python Pals Music Shop. Feel free to take a look at our Search Menu Below ♫")
    
    print("\n\tSEARCH MENU\n")
    print("1.	Search by ALBUM")
    print("2.	Search by ARTIST")
    print("3.	Search by YEAR")
    print("4.	Give Random Album")
    print("5.	Check out our playlist")
    print("6.	EXIT")
    
    choice = input("\n\tPlease make a selection from the follwing options [1 - 6]: ")

    while choice != "1" and choice != "2" and choice != "3" and choice != "4" and choice != "5" and choice != "6":
        
        print("\t\t\t\t**ERROR!** Invalid Entry")
        choice = input("\n\tPlease enter your selection [1 - 6]: ")

    return choice

def bubble(): #Album ascending order
        for i in range(0, records - 1):#outter loop
            for index in range(0, records - 1):#inner loop
                if(album[index] > album[index + 1]): 
                    
                    temp = album[index]                 #Swap all other values
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
    answer = input("\n\n\tWould you like to search again? [y/n]: ").lower()
    os.system('cls')
    while answer != "n" and answer != "y":
        print("\t\t **ERROR** Invalid Entry")
        answer = input("\n\n\tWould you like to search again? [y/n]: ").lower()
    return answer

def bye():
    os.system('cls')
    print("\n\n\t\t\tThank you for coming to the Python Pals music shop! ♫\n\n")

#-------------------MAIN PROGRAM-------------------

import csv
import random
import os 
import webbrowser

album = []
artist = []
year = []
explicit = []

records = 0

with open("C:/Users/ghard/Desktop/SE126_202240/Final_Project/Final_Project_Data.txt") as csvfile:
    file = csv.reader(csvfile)

    for rec in file:

        records += 1
        album.append(rec[0].lower())
        artist.append(rec[1].lower())
        year.append(rec[2])
        
        #Adds " --- " to empty Indices if album is not Explicit
        if rec[3] == "Explicit":
            explicit.append(rec[3])
        else:
            explicit.append("--------")
            
    
    print("\nRecords in file: ",records)
    
print("\n{0:13}\t{1:24}\t{2:20}\t{3:15} {4}".format("Index", "Album", "Artist", "Year", "Explicit"))
print("---------------------------------------------------------------------------------------------------------")
for i in range(0,records):
    print("{0:3}\t{1:35} {2:27} {3:15} {4:25}".format(i + 1, album[i].title(), artist[i].title(), year[i], explicit[i]))
    
answer = "y"

while answer == "y":
    choice = menu()
    
    if choice == "1":
        print("binary Search for Album")
        bubble()
        search = input("\n\n\tEnter the FULL title of the ALBUM you are looking for: ").lower()

        min = 0                         #this is the lowest starting INDEX
        max = records -1                #the highest starting INDEX
        guess = int((min + max) / 2) #or: guess = (min + max) // 2 -> starting MIDDLE index
        search_count = 0

        while min < max and search != album[guess]:
            search_count += 1

            if search < album[guess]:   #this is for ASCENDING ORDER LISTS   " > " for descending
                max = guess - 1

            else:
                min = guess + 1

            guess = int((min + max) / 2)
            
        if search == album[guess]:

            print("\n\t\tYour BINARY SEARCH results for ", search.title(), ": ")
            print("\n{0:13}\t{1:24}\t{2:20}\t{3:15} {4}".format("Index", "Album", "Artist", "Year", "Explicit"))
            print("---------------------------------------------------------------------------------------------------------")
            print("{0:3}\t{1:35} {2:27} {3:15} {4:25}".format(i + 1, album[guess].title(), artist[guess].title(), year[guess], explicit[guess].title()))

        else:
            print("\n\tYour BINARY SEARCH results for ", search.title(), ": could NOT BE FOUND. ")
            print("\tPlease check your spelling and try again!")
        print("\nBINARY SEACH LOOPS: {}".format(search_count))
        answer = again()

    if choice == "2":
        search_count = 0
        
        search = input("\nEnter the Artist you are searching for: ").lower()
        found = []

        for i in range(0, records):
            search_count += 1

            if search == artist[i]:
                found.append(i)
        
        print("\n\n\t\tHey, this is all the info we have for", search.title(),": \n")
        print("\n{0:13}\t{1:24}\t{2:20}\t{3:15} {4}".format("Index", "Album", "Artist", "Year", "Explicit"))
        print("---------------------------------------------------------------------------------------------------------")
        if len(found) > 0:
            for i in range(0, len(found)):
                print("{0:3}\t{1:35} {2:27} {3:15} {4:25}".format(found[i], album[found[i]].title(), artist[found[i]].title(), year[found[i]], explicit[found[i]].title()))
        else:
            print("\n\tYour search for ", search.title(), " was NOT FOUND. Please check your spelling!")

        print("\n\nSearch Loop Iterations Performed: {}".format(search_count))
        answer = again()

    if choice == "3":
        
        search_count = 0
        
        search = input("\nPlease enter the Year you are searching for: ")
        found = []

        for i in range(0, records):
            search_count += 1

            if search == year[i]:
                found.append(i)

        print("\n\n\t\t\tYour SEQUENTIAL SEARCH results for", search,":")
        print("\n{0:13}\t{1:24}\t{2:20}\t{3:15} {4}".format("Index", "Album", "Artist", "Year", "Explicit"))
        print("---------------------------------------------------------------------------------------------------------")
        
        if len(found) > 0:
            for i in range(0, len(found)):
                print("{0:3}\t{1:35} {2:27} {3:15} {4:25}".format(found[i], album[found[i]].title(), artist[found[i]].title(), year[found[i]], explicit[found[i]].title()))
        else:
            print("\n\t\tYour search for ", search.title(), " was NOT FOUND. Please check your spelling!")

        print("\n\nSearch Loop Iterations Performed: {}".format(search_count))
        answer = again()


    if choice == "4":
        with open ("C:/Users/ghard/Desktop/SE126_202240/Final_Project/Final_Project_Data.txt") as csvfile:
            
            file = csv.reader(csvfile)
            rand = random.choice([line[0].lower() for line in file]) #randoom function!!
            
            for i in range(0, records):
                if rand == album[i]:
                    print("\n\nHey, we recomend you listen to: ")
                    print("\n{0:35}\t{1:25}\t{2:15} {3}".format("Album", "Artist", "Year", "Explicit"))
                    print("--------------------------------------------------------------------------------------------------------")
                    print("{0:35}\t {1:30} {2:15} {3}".format(album[i], artist[i], year[i], explicit[i]))
        answer = again()
                    
    if choice == "5": #opens a spotify playlsit within the web browser
        webbrowser.open("https://open.spotify.com/playlist/6qCz3om0TmhNXcOL5Xdj17")
        answer = again()

    if choice == "6":
        print("\n\tYou have chosen to Exit!")
        answer = "n"
    
if answer == "n":
    bye()
