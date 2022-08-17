import csv

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
        rank.append(float(rec[0]))
        artist.append(rec[1])
        song.append(rec[2])
        duration.append(rec[3])
        bpm.append(float(rec[4]))
        year.append(rec[5])

print("\n\n----------------------------------------ORIGINAL DATA-------------------------------------------------------")
#formatting headers for sections        
print("{0:10} {1:35} {2:22} {3:13} {4:5} \t{5:7}".format("RANK","ARTIST","SONG","DURATION","BPM","YEAR"))
print("------------------------------------------------------------------------------------------------------------")
    
    
    
#first print out of original list data
for index in range(0, records):   
        
    print("{0:3.0f}\t {1:30} {2:30} \t{3:10} {4:5.1f}\t{5:5}".format(rank[index], artist[index], song[index], duration[index], bpm[index], year[index]))
    
    
print("\n\n---------------------------------------------TEMPO-----------------------------------------------------------------")
print("{0:10} {1:35} {2:22} {3:13} {4:5} \t{5:9} {6:15}".format("RANK","ARTIST","SONG","DURATION","BPM","YEAR","TEMPO"))
print("-------------------------------------------------------------------------------------------------------------------")


for index in range(0,records):
    
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
    
    
    
    
    
    
    
    
    
    
    
    
    
    
print("\n\nNUMBER OF Songs:",records)
print("Songs played in Prestissimo: {}".format(prestissimo))
print("Songs played in Presto: {}".format(presto))
print("Songs played in Allegro: {}".format(allegro))
print("Songs played in Moderato: {}".format(moderato))
print("Songs played in Andante: {}".format(andante))
print("Songs played in Adagio: {}".format(adagio))
print("Songs played in Lento: {}".format(lento))
print("Songs played in Grave: {}".format(grave))
