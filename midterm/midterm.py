import csv

records = 0


#assign names to empty index
rank = []
artist = []
song = []
duration = []
bpm = []
year = [] 



#open csv file to read

with open("C:/Users/ghard/Desktop/SE126_202240/midterm/90s_songs.txt") as csvfile:

    file = csv.reader(csvfile)

    for rec in file:
        records += 1
        
        #append your index names in their perspective fields
        rank.append(rec[0])
        artist.append(rec[1])
        song.append(rec[2])
        duration.append(rec[3])
        bpm.append(rec[4])
        year.append(rec[5])

        
#formatting headers for sections        
print("\n\n{0:13} {1:20} {2:20} \t{3:7} {4:5} \t {5:7}".format("Rank","Artist","Song","Duration","BPM","Year"))
print("----------------------------------------------------------------------------")
    
    
    
#first print out of original list data
for index in range(0, records):   
        
    print("{0:13} {1:20} {2:20} \t\t{3:7} {4:5} \t {5:7}".format(rank[index], artist[index], song[index], duration[index], bpm[index], year[index]))
    
    
print("\n\nNUMBER OF Songs:",records)