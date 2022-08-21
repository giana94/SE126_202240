# Giana Hardin
# MIDTERM
# SE126_202240
# 8/21/2022

# -------------- PROGRAM ------------------
# Use a menu to give user options to view Top hit songs from the decade 1990 - 2000 from the CSV file. Using another list, add an additional column of values to each song called Tempo. This added index will depend on the BPM index from the original CSV file. Print the total number of songs played in each tempo if only the number is greater than 0. (This will show the popular tempos that are used to make the Top Hit Charts). 


# ----------- VARIABLE DICTIONARY ---------------

#menu               options to choose from
#choice             user input for menu option
#records            count of how many songs in csv file
#prestissimo        very very fast (>200 BPM)
#presto             very fast (168-200 BPM)
#allegro            fast (120-168 BPM)
#moderato           moderately (108-120 BPM)
#andante            walking pace (76-108 BPM)
#adagio             slow and stately (66-76 BPM)
#lento              very slow (40-60 BPM)
#grave              slow and solemn (20-40 BPM)
#rank               song rank from list [INDEX 0]
#artist             top hit artist [INDEX 1]
#song               top hit song [INDEX 2]
#duration           song time length [INDEX 3]
#bpm                song Beats Per Minute [INDEX 4]
#year               year song released [INDEX 5] 
#tempo              speed or pace of a given piece [INDEX 6]

#--------------------------------------------------------------------------------------------------------------------
import csv


def menu():
    
    print("1. Top Hits from 1990-2000")
    print("2. Song Tempo list! ")
    print("3. **EXIT**")
    
    choice = int(input("Please select an option (1-3): "))
    
    while choice < 0 or choice > 3:
        
        print("**INVALID OPTION! TRY AGAIN**")
        choice = int(input("Please select an option (1-3): "))
        
    return choice


records = 0
prestissimo = 0
presto = 0
allegro = 0
moderato = 0
andante = 0
adagio = 0
lento = 0
grave = 0


#assign names to empty index
rank = []
artist = []
song = []
duration = []
bpm = []
year = []
tempo = []


#open csv file to read

with open("C:/Users/ghard/Desktop/SE126_202240/midterm/90s_songs.txt") as csvfile:

    file = csv.reader(csvfile)

    for rec in file:
        records += 1
        
        #append your index names in their perspective fields
        rank.append(int(rec[0]))
        artist.append(rec[1])
        song.append(rec[2])
        duration.append(rec[3])
        bpm.append(float(rec[4]))
        year.append(rec[5])

#first print out of original list data

print("\n\t\t\t\tWelcome to Top hits of 1990-2000!! What would you like to view?\n")
menu_choice = menu()

while menu_choice != 3: 

    if menu_choice == 1:
        print("\n\n----------------------------------------ORIGINAL DATA-------------------------------------------------------")
        #formatting headers for sections        
        print("{0:10} {1:35} {2:22} {3:13} {4:5} \t{5:7}".format("RANK","ARTIST","SONG","DURATION","BPM","YEAR"))
        print("------------------------------------------------------------------------------------------------------------")

        for index in range(0, records):   

            print("{0:3.0f}\t {1:30} {2:30} \t{3:10} {4:5.1f}\t{5:5}".format(rank[index], artist[index], song[index], duration[index], bpm[index], year[index]))
        print("\n\tNUMBER OF Songs:",records)


    if menu_choice == 2:
        print("\n\n---------------------------------------------TEMPOS-----------------------------------------------------------------")
        print("{0:10} {1:35} {2:22} {3:13} {4:5} \t{5:9} {6:15}".format("RANK","ARTIST","SONG","DURATION","BPM","YEAR","TEMPO"))
        print("-------------------------------------------------------------------------------------------------------------------")
        for index in range(0, records):   
            
            if bpm[index] > 200:
                tempo_class = "Prestissimo"
                tempo.append(tempo_class)
                prestissimo += 1
            
            if bpm[index] >= 168 and  bpm[index] < 200:
                tempo_class = "Presto"
                tempo.append(tempo_class)
                presto += 1
            
            if bpm[index] >= 120 and  bpm[index] < 168:
                tempo_class = "Allegro"
                tempo.append(tempo_class)
                allegro += 1
                
            if bpm[index] >= 108 and  bpm[index] < 120:
                tempo_class = "Moderato"
                tempo.append(tempo_class)
                moderato += 1
                
            if bpm[index] >= 76 and  bpm[index] < 108:
                tempo_class = "Andante"
                tempo.append(tempo_class)
                andante += 1
                
            if bpm[index] >= 66 and  bpm[index] < 76:
                tempo_class = "Adagio"
                tempo.append(tempo_class)
                adagio += 1
                
            if bpm[index] >= 40 and  bpm[index] < 60:
                tempo_class = "Lento"
                tempo.append(tempo_class)
                lento += 1
                
            if bpm[index] >= 20 and  bpm[index] < 40:
                tempo_class = "Grave"
                tempo.append(tempo_class)
                grave += 1

            print("{0:3.0f}\t {1:30} {2:30} \t{3:10} {4:5.1f} \t{5:7}  {6:12}".format(rank[index], artist[index], song[index], duration[index], bpm[index], year[index], tempo[index]))

        print("\n")
        if prestissimo > 0:
            print("Songs played in Prestissimo: {}".format(prestissimo))
        if presto > 0:
            print("     Songs played in Presto: {}".format(presto))
        if allegro > 0:
            print("    Songs played in Allegro: {}".format(allegro))
        if moderato > 0:
            print("   Songs played in Moderato: {}".format(moderato))
        if andante > 0:
            print("    Songs played in Andante: {}".format(andante))
        if adagio > 0:
            print("     Songs played in Adagio: {}".format(adagio))
        if lento > 0:
            print("      Songs played in Lento: {}".format(lento))
        if grave > 0:
            print("      Songs played in Grave: {}".format(grave))

    print("\n")
    menu_choice = menu()


print("\n\n\t\tObrigada! Have a nice day!!! :) \n")