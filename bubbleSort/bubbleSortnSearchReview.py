import csv
records = 0

lastname = []
firstname = []
age = []

with open("C:/Users/ghard/Desktop/SE126_202240/bubbleSort/GOT_bubble_sort.txt") as csvfile:

    file = csv.reader(csvfile)

    for rec in file:
        records += 1

        lastname.append(rec[0])
        firstname.append(rec[1])
        age.append(int(rec[2]))

for i in range(0, records):
    print("{0:15}\t{1:15}\t{2:5}".format(lastname[i], firstname[i], age[i]))


answer = "y"

while answer == "y":
    
    print("SEARCH OPTIONS")
    print("1. Search for multiples of 1 name [LASTNAME]")
    print("2. Search for unique name [FIRSTNAME]")
    print("3. EXIT")

    choice = input("Enter which you would like to do [1-3]: ")

    while answer != "y" and answer != "n":
        print("\t\t**ERORR** INVALID ENTRY")
        choice = input("Enter which you would like to do [1-3]: ")
    
    
    #SEQUENTIAL SEARCH----------------
    if choice == "1":
        
        print("\t\t~SEQUENTIAL SEARCH")

        search = input("Enter the LASTNAME of the person/people you are looking for: ")
        
        found = []
        f = -1
        
        for i in range(0, records):

            if search == lastname[i]:

                found.append(i) #stores index of found lastname to the found list
                f = i

        if f >= 0:

            print("\t\tYour SEQUENTIAL SEARCH results for ", search, ": ")

            for i in range(0, len(found)):
                print("INDEX: {3}\t{0:15}\t{1:15}\t{2:5}".format(lastname[found[i]], firstname[found[i]], age[found[i]],found[i]))

        else:
            print("\t\tYour SEQUENTIAL SEARCH results for ", search, ": could NOT BE FOUND. ")
            print("Please check your spelling and try again :]")


    if choice == "2":
    #BUBBLE SORT - REQUIRED for BINARY SEARCH! MUST HAPPEN FIRST :]
    
        for i in range(0, records - 1):#outter loop

            print("OUTER LOOP! i = ", i)


            for index in range(0, records - 1):#inner loop

                print("\t INNER LOOP! k = ", index)

                #below if statement determines the sort

                #list used is the list being sorted

                # > is for increasing order, < for decreasing

                if(firstname[index] > firstname[index + 1]):

                    print("\t\t SWAP! ", firstname[index], "<-->", firstname[index + 1])

                    #if above is true, swap places!

                    temp = firstname[index]
                    firstname[index] = firstname[index + 1]
                    firstname[index + 1] = temp

                    #swap all other values

                    temp = age[index]
                    age[index] = age[index + 1]
                    age[index + 1] = temp
                    
                    temp = lastname[index]
                    lastname[index] = lastname[index +1]
                    lastname[index + 1] = temp
                

    #BINARY SEARCH----------------------------
        print("\t\t~BINARY SEARCH")

        search = input("Enter the FIRST NAME of the person/people you are looking for: ")

        min = 0                         #this is the lowerst starting INDEX
        max = records -1                #the highest starting INDEX
        guess = int((min + max) / 2) #or: guess = (min + max) // 2 -> starting MIDDLE index

        while min < max and search != firstname[guess]:

            if search < firstname[guess]:   #this is for ASCENDING ORDER LISTS   " > " for descending

                max = guess - 1

            else:
                min = guess + 1

            guess = int((min + max) / 2)
            
        if search == firstname[guess]:

            print("\t\tYour BINARY SEARCH results for ", search, ": ")

            print("\t{0:15}\t{1:15}\t{2:5}".format(lastname[guess], firstname[guess], age[guess]))

        else:
            print("\t\tYour BINARY SEARCH results for ", search, ": could NOT BE FOUND. ")
            print("Please check your spelling and try again :]")

    
    
    
    #EXIT----------------------
