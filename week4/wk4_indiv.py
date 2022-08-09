#Giana Hardin
#Lab 4 (individual)
#08/15/2022
#SE126_202240

#-----------------PROGRAM PROMPT-- 4 Individual.

#In Python, process the text file “lab4A_GOT_NEW.txt” to store each field into its own corresponding list:
#FIELD0                   FIELD1                   FIELD2                   FIELD3                   FIELD4
#Firstname            Lastname            Age                        Nickname            House Allegiance
#Then:
#Process the lists to print the them as they appear in the file
#Re-process the lists to add the House Motto (dependent on Field4/Allegiance; see motto chart below)
#Re-Process the lists to print each record fully with the House Mottos
#Re-process the lists to find the average age within the list, then
#Print the total number of people in the list
#Print the average age
#Print tallies for each allegiance (Field4)


#-----------------VARIABLE DICTIONARY
#records                count of number of people in list
#avg_age                count of index 4; all ages in list divided by records
#houseStark             count of number of people in House Stark
#houseBaratheon         count of number of people in House Baratheon
#houseTully             count of number of people in House Tully
#nightsWatch            count of number of people in Night's Watch
#houseLannister         count of number of people in House Lannister
#houseTaragaryen        count of number of people in House Taragaryen
#firstName              index[0]
#lastName               index[1]
#age                    index[2]
#nickname               index[3]
#houseAllegiance        index[4]
#motto                  index[5]
#houseMotto             appended motto to index

#------------MAIN PROGRAM---------------

#import csv file from library
import csv

records = 0
avg_age = 0
houseStark = 0
houseBaratheon = 0
houseTully = 0
nightsWatch = 0
houseLannister = 0
houseTaragaryen = 0

#assign names to empty index
firstName = []
lastName = []
age = []
nickname = []
houseAllegiance = [] 
motto = []
houseMotto = []


#open csv file to read

with open("C:/Users/ghard/Desktop/SE126_202240/week4/lab4A_GOT_NEW.txt") as csvfile:

    file = csv.reader(csvfile)

    for rec in file:
        records += 1
        
        #append your index names in their perspective fields
        firstName.append(rec[0])
        lastName.append(rec[1])
        age.append(int(rec[2]))
        nickname.append(rec[3])
        houseAllegiance.append(rec[4])
        
#formatting headers for sections        
print("\n\n{0:13} {1:13} {2} \t{3:20} {4:13}".format("First Name","Last Name","Age","Nickname","House Allegience"))
print("----------------------------------------------------------------------------")
    
    
    
#first print out of original list data
for index in range(0, records):   
        
    print("{0:13} {1:13} {2} \t\t{3:20} {4:13}".format(firstName[index], lastName[index], age[index], nickname[index], houseAllegiance[index]))


print("\n\n\n{0:13} {1:13} {2} \t{3:20} {4:25} {5:20}".format("First Name","Last Name","Age","Nickname","House Allegience","Motto"))

print("---------------------------------------------------------------------------------------------------------")

#second print of list with added house motto and tally count per house
for index in range(0,records):

    if houseAllegiance[index] == "House Stark":
        motto = "Winter is Coming"
        houseMotto.append(motto)
        houseStark += 1
        
    if houseAllegiance[index] == "House Baratheon":
        motto = "Ours is the fury."
        houseMotto.append(motto)
        houseBaratheon += 1
    
    if houseAllegiance[index] == "House Tully":
        motto = "Family. Duty. Honor."
        houseMotto.append(motto)
        houseTully += 1
    
    if houseAllegiance[index] == "Night's Watch":
        motto = "And now my watch begins."
        houseMotto.append(motto)
        nightsWatch += 1
    
    if houseAllegiance[index] == "House Lannister":
        motto = "Hear me roar!"
        houseMotto.append(motto)
        houseLannister += 1
    
    if houseAllegiance[index] == "House Targaryen":
        motto = "Fire & Blood"
        houseMotto.append(motto)
        houseTaragaryen += 1
    

    print("{0:13} {1:13} {2} \t\t{3:20} {4:22} {5:20}".format(firstName[index], lastName[index], age[index], nickname[index], houseAllegiance[index],houseMotto[index]))
        
        
#finding the average age from index
    
    avg_age += age[index]
    
#avg_age = average age / records
    
avg_age /= records


print("\n\nNUMBER OF PEOPLE LISTED:",records)
print("AVERAGE AGE: {:.1f}\n".format(avg_age))

print("\n\nNUMBER OF PEOPLE IN EACH HOUSE:\n")
print("     House Stark:", houseStark)
print(" House Baratheon:", houseBaratheon)
print("     House Tully:", houseTully)
print("   Night's Watch:", nightsWatch)
print(" House Lannister:", houseLannister)
print("House Taragaryen:", houseTaragaryen,"\n\n")