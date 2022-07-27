import csv

records = 0

#header
print("\nDATA FROM FILE--------------------------------------")
print("{0:8}    {1:8}   {2}     {3}  {4}    {5}         {6}     {7}     {8}".format("TYPE", "BRAND", "CPU", "RAM", "DISK 1", "NUM DISKS", "DISK 2", "OS", "YEAR"))


with open("C:/Users/008018155/Desktop/SE126_202240/review_se116/lab2b/lab2b.csv") as csvfile:

    file = csv.reader(csvfile)

    for rec in file: #one record at a time 
        #entire code block applies to ONE record..... at a time

        records += 1

        type_ =rec[0]
        manu = rec[1]
        cpu = rec[2]
        ram = rec[3]
        first_disk = rec[4]
        num_disks = rec[5]

        #fiels below change per year
        second_disk = ""
        os = ""
        year = ""
        

        if type_ =="D":
            type_ = "Desktop"

        elif type_ == "L":
            type_ = "Laptop"

        else:
            #error in file check 
            point = records - 1
            type_ = "ERROR @ record " + str(point)




        if num_disks == "1":
            #no second disk
            os = rec[6]
            year = rec[7]
            second_disk = "---"


        print("{0:8}     {1:8}   {2}     {3:3}  {4:6}    \t{5:9}   \t {6:6}   {7:2} \t  {8:4}".format(type_, manu, cpu, ram, first_disk, num_disks, second_disk, os, year))

print("\n\nRECORDS:{0}".format(records))