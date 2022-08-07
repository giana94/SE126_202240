#Giana Hardin
#Lab3 (individual)
#08/05/2022
#SE126_202240

#---------------------PROGRAM PROMP-------------------------
#Your CIO (Chief Information Officer) has asked you to determine how much it would cost the company to replace all machines that are from 2016 and earlier. He plans on spending not more than $2,000 dollars for desktops and $1,500 for laptops.  Store the data from the file lab3a.csv into lists.  Then process the lists to reprint all of the file information (exactly as you did in Lab 2) and also produce an end report that lists the number of desktops that will be replaced, the cost to replace the desktops, the number of laptops that will be replaced, and the cost to replace the laptops.

#------VARIABLE DICTIONARY----------
# 
# ******DONT FORGET THIS*******


#--------MAIN PROGRAM----------------



import csv

records = 0

#prepare empty lists - one for EVERY POSSIBLE field in the file
device =[]
brand = []
cpu = []
ram =[]
first_disk = []
num_hdd = []
second_disk = []
os = []
yr = []


#connect to and open file ----------------------------------------
with open ("C:/Users/ghard/Desktop/SE126_202240/week3/lab3a.csv")as csvfile:

    file = csv.reader(csvfile)

    for rec in file:

        records += 1
        #print(rec)

        #add data from file to lists - .append()
        device.append(rec[0])
        brand.append(rec[1])
        cpu.append(rec[2])
        ram.append(rec[3])
        first_disk.append(rec[4])
        num_hdd.append(rec[5])

        if rec[5] == "1":
            second_disk.append("-none-")
            os.append(rec[6])
            yr.append(rec[7])


        else:
            second_disk.append(rec[6])
            os.append(rec[7])
            yr.append(rec[8])




#closed file ------------------------------------------------------

#process the lists to print the data to the screen 
print("\n\tORIGINAL FILE DATA---------------------------")
repl_des = 0
repl_lap = 0

for index in range(0, records):

    if device[index] == "D":
        #change to desktop
        device[index] = "Desktop"
        if yr[index] <= "16":
            repl_des += 1

    elif device[index] == "L":
        device[index] = "Laptop"
        if yr[index] <= "16":
            repl_lap += 1

    #change brands


    print("INDEX#{9}:\t{0:8}\t{1}\t{2}\t{3}\t{4}\t{5}\t{6}\t{7}\t{8}".format(device[index], brand[index], cpu[index], ram[index], first_disk[index], num_hdd[index], second_disk[index], os[index], yr[index], index))

print("\n\tTHERE ARE {0} Desktop DEVICES / {1} Laptop DEVICES".format(repl_des, repl_lap))

print("\t-----------------------------------------------")

#prepare counting variables 
ram8 = 0
ram16 = 0
#process the lists to determine the number of 8 rams and 16 rams
for i in range(0, records):
    
    if ram[i] == "08":

        ram8 += 1

    elif ram[i] == "16":

        ram16 += 1

    else:

        print("*ERROR* encountered at index {}".format(i))

print("\n\tTHERE ARE {0} 8GB RAM DEVICES / {1} 16GB RAM DEVICES".format(ram8, ram16))

print("\n\n\tTOTAL RECORDS:", records)

