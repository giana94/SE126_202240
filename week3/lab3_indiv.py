#Giana Hardin
#Lab3 (individual)
#08/05/2022
#SE126_202240

#---------------------PROGRAM PROMP-------------------------
#Your CIO (Chief Information Officer) has asked you to determine how much it would cost the company to replace all machines that are from 2016 and earlier. He plans on spending not more than $2,000 dollars for desktops and $1,500 for laptops.  Store the data from the file lab3a.csv into lists.  Then process the lists to reprint all of the file information (exactly as you did in Lab 2) and also produce an end report that lists the number of desktops that will be replaced, the cost to replace the desktops, the number of laptops that will be replaced, and the cost to replace the laptops.

#------VARIABLE DICTIONARY----------

#device             assigned column [0]
#brand              assigned column [1] 
#cpu                assigned column [2]
#ram                assigned column [3]
#first_disk         assigned column [4]
#num_hdd            assigned column [5]
#second_disk        assigned column [6]
#os                 assigned column [7]
#os                 assigned column [8]
#yr                 assigned column [9]
#repl_des           counter for number of desktops to be replaced
#repl_lap           counter for number of laptops to be replaced
#costPerDes         cost per desktop
#costPerLap         cost per laptop

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
            second_disk.append("-----")
            os.append(rec[6])
            yr.append(rec[7])


        else:
            second_disk.append(rec[6])
            os.append(rec[7])
            yr.append(rec[8])




#closed file ------------------------------------------------------

#process the lists to print the data to the screen 
print("\n\t----------------------ORIGINAL FILE DATA---------------------------\n\n")
repl_des = 0
repl_lap = 0
costPerDes = int(2000)
costPerLap = int(1500)

print("{9:9}{0:10} {1:9} {2:8} {3:8} {4:11} {5:13} {6:11} {7:8} {8:8}".format(" TYPE", "BRAND", "CPU", "RAM", "DISK 1", "NUM DISKS", "DISK 2", "OS", "YEAR", "INDEX"))
print("-------------------------------------------------------------------------------------------------------")

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


    print("{9}\t {0:12} {1:7} {2:8} {3:8} {4:14} {5:10} {6:11} {7:9} {8:5}".format(device[index], brand[index], cpu[index], ram[index], first_disk[index], num_hdd[index], second_disk[index], os[index], yr[index],index))
    
print("-------------------------------------------------------------------------------------")

print("\n\tTOTAL RECORDS PROCESSED:", records)

print("\n\t\tTo replace {0} Desktops it will cost $ {1:7.2f}".format(repl_des, repl_des * costPerDes))
print("\t\tTo replace {0}  Laptops it will cost $ {1:8.2f}\n\n".format(repl_lap, repl_lap * costPerLap))



