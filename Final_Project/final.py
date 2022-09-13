#----------PROGRAM PROMPT----------
#Our program takes a list of Rap/Hip-Hop albums and lists them out starting from album name, artist name, year, and whether its explicit or not. Then the program will ask you to pick an option from the list of search methods:
# 1. Search by Album
# 2. Search by Artist
# 3. Search by Year
# 4. Give Random Album
# . Exit
#Depending on which option the user chooses, the program will use either binary search or sequential search. Then Ransom Album will give the user a random album from the list. Exit will just simply wxit the program. Also, before each new search teh screen will clear. 

#----------VARIABLE DICTIONARY----------
def menu():
    print("\n\n\tSEARCH MENU\n")
    print("1.	Search by ALBUM")
    print("2.	Search by ARTIST")
    print("3.	Search by YEAR")
    print("4.	Give Random Album")
    print("5.	EXIT")
    
    choice = int(input("\n\tPlease enter your selection [1 - 5]: "))
    
    while choice <= 0 or choice > 5:
        
        print("\t\t\t\t**ERROR!** Invalid Entry")
        choice = int(input("\n\tPlease enter your selection [1 - 5]: "))

    return choice


def bubble(): #ID code ascending order
        for i in range(0, records - 1):#outter loop
            for index in range(0, records - 1):#inner loop
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
    answer = input("\n\n\tWould you like to search again? [y/n]: ").lower()
    while answer != "n" and answer != "y":
        print("\t\t **ERROR** Invalid Entry")
        answer = input("\n\n\tWould you like to search again? [y/n]: ").lower()
    return answer

#----------MAIN PROGRAM----------
import csv

album = []
artist = []
year = []
explicit = []

records = 0

with open("C:/Users/ghard/Desktop/SE126_202240/Final_Project/Final_Project_Data.txt") as csvfile:
    file = csv.reader(csvfile)

    for rec in file:

        records += 1
        album.append(rec[0])
        artist.append(rec[1])
        year.append(rec[2])
        explicit.append(rec[3])
    print("\nRecords in file: {}".format(records))
    
print("\n{0:13}\t{1:24}\t{2:20}\t{3:15} {4}".format("Index", "Album", "Artist", "Year", "Explicit"))
print("---------------------------------------------------------------------------------------------------------")
for i in range(0,records):
    print("{0:3}\t{1:35} {2:27} {3:15} {4:25}".format(i + 1, album[i], artist[i], year[i], explicit[i]))
    
answer = "y"

while answer == "y":
    choice = menu()
    
    if choice == 1:
        print("binary Search for Album")
        bubble()
        search = input("\n\n\tEnter the ALBUM you are looking for: ")

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

            print("\n\t\tYour BINARY SEARCH results for ", search, ": ")
            print("\n{0:13}\t{1:24}\t{2:20}\t{3:15} {4}".format("Index", "Album", "Artist", "Year", "Explicit"))
            print("---------------------------------------------------------------------------------------------------------")
            print("{0:3}\t{1:35} {2:27} {3:15} {4:25}".format(i + 1, album[guess], artist[guess], year[guess], explicit[guess]))

        else:
            print("\n\tYour BINARY SEARCH results for ", search, ": could NOT BE FOUND. ")
            print("\tPlease check your spelling and try again!")
        print("\nBINARY SEACH LOOPS: {}".format(search_count))
    answer = again()
print("okayyyy byeeeeee")